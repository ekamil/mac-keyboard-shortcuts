from __future__ import annotations

from dataclasses import dataclass

from mac_keyboard_shortcuts.consts.apple import NON_ASCII


@dataclass(frozen=True)
class Key:
    label: str
    character: str | None
    ascii_code: int
    mac_key_code: int
    layout_dependence: str

    @classmethod
    def no_op(cls) -> Key:
        return Key(
            label="Missing",
            character="-",
            ascii_code=NON_ASCII,
            mac_key_code=NON_ASCII,
            layout_dependence="Missing",
        )

    @classmethod
    def unknown(cls, *, ascii_code: int, mac_key_code: int) -> Key:
        if mac_key_code == NON_ASCII:
            return cls.no_op()
        return Key(
            label=f"Unknown {mac_key_code}",
            character="-",
            ascii_code=ascii_code,
            mac_key_code=mac_key_code,
            layout_dependence="Unknown",
        )
