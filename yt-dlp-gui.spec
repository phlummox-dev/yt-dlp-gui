# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
from PyInstaller.utils.hooks import copy_metadata
import sys
from pathlib import Path

# TODO: we could, if desired, detect whether to enabled debugging (e.g. look for an env var,
# `YTDL_PYINSTALLER_DEBUG`)

datas = [('src/yt_dlp_gui/data/sample_config.toml', 'yt_dlp_gui/data')]
binaries = []
hiddenimports = []
datas += copy_metadata('yt_dlp_gui')
tmp_ret = collect_all('yt_dlp_gui')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

if sys.platform == 'darwin':
    platform = 'mac'
elif sys.platform.startswith('win'):
    platform = 'windows'
elif sys.platform.startswith('linux'):
    platform = 'linux'
else:
    raise ValueError(f'unrecognized platform {sys.platform}')

script_path = str(Path('scripts') / 'run.py')

# perform analysis

a = Analysis(
    [script_path],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

# build the exe

if platform == "windows":
  exec_params = [a.scripts, a.binaries, a.datas, [],]
  exec_kws = {
    'exclude_binaries': False,
    'upx': True,
    'upx_exclude': [],
    'runtime_tmpdir': None,
  }
else:
  exec_params = [a.scripts, []]
  exec_kws = {
    'exclude_binaries': True,
    'upx': False,
  }

exe = EXE(
    pyz,
    *exec_params,
    **exec_kws,
    name='yt-dlp-gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['src/yt_dlp_gui/ui/assets/yt-dlp-gui.ico'],
)

# on windows - stop now.
# on linux and mac - collect files needed for a "onedir" app

if platform != 'windows':

    coll = COLLECT(
        exe,
        a.binaries,
        a.datas,
        strip=False,
        upx=False,
        upx_exclude=[],
        name='yt-dlp-gui',
    )

# on mac only - build an app "bundle"

if platform == "mac":
    app = BUNDLE(
        coll,
        name='yt-dlp-gui.app',
        icon=None,
        bundle_identifier='com.github.phlummox-dev.yt-dlp-gui',
    )

# vim: syntax=python :
