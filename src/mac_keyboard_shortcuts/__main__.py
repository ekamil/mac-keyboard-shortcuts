"""Command-line interface."""

import os
import sys
from importlib.util import find_spec
from pathlib import Path

import click

from mac_keyboard_shortcuts.consts.apple import PLIST_PATH_S
from mac_keyboard_shortcuts.utils.authoring import download_key_definitions
from mac_keyboard_shortcuts.utils.plist import show_enabled_impl


@click.group()
@click.version_option()
def main() -> None:
    """Mac Keyboard Shortcuts.

    mac-keyboard-shortcuts print [FILE1]
    mac-keyboard-shortcuts diff FILE1 FILE2
    mac-keyboard-shortcuts write-using-py PYTHON_FILE
    mac-keyboard-shortcuts print-key-defs
    """


@main.command()
@click.option(
    "--print-code/--no-print-code", default=True, help="Print code or silent run"
)
def download_key_defs(print_code: bool) -> None:
    download_key_definitions(print_code=print_code)


@main.command()
@click.option("--plist-path", default=PLIST_PATH_S, help="Path to .plist file")
@click.option("--color/--no-color", default=False, help="Suppresses using colors")
@click.option(
    "--validate/--no-validate",
    default=False,
    help="Writes and validates the new data using plutil (tempfile)",
)
def show_enabled(plist_path: str, color: bool, validate: bool) -> None:
    """
    Prints a diff showing all enabled shortcuts. This serves also a sanity check, testing differ, updater and reader.
    The real Mac settings WILL NOT change, this is safe.
    """
    plist_path = os.path.expanduser(plist_path)
    if not Path(plist_path).exists():
        raise RuntimeError(f"{plist_path} couldn't be found")
    if color:
        if not find_spec("termcolor"):
            print(
                "Missing termcolor, install with extra: pip install mac-keyboard-shortcuts[color]",
                file=sys.stderr,
            )
    show_enabled_impl(plist_path=plist_path, no_color=color, validate=validate)


if __name__ == "__main__":
    main(prog_name="mac-keyboard-shortcuts")  # pragma: no cover
