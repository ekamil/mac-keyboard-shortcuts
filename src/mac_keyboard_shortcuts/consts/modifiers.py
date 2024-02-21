from __future__ import annotations

from enum import IntEnum


class Modifiers(IntEnum):
    """
    Source 1: https://developer.apple.com/documentation/appkit/nseventmodifierflags/
    Local source `mdfind -name Events.h | grep Carbon`?
    """

    # fmt: off
    activate     = 1 << 0   # ?
    state_       = 1 << 15  # ?
    caps_lock    = 1 << 16  # aka int("0x00020000", 16) aka 65536
    shift        = 1 << 17
    control      = 1 << 18
    option       = 1 << 19  # alt or option
    command      = 1 << 20
    numericpad   = 1 << 21  # or an arrow key?
    help_key     = 1 << 22  # 8388608
    function     = 1 << 23  # rightControlKeyBit?
    # device_independent = int("0xffff0000", 16)  # kinda removes the mask?
    # fmt: on

    @classmethod
    def find_constituent_flags(cls, v: int) -> list[Modifiers]:
        flags = sorted(cls, key=lambda c: c.value, reverse=False)
        result_flags = [flag for flag in flags if v & flag.value]
        return result_flags
