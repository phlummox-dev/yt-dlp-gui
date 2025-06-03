#!/usr/bin/env python3

"""
Just an entrypoint into the app, used by pyinstaller

Handles any CLI options like `--version` first, before
attempting to load GUI shared libraries.
"""

from yt_dlp_gui import cli

cli.main()
