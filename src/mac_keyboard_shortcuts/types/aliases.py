from typing import Iterable, Callable

from mac_keyboard_shortcuts.types.entry import HotKeyEntry

HotKeyEntries = Iterable[HotKeyEntry]
HKMutator = Callable[[HotKeyEntries], HotKeyEntries]
