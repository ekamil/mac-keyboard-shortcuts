#!/usr/bin/env python
import os.path
import subprocess
from typing import Iterable, Generator

from mac_keyboard_shortcuts.api import Actions
from mac_keyboard_shortcuts.api import HotKeyEntry
from mac_keyboard_shortcuts.api import Keys
from mac_keyboard_shortcuts.api import Modifiers
from mac_keyboard_shortcuts.entries_mutators import print_currently_enabled
from mac_keyboard_shortcuts.entries_mutators import turn_off_all_shortcuts
from mac_keyboard_shortcuts.utils.plist_reading import parse_plist_data
from mac_keyboard_shortcuts.utils.plist_writing import format_for_writing
from mac_keyboard_shortcuts.utils.plist_writing import plist_writer


PLIST_PATH = os.path.expanduser("~/Library/Preferences/com.apple.symbolichotkeys.plist")


def main(
    *,
    print_current: bool = False,
    backup: bool = True,
    replace: bool = False,
    validate: bool = True,
    print_diff: bool = True,
    alfred: bool = True,
    contexts: bool = True
) -> None:
    """
    Turns off everything whose function I don't know (per the Actions enum) and
    then sets only my shortcuts.
    """
    with plist_writer(
        path=PLIST_PATH,
        backup=backup,
        replace=replace,
        validate=validate,
        print_diff=print_diff,
    ) as raw_plist_data:
        parsed = parse_plist_data(raw_plist_data)  # type:ignore[arg-type]
        # Print current state
        if print_current:
            parsed = print_currently_enabled(parsed)
        # First pass - turn off everything
        parsed = turn_off_all_shortcuts(
            parsed, only_managed=False, verbose=print_current
        )
        # Second pass
        parsed = list(set_my_shortcuts(parsed, alfred=alfred, contexts=contexts))
        # Override the original dict
        format_for_writing(
            parsed,
            raw_plist_data,  # type:ignore[arg-type]
        )


def set_my_shortcuts(
    entries: Iterable[HotKeyEntry], *, alfred: bool = True, contexts: bool = True
) -> Generator[HotKeyEntry, None, None]:
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
        enabled=not alfred,  # either Alfred or Spotlight
        # other option would be to run one of them with a different hotkey
    )


if __name__ == "__main__":
    subprocess.run(["osascript", "-e", 'tell application "System Preferences" to quit'])
    main(
        print_current=False,
        backup=True,
        replace=True,
        validate=True,
        print_diff=True,
        alfred=False,
        contexts=False,
    )
