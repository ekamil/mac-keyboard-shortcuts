import dataclasses

from mac_keyboard_shortcuts.types.aliases import HotKeyEntries


def turn_off_all_shortcuts(
    entries: HotKeyEntries,
    only_managed: bool = True,
    verbose: bool = False,
) -> HotKeyEntries:
    """
    Produces hotkeys which are all off.
    Args:
        entries: A list of entries to mutate
        only_managed: Only mutate hotkeys whose Action is known
        verbose: Print ignored entries
    Returns: Generates possibly changed entries

    """
    new_entries = []
    for value in entries:
        if (not only_managed) or value.managed:
            if verbose:
                print("Disabling ", value.as_short_str())
            new_entries.append(dataclasses.replace(value, enabled=False))
        else:
            if verbose:
                print("Ignoring ", value.as_short_str())
            new_entries.append(dataclasses.replace(value))
    return new_entries


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
    return entries
