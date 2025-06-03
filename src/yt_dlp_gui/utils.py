"""
Manage the config file
"""

# TODO: rename module. "utils" is a silly name

# pylint: disable=missing-function-docstring

import importlib.resources
import logging
from pathlib import Path

import toml
from platformdirs import user_config_dir

from .metadata import properties

logger = logging.getLogger(__name__)

app_name = properties.app_name

config_dir = Path(user_config_dir(app_name, None))
config_file_path = config_dir / "config.toml"

# data file, packaged with our app
sample_config_path = importlib.resources.files("yt_dlp_gui.data") \
                              .joinpath("sample_config.toml")

def create_config_if_needed():
    config_dir.mkdir(parents=True, exist_ok=True)
    if not config_file_path.exists():
        with sample_config_path.open("r") as f:
            sample_toml_conts = f.read()
        config_file_path.write_text(sample_toml_conts, encoding="utf-8")
        logger.info("Created new config file at: %s", config_file_path)
    assert config_file_path.exists(), f"config file {config_file_path} wasn't created"

def load_toml():
    logger.info("loading config file from %s", config_file_path)
    # ruff: noqa: UP015
    # mode args are just fine, thanks
    with open(config_file_path, "r", encoding="utf-8") as file:
        data = toml.load(file)
    return data


def save_toml(data: dict):
    logger.debug("saving config to '%s'", config_file_path)
    with open(config_file_path, "w", encoding="utf-8") as file:
        toml.dump(data, file)
