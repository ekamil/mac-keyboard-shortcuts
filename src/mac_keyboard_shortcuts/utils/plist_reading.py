import plistlib as pl
from operator import attrgetter
from pathlib import Path
from pprint import pprint
from typing import Iterable
from typing import Union

from mac_keyboard_shortcuts.types.apple import SymbolicHotKeys
from mac_keyboard_shortcuts.types.apple import SymbolicHotKeysPlist
from mac_keyboard_shortcuts.types.entry import HotKeyEntry


def print_plist(path: Union[str, Path]) -> None:
    with open(path, "rb") as fd:
        data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
    pprint(data)


def parse_plist_data(plist_data: SymbolicHotKeysPlist) -> Iterable[HotKeyEntry]:
    entries: SymbolicHotKeys = plist_data["AppleSymbolicHotKeys"]
    parsed: Iterable[HotKeyEntry]
    parsed = sorted(
        [HotKeyEntry.parse(key, value) for key, value in entries.items()],
        key=attrgetter("action"),
    )
    return parsed
