# language=rst
"""
Submodule for rectangle structures.
"""

from collections.abc import Iterator


class Rectangle[Value = int]:
    """
    A rectangle of generic type ``InternalValue`` in a cartesian plane, not locked to the origin.

    In Terraria worlds, ``InternalValue`` will always be :class:`int`.
    """

    __slots__ = ("left", "right", "top", "bottom")

    def __init__(self, left: Value, right: Value, top: Value, bottom: Value):
        self.left: Value = left
        "Coordinate of the left edge of the rectangle."

        self.right: Value = right
        "Coordinate of the right edge of the rectangle."

        self.top: Value = top
        "Coordinate of the top edge of the rectangle."

        self.bottom: Value = bottom
        "Coordinate of the bottom edge of the rectangle."

    def __repr__(self) -> str:
        left = self.left
        right = self.right
        top = self.top
        bottom = self.bottom
        return f"Rect({left=}, {right=}, {top=}, {bottom=})"

    def __iter__(self) -> Iterator[Value]:
        """
        :return: The edges in the order they are written in Terraria save files: :attr:`.left`, :attr:`.right`, :attr:`.top`, then :attr:`.bottom`.
        """
        return iter((self.left, self.right, self.top, self.bottom))
