import plistlib as pl
import subprocess  # noqa: S404
import tempfile
from pathlib import Path
from typing import Generator

from mac_keyboard_shortcuts.entries_mutators import turn_off_all_shortcuts
from mac_keyboard_shortcuts.utils.plist import diff_hotkeys_definitions
from mac_keyboard_shortcuts.utils.plist_reading import parse_plist_data


def print_enabled_impl(
    plist_path: Path,
    no_color: bool = False,
    validate: bool = True,
) -> Generator[list[str], None, None]:
    """
    Yields a diff just before validation.
    Args:
        plist_path: Path to plist file
        no_color: suppress printing color codes
        validate: run plutil on the file

    Returns: generator with a diff (list[str])

    """
    with open(plist_path, "rb") as fd:
        data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
    old = parse_plist_data(data)
    new = turn_off_all_shortcuts(old)

    diff = diff_hotkeys_definitions(
        list(new),
        list(old),
        use_colours=not no_color,
        print_common_lines=False,
    )
    yield diff
    if validate:
        with tempfile.NamedTemporaryFile(mode="wb") as tmp:
            pl.dump(data, tmp, fmt=pl.FMT_BINARY, sort_keys=True, skipkeys=False)
            tmp.flush()
            exit_code = subprocess.call(["plutil", tmp.name])  # noqa: S603,S607
            if exit_code != 0:
                raise RuntimeError(
                    "plutil couldn't validate the new data. Please don't use it on real config files!"
                )
