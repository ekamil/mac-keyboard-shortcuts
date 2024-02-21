#!/usr/bin/env python
import os.path

from mac_keyboard_shortcuts.api import APPLE_SYMBOLIC_HOT_KEYS, PLIST_PATH_S
from mac_keyboard_shortcuts.api import Actions
from mac_keyboard_shortcuts.api import KeysEnum
from mac_keyboard_shortcuts.api import Modifiers
from mac_keyboard_shortcuts.api import ShortcutEntry
from mac_keyboard_shortcuts.api import plist_writer
from mac_keyboard_shortcuts.utils.helpers import same

PLIST_PATH = os.path.expanduser(PLIST_PATH_S)


def my_config_or_passthrough(*, print_current=False, backup=True, replace=False):
    """
    Turns off everything that's unknown (per actions enum) and
    then sets my shortcuts.
    """
    with plist_writer(path=PLIST_PATH, backup=backup, replace=replace) as plist_data:
        entries = plist_data[APPLE_SYMBOLIC_HOT_KEYS]
        parsed = [ShortcutEntry.parse(key, value) for key, value in entries.items()]
        parsed = sorted(parsed, key=lambda se: se.action)
        new_entries = {se.action: se for se in parsed}

        # TODO: this section here could be with run using py?

        # Print current state
        if print_current:
            _print_current(new_entries)
        # First pass - turn off everything
        _turn_off_all_shortcuts(new_entries)
        # Second pass
        set_my_shortcuts(new_entries)

        # Override the original dict
        plist_data[APPLE_SYMBOLIC_HOT_KEYS] = dict(
            se.as_item() for se in new_entries.values()
        )


def _turn_off_all_shortcuts(new_entries):
    for value in new_entries.values():
        if value.managed:
            value.enabled = False


def _print_current(new_entries):
    print("Current values:")
    for value in new_entries.values():
        if value.enabled:
            print(value.as_short_str())


def set_my_shortcuts(new_entries: dict, *, alfred=True, contexts=True) -> None:
    with same(Actions.kCGSHotKeyFocusApplicationWindow) as k:
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_GRAVE.value,
            modifiers=(
                [Modifiers.command, Modifiers.option]
                if contexts
                else [Modifiers.command]
            ),
        )
    with same(Actions.kCGSHotKeyScreenshot) as k:
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_3.value,
            modifiers=[Modifiers.command, Modifiers.shift],
        )
    with same(Actions.kCGSHotKeyScreenshotRegion) as k:
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_4.value,
            modifiers=[Modifiers.command, Modifiers.shift],
        )
    with same(Actions.screenshot_and_recording_options) as k:
        # not sure what this is
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_5.value,
            modifiers=[Modifiers.shift, Modifiers.command],
        )
    with same(Actions.kCGSHotKeyExposeDesktopsSlow) as k:
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_D.value,
            modifiers=[Modifiers.shift, Modifiers.command],
            enabled=False,
        )
    with same(Actions.kCGSHotKeyExposeAllWindows) as k:
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_F10.value,
            modifiers=[Modifiers.function],
        )
    with same(Actions.kCGSHotKeyExposeAllWindowsSlow) as k:
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_F10.value,
            modifiers=[Modifiers.shift, Modifiers.function],
        )
    with same(Actions.kCGSHotKeySpaceLeft) as k:
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_LEFTARROW.value,
            modifiers=[Modifiers.control],
        )
    with same(Actions.kCGSHotKeySpaceLeftSlow) as k:
        # not sure what this is
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_LEFTARROW.value,
            modifiers=[Modifiers.control, Modifiers.option],
        )
    with same(Actions.kCGSHotKeySpaceRight) as k:
        # not sure what this is
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_RIGHTARROW.value,
            modifiers=[Modifiers.control],
        )
    with same(Actions.kCGSHotKeySpaceRightSlow) as k:
        # not sure what this is
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_RIGHTARROW.value,
            modifiers=[Modifiers.control, Modifiers.option],
        )
    with same(Actions.kCGSHotKeySpotlightSearchField) as k:
        # not sure what this is
        new_entries[k.value] = ShortcutEntry(
            action=k.value,
            key=KeysEnum.KEY_SPACE.value,
            modifiers=[Modifiers.command],
            enabled=not alfred,  # Change if not using alfred
        )
