import dataclasses

from mac_keyboard_shortcuts.types.aliases import HotKeyEntries


def turn_off_all_shortcuts(
    entries: HotKeyEntries,
    only_managed: bool = True,
) -> HotKeyEntries:
    """
    Produces hotkeys which are all off.
    Args:
        entries: A list of entries to mutate
        only_managed: Only mutate hotkeys whose Action is known

    Returns: Generates possibly changed entries

    """
    for value in entries:
        if (not only_managed) or value.managed:
            yield dataclasses.replace(value, enabled=False)
        else:
            yield dataclasses.replace(value)


def print_currently_enabled(entries: HotKeyEntries) -> HotKeyEntries:
    """
    Iterates and prints the entries as a short text.
    Args:
        entries:

    Returns: entries

    """
    print("Current values:")
    for value in entries:
        if value.enabled:
            print(value.as_short_str())
        yield value
