# Code licensed LGPLv3 by Jérémie Lumbroso <lumbroso@cs.princeton.edu>

import difflib
import typing
from typing import Optional  # TODO(3.10): Move to new union syntax after dropping 3.9

from mac_keyboard_shortcuts.utils.print_side_by_side import side_by_side


try:
    from termcolor import colored
except ImportError:

    def colored(text: str, color: str, on_color: Optional[str] = None) -> str:  # type: ignore
        return text


def better_diff(
    left: typing.List[str],
    right: typing.List[str],
    width: int = 78,
    print_common_lines: bool = True,
    use_colours: bool = False,
    separator: Optional[str] = None,
    left_title: Optional[str] = None,
    right_title: Optional[str] = None,
) -> typing.List[str]:
    """Returns a side-by-side comparison of the two provided inputs, showing
    common lines between both inputs, and the lines that are unique to each.

    :param left: Lines of text to place on the left side
    :type left: typing.List[str]
    :param right: Lines of text to place on the right side
    :type right: typing.List[str]

    :param width: Character width of the overall output, defaults to 78
    :type width: int, optional
    :param print_common_lines: Whether to print lines identical in left and right, defaults to True
    :type print_common_lines: bool, optional
    :param use_colours: Whether to print in colour using colorama, defaults to False
    :type use_colours: bool, optional
    :param separator: String separating the left and right side, defaults to " | "
    :type separator: typing.Optional[str], optional
    :param left_title: Title to place on the left side, defaults to None
    :type left_title: typing.Optional[str], optional
    :param right_title: Title to place on the right side, defaults to None
    :type right_title: typing.Optional[str], optional

    :return: Lines of the merged side-by-side diff comparison output.
    :rtype: typing.List[str]
    """

    def _c(text: str, color: str, on_color: Optional[str] = None) -> str:
        if use_colours:
            return colored(text, color, on_color)  # type: ignore
        else:
            return text

    differ = difflib.Differ()

    left_side = []
    right_side = []

    # adapted from
    # LINK: https://stackoverflow.com/a/66091742/408734
    difflines = list(differ.compare(left, right))

    for line in difflines:
        op = line[0]
        tail = line[2:]
        if op == " " and print_common_lines:
            # line is same in both
            left_side.append(tail)
            right_side.append(tail)

        elif op == "-":
            # line is only on the left
            left_side.append(_c(tail, "red"))
            right_side.append("")

        elif op == "+":
            # line is only on the right
            left_side.append("")
            right_side.append(_c(tail, "green"))

    return side_by_side(
        left=left_side,
        right=right_side,
        width=width,
        separator=separator,
        left_title=left_title,
        right_title=right_title,
    )
