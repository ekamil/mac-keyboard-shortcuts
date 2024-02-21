from dataclasses import dataclass
from typing import Self

from mac_keyboard_shortcuts.consts.actions import Actions
from mac_keyboard_shortcuts.consts.apple import *
from mac_keyboard_shortcuts.consts.consts import MISSING
from mac_keyboard_shortcuts.consts.keys import KeysEnum
from mac_keyboard_shortcuts.consts.modifiers import Modifiers
from mac_keyboard_shortcuts.types.key import Key


@dataclass
class ShortcutEntry:
    action: int
    key: Key
    modifiers: list[Modifiers]
    modifiers_value: int = 0
    enabled: bool = True
    type_: str = STANDARD
    managed: bool = True
    action_name: str = MISSING

    def as_item(self) -> tuple[str, dict]:
        return str(self.action), {
            "enabled": self.enabled,
            VALUE: {
                PARAMETERS: [
                    self.key.ascii_code,
                    self.key.mac_key_code,
                    sum((m.value for m in self.modifiers)),
                ],
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
                "{0:3d}".format(self.action),
                " on" if self.enabled else "off",
                "{:<50}".format(key_spec),
                "{0:10d}".format(self.modifiers_value),
                "{:<40}".format(self.action_name),
            )
        )

    @classmethod
    def parse(cls, action_number: str, entry_dict: dict) -> Self:
        managed = True
        action = Actions.get_by_value(action_number)
        if action:
            action_value = action.value
            action_name = action.name
        else:
            action_value = int(action_number)
            action_name = MISSING
            managed = False
        if VALUE not in entry_dict:  # no key assigned - so probably it's also off
            return cls(
                action=action_value,
                action_name=action_name,
                key=Key.no_op(),
                modifiers=[],
                enabled=False,
                type_=STANDARD,
                managed=False,
            )
        modifiers_value = entry_dict[VALUE][PARAMETERS][2]
        modifiers = Modifiers.find_constituent_flags(modifiers_value)
        ascii_code = entry_dict[VALUE][PARAMETERS][0]
        mac_key_code = entry_dict[VALUE][PARAMETERS][1]
        key_sequence = KeysEnum.find_key_by_mac_key_code(mac_key_code)
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
            type_=entry_dict[VALUE]["type"],
            managed=managed,
        )
