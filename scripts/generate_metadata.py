#!/usr/bin/env python3

"""
generate an __init__.py file containing app metadata
"""

import datetime
import os
import subprocess

import toml


def safe_run(cmd):
    "shell out, but with a default return string"
    try:
        return subprocess.check_output(cmd).decode().strip()
    except Exception:
        return "(na)"

with open("pyproject.toml", "r", encoding="utf-8") as f:
    pyproject = toml.load(f)

init_path = os.path.join("src", "yt_dlp_gui", "__init__.py")

# pylint: disable=invalid-name

# metadata properties
app_name = pyproject.get("project", {}).get("name", "(na)")
version = pyproject.get("project", {}).get("version", "(na)")
commit = safe_run(['git', 'rev-parse', '--short', 'HEAD'])
build_time = f"{datetime.datetime.now(datetime.UTC).isoformat()}Z"

build_host = os.uname().nodename if hasattr(os, 'uname') \
                                 else os.getenv('COMPUTERNAME', '(na)')
ci_pipeline = os.getenv('CI_PIPELINE_NAME', '(na)')

init_conts = f"""
# NOTE: This file is overwritten by CI. Do not edit manually.
# For local development, metadata fields may be "(na)" or similar.

# pylint: disable=missing-module-docstring

__app_name__ = "{app_name}"
__version__ = "{version}"
__commit__ = "{commit}"
__build_time__ = "{build_time}"
__build_host__ = "{build_host}"
__ci_pipeline__ = "{ci_pipeline}"
"""

with open(init_path, "w", encoding="utf-8") as ofp:
    ofp.write(init_conts)
