import contextlib
import plistlib as pl
import shutil as sh
import subprocess  # noqa: S404
from pathlib import Path
from typing import Any
from typing import Generator
from typing import Optional

from mac_keyboard_shortcuts.types.aliases import HotKeyEntries
from mac_keyboard_shortcuts.types.apple import SymbolicHotKeysPlist
from mac_keyboard_shortcuts.utils.plist import diff_hotkeys_definitions
from mac_keyboard_shortcuts.utils.plist_reading import parse_plist_data


def format_for_writing(
    parsed_entries: HotKeyEntries,
    mutable_data: Optional[SymbolicHotKeysPlist] = None,
) -> SymbolicHotKeysPlist:
    result = mutable_data if mutable_data is not None else {"AppleSymbolicHotKeys": {}}
    result["AppleSymbolicHotKeys"] = dict(se.as_item() for se in parsed_entries)
    return result


@contextlib.contextmanager
def plist_writer(
    path: str,
    *,
    backup: bool = True,
    replace: bool = False,
    validate: bool = False,
    print_diff: bool = False,
) -> Generator[dict[str, Any], None, None]:
    """
    Context manager to open, read, validate and write a .plist file.
    Yields a dictionary representing the data inside plist file. Mutate this dict to update settings.
    By default, this function won't actually update the file, but create a new one next to it with suffix .new.
    This new file will be validated with `plutil` system command.
    You can change this behaviour using `replace` flag.

    Args:
      path (str): Filesystem path to the file
      backup (bool): Backup the file before reading to a new one with suffix .bak
      replace (bool): Actually replace the file with possibly updated data
      validate (bool): Set to False if you don't want to run `plutil`
      print_diff (bool): Compare before replacing
    Raises:
      RuntimeError: When the new/modified content fails validation
    Yields:
      dictionary representation of the plist

    """
    if not Path(path).exists():
        raise RuntimeError(f"{path} couldn't be found")
    if backup:
        sh.copy(path, path + ".bak")
    with open(path, "rb") as fd:
        # data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=OrderedDict)
        if print_diff:
            data_for_diff = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
        data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
    yield data
    new_file = path + ".new"
    with open(new_file, "wb") as fd:
        # write and move patter to ensure that we can dump the data
        pl.dump(data, fd, fmt=pl.FMT_BINARY, sort_keys=True, skipkeys=False)
    if print_diff:
        diff_hotkeys_definitions(
            old=parse_plist_data(data_for_diff), new=parse_plist_data(data)
        )
    if validate:
        exit_code = subprocess.call(["plutil", new_file])  # noqa: S603,S607
        if exit_code != 0:
            raise RuntimeError(
                f"plutil couldn't validate the new file - aborting (path: {new_file}"
            )
    if replace:
        sh.move(new_file, path)
