"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Mac Keyboard Shortcuts.

    mac-keyboard-shortcuts print [FILE1]
    mac-keyboard-shortcuts diff FILE1 FILE2
    mac-keyboard-shortcuts write-using-py PYTHON_FILE
    """


if __name__ == "__main__":
    main(prog_name="mac-keyboard-shortcuts")  # pragma: no cover
