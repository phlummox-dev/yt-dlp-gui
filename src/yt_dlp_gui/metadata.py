"""
Expose app metadata in a developer-friendly way
"""

import importlib
from pathlib import Path
from typing import NamedTuple

package_dir = Path(__file__).parent.name
pkg = importlib.import_module(package_dir)

class Metadata(NamedTuple):
    "app metadata"

    app_name: str
    version: str
    commit: str
    build_time: str
    build_host: str
    ci_pipeline: str

properties = Metadata(
  app_name=pkg.__app_name__,
  version=pkg.__version__,
  commit=pkg.__commit__,
  build_time=pkg.__build_time__,
  build_host=pkg.__build_host__,
  ci_pipeline=pkg.__ci_pipeline__,
)

