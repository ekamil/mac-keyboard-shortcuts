"""Command-line interface."""

import os
from pathlib import Path

import click

from mac_keyboard_shortcuts.usecases.authoring import download_key_definitions
from mac_keyboard_shortcuts.usecases.diff_plist_files import diff_plists_file_impl
from mac_keyboard_shortcuts.usecases.mutate_using_python import mutate_impl
from mac_keyboard_shortcuts.usecases.print_enabled import print_enabled_impl
from mac_keyboard_shortcuts.usecases.print_plist_file import print_plist_file_impl

HOTKEY_PLIST_DEFAULT_PATH = os.path.expanduser(
    "~/Library/Preferences/com.apple.symbolichotkeys.plist"
)


@click.group()
@click.version_option()
@click.option("--debug", default=False, help="More logging")
@click.pass_context
def main(ctx: click.Context, debug: bool) -> None:
    """Mac Keyboard Shortcuts."""
    ctx.ensure_object(dict)
    ctx.obj["debug"] = debug


@main.command()
@click.argument(
    "plist-path",
    type=click.Path(exists=True),
    default=HOTKEY_PLIST_DEFAULT_PATH,
    nargs=1,
)
def print_plist(plist_path: str) -> None:
    """
    Prints hotkeys read from a PLIST_PATH
    """
    print_plist_file_impl(plist_path)


@main.command()
@click.argument(
    "plist-path-old",
    type=click.Path(exists=True),
    default=HOTKEY_PLIST_DEFAULT_PATH,
    nargs=1,
)
@click.argument(
    "plist-path-new",
    type=click.Path(exists=True),
    nargs=1,
)
@click.option(
    "--print-common-lines/--no-print-common-lines",
    default=False,
    help="Prints lines that don't differ",
)
@click.pass_context
def diff_plists(
    ctx: click.Context,
    plist_path_old: str,
    plist_path_new: str,
    print_common_lines: bool,
) -> None:
    """
    Diffs two hotkey files, PLIST-PATH-OLD (left) with PLIST-PATH-NEW
    """
    for d in diff_plists_file_impl(
        Path(plist_path_old),
        Path(plist_path_new),
        print_common_lines=print_common_lines,
    ):
        click.echo(d)


@main.command()
@click.argument(
    "python-file",
    type=click.Path(exists=True, readable=True),
)
@click.argument(
    "plist-path",
    type=click.Path(exists=True, readable=True),
    default=HOTKEY_PLIST_DEFAULT_PATH,
)
@click.option("--dry-run", default=False, is_flag=True, help="Only prints a diff")
@click.option(
    "--validate/--no-validate",
    default=True,
    help="Validates the result with `plutil` before writing",
)
@click.pass_context
def mutate(
    ctx: click.Context,
    python_file: str,
    plist_path: str,
    dry_run: bool,
    validate: bool,
) -> None:
    """
    Mutates PLIST_PATH using the `main` function from PYTHON_FILE
    """
    mutate_impl(
        python_file=Path(python_file),
        plist_path=Path(plist_path),
        dry_run=dry_run,
        validate=validate,
    )


@main.command()
@click.argument(
    "plist-path",
    type=click.Path(exists=True),
    default=HOTKEY_PLIST_DEFAULT_PATH,
)
@click.option(
    "--validate/--no-validate",
    default=False,
    help="Writes and validates the new data using plutil (tempfile)",
)
@click.option(
    "--diff/--no-diff",
    default=True,
    help="Prints in the form a diff",
)
@click.pass_context
def print_enabled(
    ctx: click.Context, plist_path: str, validate: bool, diff: bool
) -> None:
    """
    Prints a diff showing all enabled shortcuts. This serves also a sanity check, testing differ, updater and reader.
    The real Mac settings WILL NOT change, this is safe.

    plist-path is the path to plist file defining current hotkeys.
    """
    _plist_path = Path(plist_path)
    if not _plist_path.exists():
        raise RuntimeError(f"{plist_path} couldn't be found")
    for d in print_enabled_impl(
        plist_path=_plist_path, validate=validate, do_diff=diff
    ):
        click.echo(d)


@main.command()
@click.option(
    "--print-code/--no-print-code", default=True, help="Print code or silent run"
)
def download_key_defs(print_code: bool) -> None:
    """
    Downloads and prints code definition from a [gist by jimratliff]
    [gist by jimratliff]: https://gist.github.com/jimratliff/227088cc936065598bedfd91c360334e
    """
    download_key_definitions(print_code=print_code)


if __name__ == "__main__":
    main(prog_name="mac-keyboard-shortcuts", obj={})  # pragma: no cover
