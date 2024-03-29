from __future__ import annotations

from dataclasses import dataclass

from mac_keyboard_shortcuts.consts.actions import Actions
from mac_keyboard_shortcuts.consts.apple import NON_ASCII
from mac_keyboard_shortcuts.consts.apple import STANDARD
from mac_keyboard_shortcuts.consts.consts import MISSING
from mac_keyboard_shortcuts.consts.keys import Keys
from mac_keyboard_shortcuts.consts.modifiers import Modifiers
from mac_keyboard_shortcuts.types.apple import SymbolicHotKey
from mac_keyboard_shortcuts.types.key import Key


@dataclass
class HotKeyEntry:
    action: int
    key: Key
    modifiers: list[Modifiers]
    modifiers_value: int = 0
    enabled: bool = True
    type_: str = STANDARD
    managed: bool = True
    action_name: str = MISSING

    def as_item(self) -> tuple[str, SymbolicHotKey]:
        return str(self.action), {
            "enabled": self.enabled,
            "value": {
                "parameters": (
                    self.key.ascii_code,
                    self.key.mac_key_code,
                    sum(m.value for m in self.modifiers),
                ),
                "type": self.type_,
            },
        }

    def as_short_str(self) -> str:
        """
        Prints the entry in a compact, stable, columnar format.
        Should conform to KEY_SHORT_FORMAT_WIDTH
        """
        key_spec = "+".join([m.name for m in self.modifiers] + [self.key.label])
        return " ".join(
            (
                f"{self.action:3d}",
                " on" if self.enabled else "off",
                f"{key_spec:<30}",
                f"{self.modifiers_value:10d}",
                f"{self.action_name:<40}",
            )
        )

    @classmethod
    def parse(cls, action_number: str, entry_dict: SymbolicHotKey) -> HotKeyEntry:
        action = Actions.get_by_value(action_number)
        if action:
            action_value = action.value
            action_name = action.name
            managed = True
        else:
            action_value = int(action_number)
            action_name = MISSING
            managed = False
        value_ = entry_dict.get("value")
        if value_ is None:  # no key assigned - so probably it's also off
            return cls(
                action=action_value,
                action_name=action_name,
                key=Key.no_op(),
                modifiers=[],
                enabled=False,
                type_=STANDARD,
                managed=False,
            )
        modifiers_value = value_["parameters"][2]
        modifiers = Modifiers.find_constituent_flags(modifiers_value)
        ascii_code = value_["parameters"][0]
        mac_key_code = value_["parameters"][1]
        key_sequence = Keys.find_key_by_mac_key_code(mac_key_code)
        if not key_sequence:
            key_sequence = Key.unknown(ascii_code=ascii_code, mac_key_code=mac_key_code)
            if mac_key_code != NON_ASCII:
                print(f"Can't find key_sequence for {ascii_code=} and {mac_key_code=}")
        return cls(
            action=action_value,
            action_name=action_name,
            key=key_sequence,
            modifiers=modifiers,
            modifiers_value=modifiers_value,
            enabled=bool(entry_dict["enabled"]),
            type_=value_["type"],
            managed=managed,
        )
