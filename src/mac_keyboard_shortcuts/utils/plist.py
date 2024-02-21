import contextlib
import plistlib as pl
import shutil as sh
import subprocess
from pathlib import Path
from pprint import pprint
from typing import Union, Generator, Any

from mac_keyboard_shortcuts.consts.apple import APPLE_SYMBOLIC_HOT_KEYS
from mac_keyboard_shortcuts.consts.consts import KEY_SHORT_FORMAT_WIDTH
from mac_keyboard_shortcuts.types.apple import SymbolicHotKeys
from mac_keyboard_shortcuts.types.entry import HotKeyEntry
from mac_keyboard_shortcuts.utils.diff_side_by_side import better_diff


def print_plist(path: Union[str, Path]) -> None:
    with open(path, "rb") as fd:
        data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
    pprint(data)


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
        path (str | Path): Filesystem path to the file
        backup (bool): Backup the file before reading to a new one with suffix .bak
        replace (bool): Actually replace the file with possibly updated data
        validate (bool): Set to False if you don't want to run `plutil`
        print_diff (bool): Compare before replacing

    """
    if backup:
        sh.copy(path, path + ".bak")
    with open(path, "rb") as fd:
        # data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=OrderedDict)
        data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
    yield data
    new_file = path + ".new"
    with open(new_file, "wb") as fd:
        # write and move patter to ensure that we can dump the data
        pl.dump(data, fd, fmt=pl.FMT_BINARY, sort_keys=True, skipkeys=False)
    if print_diff:
        diff_hotkeys_plists(old=path, new=new_file)
    if validate:
        exit_code = subprocess.call(["plutil", new_file])
        if exit_code != 0:
            raise RuntimeError(
                f"plutil couldn't validate the new file - aborting (path: {new_file}"
            )
    if replace:
        sh.move(new_file, path)


def diff_hotkeys_plists(
    old: Union[Path, str],
    new: Union[Path, str],
    width: int = 2 * KEY_SHORT_FORMAT_WIDTH,
    print_common_lines: bool = True,
    use_colours: bool = True,
) -> None:
    """
    Compares and prints a diff of two .plist files, assuming they both contain Hotkeys definitions.
    """
    print(f"Comparing lists at {old} -> {new}")

    def normalized_list(data: SymbolicHotKeys) -> list[str]:
        _data = [HotKeyEntry.parse(k, v) for k, v in data.items()]
        _data.sort(key=lambda e: e.action)
        return list(map(lambda e: e.as_short_str(), _data))

    with open(old, "rb") as fd:
        old_data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
        old_parsed = normalized_list(old_data[APPLE_SYMBOLIC_HOT_KEYS])
    with open(new, "rb") as fd:
        new_data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
        new_parsed = normalized_list(new_data[APPLE_SYMBOLIC_HOT_KEYS])
    if old_parsed == new_parsed:
        print("plists are identical")
        return

    diff = better_diff(
        left_title=str(old),
        left=old_parsed,
        right_title=str(new),
        right=new_parsed,
        width=width,
        print_common_lines=print_common_lines,
        use_colours=use_colours,
    )
    for d in diff:
        print(d)
