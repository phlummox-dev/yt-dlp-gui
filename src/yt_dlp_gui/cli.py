"""
Main entrypoint
"""

import argparse
import sys

from .metadata import properties


def main():
    """
    main entrypoint. Can be called without loading GUI libraries, in order
    to e.g. get version information.
    """

    parser = argparse.ArgumentParser(description='yt-dlp YouTube downloader GUI')
    parser.add_argument('--version', action='store_true',
                        help='Print version info and exit'
    )

    args = parser.parse_args()

    if args.version:
        for field in properties._fields:
            field_str = field.replace('_', ' ').capitalize() + ":"
            print(f"{field_str:<12} {getattr(properties, field)}")
        sys.exit(0)

    # we don't load gui libraries unless actually necessary
    from .app import main as gui_main # pylint: disable=import-outside-toplevel
    gui_main()

if __name__ == "__main__":
    main()

