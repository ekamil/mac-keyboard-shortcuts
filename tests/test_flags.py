import pytest

from mac_keyboard_shortcuts.consts.modifiers import Modifiers


@pytest.mark.parametrize(
    "current_value, expected_mods",
    [
        (8650752, {Modifiers.function, Modifiers.control}),
        (8781824, {Modifiers.control, Modifiers.function, Modifiers.shift}),
    ],
)
def test_flag_read_write(current_value: int, expected_mods: set[Modifiers]) -> None:
    actual = Modifiers.find_constituent_flags(current_value)
    assert expected_mods == set(actual)
    assert sum((m.value for m in expected_mods)) == current_value
