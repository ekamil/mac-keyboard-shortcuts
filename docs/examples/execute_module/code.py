import dataclasses
from typing import Iterable

from mac_keyboard_shortcuts.api import Actions
from mac_keyboard_shortcuts.api import HotKeyEntry


def main(entries: Iterable[HotKeyEntry]) -> Iterable[HotKeyEntry]:
    for entry in entries:
        if entry.action_name == Actions.kCGSHotKeyFocusApplicationWindow.name:
            print(entry.as_short_str())
            yield dataclasses.replace(entry, enabled=False)
        else:
            yield entry
