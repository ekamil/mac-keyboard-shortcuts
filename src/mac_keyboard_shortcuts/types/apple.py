from typing import TypedDict, Optional

"""
Describes the model of a single key-shortcut entry, i.e. the part after "7":

{
  "AppleSymbolicHotKeys" => {
    "7" => {
      "enabled" => 0
      "value" => {
        "parameters" => [
          0 => 65535
          1 => 120
          2 => 8650752
        ]
        "type" => "standard"
      }
    }
"""


class Value(TypedDict):
    parameters: tuple[int, int, int]
    type: str


class SymbolicHotKey(TypedDict):
    enabled: bool
    value: Optional[Value]


SymbolicHotKeys = dict[str, SymbolicHotKey]


class SymbolicHotKeysPlist(TypedDict):
    AppleSymbolicHotKeys: dict[str, SymbolicHotKey]
