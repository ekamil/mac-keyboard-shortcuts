import dataclasses
from typing import Iterable

from mac_keyboard_shortcuts.types.entry import HotKeyEntry


def _turn_off_all_shortcuts(
    entries: Iterable[HotKeyEntry],
    only_managed: bool = True,
) -> Iterable[HotKeyEntry]:
    for value in entries:
        if (not only_managed) or value.managed:
            yield dataclasses.replace(value, enabled=False)
        else:
            yield dataclasses.replace(value)


def _print_current(
    entries: Iterable[HotKeyEntry], print_current: bool = False
) -> Iterable[HotKeyEntry]:
    if not print_current:
        yield from entries
    print("Current values:")
    for value in entries:
        if value.enabled:
            print(value.as_short_str())
        yield value
