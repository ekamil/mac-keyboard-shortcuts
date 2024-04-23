from typing import Optional
from typing import TypedDict


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


SymbolicHotKeyAction = str
SymbolicHotKeys = dict[SymbolicHotKeyAction, SymbolicHotKey]


class SymbolicHotKeysPlist(TypedDict):
    AppleSymbolicHotKeys: SymbolicHotKeyAction
