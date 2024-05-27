from typing import Callable
from typing import Iterable

from mac_keyboard_shortcuts.types.entry import HotKeyEntry


HotKeyEntries = Iterable[HotKeyEntry]
HKMutator = Callable[[HotKeyEntries], HotKeyEntries]
