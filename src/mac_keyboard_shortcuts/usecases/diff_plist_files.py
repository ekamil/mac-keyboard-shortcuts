import plistlib as pl
from pathlib import Path

from mac_keyboard_shortcuts.consts.consts import KEY_SHORT_FORMAT_WIDTH
from mac_keyboard_shortcuts.utils.plist import diff_hotkeys_definitions
from mac_keyboard_shortcuts.utils.plist_reading import parse_plist_data


def diff_plists_file_impl(
    plist_path_old: Path,
    plist_path_new: Path,
    print_common_lines: bool = True,
    use_colours: bool = True,
) -> list[str]:
    """
    Compares and prints a diff of two .plist files, assuming they both contain Hotkeys definitions.
    """
    print(f"Comparing lists at {plist_path_old} -> {plist_path_old}")

    width: int = 2 * KEY_SHORT_FORMAT_WIDTH

    with open(plist_path_old, "rb") as fd:
        old_data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
        old_parsed = parse_plist_data(old_data)
    with open(plist_path_new, "rb") as fd:
        new_data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
        new_parsed = parse_plist_data(new_data)
    diff = diff_hotkeys_definitions(
        old_parsed,
        new_parsed,
        width,
        print_common_lines,
        use_colours,
    )
    return diff
