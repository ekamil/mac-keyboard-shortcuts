"""Command-line interface."""

import click

from mac_keyboard_shortcuts.utils.authoring import download_key_definitions


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
@click.option("--print-code", default=True, help="Print code or silent run")
def download_key_defs(print_code: bool) -> None:
    download_key_definitions(print_code=print_code)


if __name__ == "__main__":
    main(prog_name="mac-keyboard-shortcuts")  # pragma: no cover
