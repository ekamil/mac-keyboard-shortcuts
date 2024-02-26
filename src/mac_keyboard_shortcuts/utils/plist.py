from mac_keyboard_shortcuts.consts.consts import KEY_SHORT_FORMAT_WIDTH
from mac_keyboard_shortcuts.types.aliases import HotKeyEntries
from mac_keyboard_shortcuts.utils.diff_side_by_side import better_diff


def diff_hotkeys_definitions(
    old: HotKeyEntries,
    new: HotKeyEntries,
    width: int = 2 * KEY_SHORT_FORMAT_WIDTH,
    print_common_lines: bool = True,
    use_colours: bool = True,
) -> list[str]:
    def normalized_list(data: HotKeyEntries) -> list[str]:
        return list(map(lambda e: e.as_short_str(), data))

    old_parsed = normalized_list(old)
    new_parsed = normalized_list(new)

    if old_parsed == new_parsed:
        return ["plists are identical"]

    diff = better_diff(
        left_title="Left",
        left=old_parsed,
        right_title="Right",
        right=new_parsed,
        width=width,
        print_common_lines=print_common_lines,
        use_colours=use_colours,
    )
    return diff
