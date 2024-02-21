from typing import Iterable
from typing import Optional

from mac_keyboard_shortcuts.types.apple import SymbolicHotKeysPlist
from mac_keyboard_shortcuts.types.entry import HotKeyEntry


def format_for_writing(
    parsed_entries: Iterable[HotKeyEntry],
    mutable_data: Optional[SymbolicHotKeysPlist] = None,
) -> SymbolicHotKeysPlist:
    result = mutable_data if mutable_data is not None else {"AppleSymbolicHotKeys": {}}
    result["AppleSymbolicHotKeys"] = dict(se.as_item() for se in parsed_entries)
    return result
