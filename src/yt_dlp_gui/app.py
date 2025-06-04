"""
Main GUI app
"""

import logging
import os
import sys
from pathlib import Path

import toml
from platformdirs import (
    user_log_dir,
)
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from . import (
    config,
    dep_dl,
)
from .metadata import properties

# we need to import icon resources even if apparently not used --
# <https://doc.qt.io/qtforpython-6/tutorials/basictutorial/qrcfiles.html>
from .ui import icons_rc  # noqa: F401 # pylint: disable=unused-import
from .ui.app_ui import Ui_MainWindow
from .worker import Worker

app_name = properties.app_name
version_str = properties.version + " " + properties.commit
log_dir = Path(user_log_dir(app_name, None))
log_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s (%(module)s:%(lineno)d) %(message)s",
    handlers=[
        logging.FileHandler(log_dir / "debug.log", encoding="utf-8", delay=True),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# we need run-time dependency tools - which we might already have
# downloaded to bin_dir - to be on the PATH
logger.debug("adding bin_dir '%s' to PATH", dep_dl.bin_dir)
os.environ["PATH"] += os.pathsep + str(dep_dl.bin_dir)

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    "Main app window"

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tw.setColumnWidth(0, 200)
        self.link_edit.setFocus()
        self.load_config()
        self.statusBar.showMessage(version_str)

        self.form = dep_dl.DownloadWindow()
        self.form.finished.connect(self.form.close)
        self.form.finished.connect(self.show)

        self.to_dl = {}
        self.worker = {}
        self.index = 0

        ## set up widget bindings

        self.path_btn.clicked.connect(self.button_path)

        # user has selected a different preset - load it from config
        self.format_combo.currentTextChanged.connect(self.load_preset)

        # user clicked to 'save' the preset
        self.save_preset_btn.clicked.connect(self.save_preset)

        # user clicked to add an item
        self.add_btn.clicked.connect(self.button_add)

        # user clicked to clear an item
        self.clear_btn.clicked.connect(self.button_clear)

        # user clicked to download an item
        self.download_btn.clicked.connect(self.button_download)

        # user clicked to remove an item
        self.tw.itemClicked.connect(self.remove_item)

    def remove_item(self, item, _column):
        "remove an item from the treeview"

         # pylance claims the .Yes / .No constants don't exist.
         # But they do according to the pyqt docco - see
         #   <https://doc.qt.io/qt-6/qmessagebox.html#StandardButton-enum>.
         # TODO: test to see who's right.
         # ruff: noqa: E501
         # cf https://github.com/ArthurKun21/yt-dlp-gui/commit/ad228768121eb3df8c54665268a7aad5d72cc1c2#diff-fc3b1a787c6d94d379c141d039d3d5eb98ba8804720945de123abb50a167006c # pylint: disable=line-too-long
        ret = qtw.QMessageBox.question(
            self,
            "Application Message",
            f"Would you like to remove {item.text(0)} ?",
            qtw.QMessageBox.Yes | qtw.QMessageBox.No,
            qtw.QMessageBox.No,
        )
        if ret == qtw.QMessageBox.Yes:
            if self.to_dl.get(item.id):
                logger.debug("Removing queued download (%s): %s", item.id, item.text(0))
                self.to_dl.pop(item.id)
            elif worker := self.worker.get(item.id):
                logger.info(
                    "Stopping and removing download (%s): %s", item.id, item.text(0)
                )
                worker.stop()
            self.tw.takeTopLevelItem(self.tw.indexOfTopLevelItem(item))

    def button_path(self):
        path = qtw.QFileDialog.getExistingDirectory(
            self,
            "Select a folder",
            self.path_edit.text() or qtc.QDir.homePath(),
            qtw.QFileDialog.Option.ShowDirsOnly,
        )

        if path:
            self.path_edit.setText(path)

    def button_add(self):
        missing = {}
        link = self.link_edit.text()
        path = self.path_edit.text()
        filename = self.filename_edit.text()

        if not link:
            missing["Link"] = link
        if not self.fmt:
            missing["Format"] = self.fmt
        if "path" in self.preset and not path:
            missing["Path"] = path
        if "filename" in self.preset and not filename:
            missing["Filename"] = filename

        if not all(missing.values()):
            missing_fields = ", ".join(missing.keys())
            return qtw.QMessageBox.information(
                self,
                "Application Message",
                f"Required fields ({missing_fields}) are missing.",
            )

        item = qtw.QTreeWidgetItem(
            self.tw, [link, self.fmt, "-", "0%", "Queued", "-", "-"]
        )
        pb = qtw.QProgressBar()
        pb.setStyleSheet("QProgressBar { margin-bottom: 3px; }")
        pb.setTextVisible(False)
        self.tw.setItemWidget(item, 3, pb)
        for i in range(1, 6):
            item.setTextAlignment(i, qtc.Qt.AlignmentFlag.AlignCenter)

        item.id = self.index # type: ignore
        self.link_edit.clear()

        self.to_dl[self.index] = Worker(
            item,
            self.preset["args"],
            link,
            path,
            filename,
            self.fmt,
            self.sponsorblock_combo.currentText(),
            self.metadata_check.isChecked(),
            self.thumbnail_check.isChecked(),
            self.subtitles_check.isChecked(),
        )
        logger.info("Queue download (%s) added: %s", item.id, self.to_dl[self.index]) # type: ignore
        self.index += 1

    def button_clear(self):
        if self.worker:
            return qtw.QMessageBox.critical(
                self,
                "Application Message",
                "Unable to clear list because there are active downloads in progress.\n"
                "Remove a download by clicking on it.",
            )

        self.worker = {}
        self.to_dl = {}
        self.tw.clear()

    def button_download(self):
        """
        User clicked to download an item
        """

        if not self.to_dl:
            return qtw.QMessageBox.information(
                self,
                "Application Message",
                "Unable to download because there are no links in the list.",
            )

        for k, v in self.to_dl.items():
            self.worker[k] = v
            self.worker[k].finished.connect(self.worker[k].deleteLater)
            self.worker[k].finished.connect(lambda x: self.worker.pop(x))
            self.worker[k].progress.connect(self.update_progress)
            self.worker[k].start()

        self.to_dl = {}

    def load_config(self):
        """
        load config from our config file into self.config,
        populate widgets
        """

        config_path = config.config_file_path

        try:
            self.config = config.load_toml()
        except FileNotFoundError:
            qtw.QMessageBox.critical(
                self,
                "Application Message",
                f"Config file not found at: {config_path}",
            )
            qtw.QApplication.exit()
        except toml.decoder.TomlDecodeError:
            qtw.QMessageBox.critical(
                self,
                "Application Message",
                "Config file TOML decoding failed, check the log file for more info.",
            )
            logger.error("Config file TOML decoding failed", exc_info=True)
            qtw.QApplication.exit()

        self.format_combo.addItems(self.config["presets"].keys())
        self.format_combo.setCurrentIndex(self.config["general"]["format"])
        self.load_preset(self.format_combo.currentText())

    def save_preset(self):
        """
        User clicked to save a preset -- store it to config file
        """

        if "path" in self.preset:
            self.preset["path"] = self.path_edit.text()
        if "sponsorblock" in self.preset:
            self.preset["sponsorblock"] = self.sponsorblock_combo.currentIndex()
        if "metadata" in self.preset:
            self.preset["metadata"] = self.metadata_check.isChecked()
        if "subtitles" in self.preset:
            self.preset["subtitles"] = self.subtitles_check.isChecked()
        if "thumbnail" in self.preset:
            self.preset["thumbnail"] = self.thumbnail_check.isChecked()
        if "filename" in self.preset:
            self.preset["filename"] = self.filename_edit.text()

        config.save_toml(self.config)

        qtw.QMessageBox.information(
            self,
            "Application Message",
            f"Preset for {self.fmt} saved successfully.",
        )

    def load_preset(self, fmt):
        """
        User has selected a different preset - load the values
        from our in-mem config into the widgets.
        """

        preset = self.config["presets"].get(fmt)

        if not preset:
            self.path_edit.clear()
            self.path_btn.setEnabled(False)
            self.sponsorblock_combo.setCurrentIndex(-1)
            self.sponsorblock_combo.setEnabled(False)
            self.metadata_check.setChecked(False)
            self.metadata_check.setEnabled(False)
            self.subtitles_check.setChecked(False)
            self.subtitles_check.setEnabled(False)
            self.thumbnail_check.setChecked(False)
            self.thumbnail_check.setEnabled(False)
            self.filename_edit.clear()
            self.filename_edit.setEnabled(False)
            self.link_edit.setEnabled(False)
            self.gb_controls.setEnabled(False)
            return

        if not preset.get("args"):
            qtw.QMessageBox.critical(
                self,
                "Application Message",
                "The args key does not exist in the current preset and "
                "therefore it cannot be used.",
            )
            self.format_combo.setCurrentIndex(-1)
            return

        logger.debug("Changed format to %s preset: %s", fmt, preset)
        self.link_edit.setEnabled(True)
        self.gb_controls.setEnabled(True)

        if "path" in preset:
            self.path_btn.setEnabled(True)
            self.path_edit.setText(preset["path"])
        else:
            self.path_edit.clear()
            self.path_btn.setEnabled(False)

        if "sponsorblock" in preset:
            self.sponsorblock_combo.setEnabled(True)
            self.sponsorblock_combo.setCurrentIndex(preset["sponsorblock"])
        else:
            self.sponsorblock_combo.setCurrentIndex(-1)
            self.sponsorblock_combo.setEnabled(False)

        if "metadata" in preset:
            self.metadata_check.setEnabled(True)
            self.metadata_check.setChecked(preset["metadata"])
        else:
            self.metadata_check.setChecked(False)
            self.metadata_check.setEnabled(False)

        if "subtitles" in preset:
            self.subtitles_check.setEnabled(True)
            self.subtitles_check.setChecked(preset["subtitles"])
        else:
            self.subtitles_check.setChecked(False)
            self.subtitles_check.setEnabled(False)

        if "thumbnail" in preset:
            self.thumbnail_check.setEnabled(True)
            self.thumbnail_check.setChecked(preset["thumbnail"])
        else:
            self.thumbnail_check.setChecked(False)
            self.thumbnail_check.setEnabled(False)

        if "filename" in preset:
            self.filename_edit.setEnabled(True)
            self.filename_edit.setText(preset["filename"])
        else:
            self.filename_edit.clear()
            self.filename_edit.setEnabled(False)

        self.preset = preset
        self.fmt = fmt

    def closeEvent(self, event):
        """
        Handle app closing - save our config
        """

        self.config["general"]["format"] = self.format_combo.currentIndex()
        config.save_toml(self.config)
        event.accept()

    def update_progress(self, item, emit_data):
        try:
            for data in emit_data:
                index, update = data
                if index != 3:
                    item.setText(index, update)
                else:
                    pb = self.tw.itemWidget(item, index)
                    if isinstance(pb, qtw.QProgressBar):
                        pb.setValue(round(float(update.replace("%", ""))))
        except AttributeError:
            logger.info("Download (%s) no longer exists", item.id)

def main(): # pylint: disable=missing-function-docstring
    config.create_config_if_needed()
    app = qtw.QApplication(sys.argv)
    _window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

