# Code licensed LGPLv3 by Jérémie Lumbroso <lumbroso@cs.princeton.edu>
import itertools
import textwrap
import typing


DEFAULT_SEPARATOR = " | "


def side_by_side(
    left: typing.List[str],
    right: typing.List[str],
    width: int = 78,
    separator: typing.Optional[str] = " | ",
    left_title: typing.Optional[str] = None,
    right_title: typing.Optional[str] = None,
) -> typing.List[str]:
    """Returns either the list of lines, or string of lines, that results from
    merging the two lists side-by-side.

    :param left: Lines of text to place on the left side
    :type left: typing.List[str]
    :param right: Lines of text to place on the right side
    :type right: typing.List[str]

    :param width: Character width of the overall output, defaults to 78
    :type width: int, optional
    :param separator: String separating the left and right side, defaults to " | "
    :type separator: typing.Optional[str], optional
    :param left_title: Title to place on the left side, defaults to None
    :type left_title: typing.Optional[str], optional
    :param right_title: Title to place on the right side, defaults to None
    :type right_title: typing.Optional[str], optional

    :return: Lines of the merged side-by-side output.
    :rtype: typing.List[str]
    """

    separator = separator or DEFAULT_SEPARATOR

    mid_width = (width - len(separator) - (1 - width % 2)) // 2

    tw = textwrap.TextWrapper(
        width=mid_width, break_long_words=False, replace_whitespace=False
    )

    def reflow(lines: list[str]) -> list[str]:
        wrapped_lines = list(map(tw.wrap, lines))
        wrapped_lines_with_linebreaks = [
            [""] if len(wls) == 0 else wls for wls in wrapped_lines
        ]
        return list(itertools.chain.from_iterable(wrapped_lines_with_linebreaks))

    left = reflow(left)
    right = reflow(right)

    zip_pairs = list(itertools.zip_longest(left, right))
    if left_title is not None or right_title is not None:
        left_title = left_title or ""
        right_title = right_title or ""
        zip_pairs = [
            (left_title, right_title),
            (mid_width * "-", mid_width * "-"),
        ] + list(zip_pairs)

    lines = []
    for left, right in zip_pairs:  # type:ignore
        left = left or ""  # type:ignore
        right = right or ""  # type:ignore
        line = "{}{}{}{}".format(
            left, (" " * max(0, mid_width - len(left))), separator, right
        )
        lines.append(line)

    return lines
