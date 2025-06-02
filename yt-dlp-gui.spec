# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
from PyInstaller.utils.hooks import copy_metadata

# created using
#
#cmd=pyinstaller; \
#	uv run $$cmd --onedir --name=yt-dlp-gui -y \
#			--icon ./src/yt_dlp_gui/ui/assets/yt-dlp-gui.ico \
#			--log-level DEBUG \
#			--collect-all yt_dlp_gui \
#			--copy-metadata yt_dlp_gui \
#			--add-data "src/yt_dlp_gui/data/sample_config.toml:yt_dlp_gui/data" \
#			--debug=all \
#			--noupx \
#			scripts/run.py
import sys

datas = [('src/yt_dlp_gui/data/sample_config.toml', 'yt_dlp_gui/data')]
binaries = []
hiddenimports = []
datas += copy_metadata('yt_dlp_gui')
tmp_ret = collect_all('yt_dlp_gui')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

print("DATAS are:", datas, file=sys.stderr)
print("tmp_ret are:", tmp_ret, file=sys.stderr)

# change to True to debug built executable
debug = True

a = Analysis(
    ['scripts/run.py'],
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

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='yt-dlp-gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['src/yt_dlp_gui/ui/assets/yt-dlp-gui.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='yt-dlp-gui',
)
