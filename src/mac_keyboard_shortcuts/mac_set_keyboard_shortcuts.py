#!/usr/bin/env python
import os.path
from operator import attrgetter
from typing import Iterable

from mac_keyboard_shortcuts.api import APPLE_SYMBOLIC_HOT_KEYS, PLIST_PATH_S
from mac_keyboard_shortcuts.api import Actions
from mac_keyboard_shortcuts.api import HotKeyEntry
from mac_keyboard_shortcuts.api import Keys
from mac_keyboard_shortcuts.api import Modifiers
from mac_keyboard_shortcuts.api import plist_writer
from mac_keyboard_shortcuts.types.apple import SymbolicHotKeys

PLIST_PATH = os.path.expanduser(PLIST_PATH_S)


def my_config_or_passthrough(
    *,
    print_current: bool = False,
    backup: bool = True,
    replace: bool = False,
) -> None:
    """
    Turns off everything that's unknown (per actions enum) and
    then sets my shortcuts.
    """
    with plist_writer(path=PLIST_PATH, backup=backup, replace=replace) as plist_data:
        entries: SymbolicHotKeys = plist_data[APPLE_SYMBOLIC_HOT_KEYS]
        parsed: Iterable[HotKeyEntry]
        parsed = sorted(
            [HotKeyEntry.parse(key, value) for key, value in entries.items()],
            key=attrgetter("action"),
        )
        # ####
        # TODO: this section here could be with run using py?
        # ####
        # Print current state
        parsed = _print_current(parsed, print_current)
        # First pass - turn off everything
        parsed = _turn_off_all_shortcuts(parsed)
        # Second pass
        parsed = set_my_shortcuts(parsed)

        # Override the original dict
        plist_data[APPLE_SYMBOLIC_HOT_KEYS] = dict(se.as_item() for se in parsed)


def _turn_off_all_shortcuts(
    entries: Iterable[HotKeyEntry],
) -> Iterable[HotKeyEntry]:
    for value in entries:
        if value.managed:
            value.enabled = False
        yield value


def _print_current(
    entries: Iterable[HotKeyEntry], print_current: bool = False
) -> Iterable[HotKeyEntry]:
    if not print_current:
        return entries
    print("Current values:")
    for value in entries:
        if value.enabled:
            print(value.as_short_str())
        yield value


def set_my_shortcuts(
    entries: Iterable[HotKeyEntry], *, alfred: bool = True, contexts: bool = True
) -> Iterable[HotKeyEntry]:
    yield HotKeyEntry(
        action=Actions.kCGSHotKeyFocusApplicationWindow.value,
        key=Keys.KEY_GRAVE,
        modifiers=(
            [Modifiers.command, Modifiers.option] if contexts else [Modifiers.command]
        ),
    )
    yield HotKeyEntry(
        action=Actions.kCGSHotKeyScreenshot.value,
        key=Keys.KEY_3,
        modifiers=[Modifiers.command, Modifiers.shift],
    )
    yield HotKeyEntry(
        action=Actions.kCGSHotKeyScreenshotRegion.value,
        key=Keys.KEY_4,
        modifiers=[Modifiers.command, Modifiers.shift],
    )
    yield HotKeyEntry(
        action=Actions.screenshot_and_recording_options.value,
        key=Keys.KEY_5,
        modifiers=[Modifiers.shift, Modifiers.command],
    )
    yield HotKeyEntry(
        action=Actions.kCGSHotKeyExposeDesktopsSlow.value,
        key=Keys.KEY_D,
        modifiers=[Modifiers.shift, Modifiers.command],
        enabled=False,
    )
    yield HotKeyEntry(
        action=Actions.kCGSHotKeyExposeAllWindows.value,
        key=Keys.KEY_F10,
        modifiers=[Modifiers.function],
    )
    yield HotKeyEntry(
        action=Actions.kCGSHotKeyExposeAllWindowsSlow.value,
        key=Keys.KEY_F10,
        modifiers=[Modifiers.shift, Modifiers.function],
    )
    yield HotKeyEntry(
        action=Actions.kCGSHotKeySpaceLeft.value,
        key=Keys.KEY_LEFTARROW,
        modifiers=[Modifiers.control],
    )
    # not sure what this "Slow" means here
    yield HotKeyEntry(
        action=Actions.kCGSHotKeySpaceLeftSlow.value,
        key=Keys.KEY_LEFTARROW,
        modifiers=[Modifiers.control, Modifiers.option],
    )
    yield HotKeyEntry(
        action=Actions.kCGSHotKeySpaceRight.value,
        key=Keys.KEY_RIGHTARROW,
        modifiers=[Modifiers.control],
    )
    yield HotKeyEntry(
        action=Actions.kCGSHotKeySpaceRightSlow.value,
        key=Keys.KEY_RIGHTARROW,
        modifiers=[Modifiers.control, Modifiers.option],
    )
    yield HotKeyEntry(
        action=Actions.kCGSHotKeySpotlightSearchField.value,
        key=Keys.KEY_SPACE,
        modifiers=[Modifiers.command],
        enabled=not alfred,  # Change if not using alfred
    )
