"""
Download tool dependencies, if needed - yt-dlp, ffmpeg, and ffprobe
"""

# pylint: disable=missing-function-docstring

import os
import platform
import shutil
import stat
from io import StringIO
from pathlib import Path
from tempfile import NamedTemporaryFile

import requests
from platformdirs import user_data_dir
from PySide6.QtCore import QThread, QTimer, Signal
from PySide6.QtWidgets import QWidget
from tqdm import tqdm

from .metadata import properties
from .ui.download_ui import Ui_Download

app_name = properties.app_name
data_dir = Path(user_data_dir(app_name, None))

bin_dir = data_dir / "bin"

YT_DLP_RELEASES_URL_PREFIX = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/"
IMAGEIO_URL_PREFIX = "https://github.com/imageio/imageio-binaries/raw/183aef992339cc5a463528c75dd298db15fd346f/ffmpeg/" # pylint: disable="line-too-long"

class DownloadWindow(QWidget, Ui_Download):
    "download window"

    finished = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.setMaximum(100)
        self.missing = []

        self.get_missing_dep()

        if self.missing:
            self.show()
            self.download_init()
        else:
            QTimer.singleShot(0, self.finished.emit)

    def get_missing_dep(self):
        binaries = {
            "Linux": {
                "ffmpeg": "ffmpeg-linux64-v4.1",
                "ffprobe": "ffprobe-linux64-v4.1",
                "yt-dlp": "yt-dlp_linux",
            },
            "Darwin": {
                "ffmpeg": "ffmpeg-osx64-v4.1",
                "ffprobe": "ffprobe-osx64-v4.1",
                "yt-dlp": "yt-dlp_macos",
            },
            "Windows": {
                "ffmpeg": "ffmpeg-win64-v4.1.exe",
                "ffprobe": "ffprobe-win64-v4.1.exe",
                "yt-dlp": "yt-dlp.exe",
            },
        }

        exes = [exe for exe in ["ffmpeg", "ffprobe", "yt-dlp"] if not shutil.which(exe)]
        os_ = platform.system()

        if exes:
            if not os.path.exists(bin_dir):
                os.makedirs(bin_dir)
            for exe in exes:
                if exe == "yt-dlp":
                    url = (
                        YT_DLP_RELEASES_URL_PREFIX + binaries[os_][exe]
                    )
                else:
                    url = (
                        IMAGEIO_URL_PREFIX + binaries[os_][exe]
                    )
                filename = os.path.join(bin_dir,
                                        f"{exe}.exe" if os_ == "Windows" else exe
                                       )

                self.missing += [[url, filename]]

    def download_init(self):
        url, filename = self.missing[0]
        self.downloader = _D_Worker(url, filename)
        self.downloader.progress.connect(self.update_progress)
        self.downloader.finished.connect(self.downloader.deleteLater)
        self.downloader.finished.connect(self.on_download_finished)
        self.downloader.start()

    def on_download_finished(self):
        _url, filename = self.missing.pop(0)
        st = os.stat(filename)
        os.chmod(filename, st.st_mode | stat.S_IEXEC)

        if self.missing:
            self.download_init()
        else:
            self.finished.emit()

    def update_progress(self, progress, data):
        self.pb.setValue(progress)
        self.lb_progress.setText(data)


class _D_Worker(QThread):
    """
    Worker thread for downloading tools
    """

    progress = Signal(int, str)

    def __init__(self, url, filename=None):
        super().__init__()
        self.url = url
        self.filename = filename

    def run(self):
        if not self.filename:
            self.filename = os.path.basename(self.url)
        r = requests.get(self.url, stream=True, timeout=10)
        file_size = int(r.headers.get("content-length", 0))
        scaling_factor = 100 / file_size
        data = StringIO()
        chunk_size = 1024
        read_bytes = 0

        with (
            NamedTemporaryFile(mode="wb", delete=False) as temp,
            tqdm(
                desc=os.path.basename(self.filename),
                total=file_size,
                unit="iB",
                unit_scale=True,
                unit_divisor=1024,
                file=data,
                bar_format=(
                    "{desc}: {n_fmt}/{total_fmt} [{elapsed}/{remaining}, "
                    "{rate_fmt}{postfix}]"
                ),
                leave=True,
            ) as bar,
        ):
            for chunk in r.iter_content(chunk_size=chunk_size):
                temp.write(chunk)
                bar.update(chunk_size)
                read_bytes += chunk_size
                self.progress.emit(
                    read_bytes * scaling_factor, data.getvalue().split("\r")[-1].strip()
                )
        data.close()
        shutil.move(temp.name, self.filename)
