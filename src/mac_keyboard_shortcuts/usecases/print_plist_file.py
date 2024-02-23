import plistlib as pl

from mac_keyboard_shortcuts.utils.plist_reading import parse_plist_data


def print_plist_file_impl(plist_path: str) -> None:
    with open(plist_path, "rb") as fd:
        data = pl.load(fd, fmt=pl.FMT_BINARY, dict_type=dict)
    data = parse_plist_data(data)
    for i in map(lambda e: e.as_short_str(), data):
        print(i)
