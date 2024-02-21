import csv
from enum import Enum
from io import StringIO
from typing import Type

import requests

from mac_keyboard_shortcuts.types.key import Key


def download_key_definitions(print_code=True) -> Type[Enum]:
    """
    Get the TSV from https://gist.github.com/jimratliff/227088cc936065598bedfd91c360334e
    and load this as key definitions.
    There's a static version in this file, which I generate using this funcion.
    """
    url = "https://gist.githubusercontent.com/jimratliff/227088cc936065598bedfd91c360334e/raw/2763d56ac84e77b5f4af07f82d55feff037227f3/Mac_keyboard_ASCII_and_virtual_keys.tsv"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("Can't get the key definitions TSV - use offline version")
    # Use StringIO to create a file-like object from the response content
    content = StringIO(response.text)
    reader = csv.reader(content, delimiter="\t")  # Specify the tab delimiter
    # Skip the header if needed
    header = next(reader)
    # Read the rest of the rows
    attributes = {}
    _properties = []
    for row in reader:
        property_value = Key(
            label=row[0].strip(),
            character=row[1],
            ascii_code=int(row[2]),
            mac_key_code=int(row[3]),
            layout_dependence=row[4],
        )
        property_name = f"KEY_{row[0].strip().upper()}"
        attributes[property_name] = property_value
        _properties.append(property_name)
    if len(_properties) != len(attributes):
        raise ValueError("Some attributes were missed - debug me!")
    if len(set([k.mac_key_code for k in attributes.values()])) != len(attributes):
        raise ValueError("Duplicate Mac key codes - debug me!")
    new_enumeration = Enum("Keys", attributes)
    if print_code:
        print("class Keys(Key, Enum):")
        print("    # fmt: off")
        for name, value in attributes.items():
            print(f"    {name} = {value}")
        print("    # fmt: on")
    return new_enumeration
