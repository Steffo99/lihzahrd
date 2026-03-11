# language=rst
"""
Submodule for pairs of coordinates.
"""

from collections.abc import Iterator
from typing import Any


class Coordinates[Value = int]:
    """
    A pair of coordinates of the generic type ``InternalValue``.

    In Terraria worlds, ``InternalValue`` will be either :class:`float` (usually when referring to entities) or :class:`int` (usually when referring to tiles).
    """

    __slots__ = ("x", "y")

    def __init__(self, x: Value, y: Value):
        self.x: Value = x
        "The horizontal coordinate, with the negative axis being left, and the positive axis being right."

        self.y: Value = y
        "The vertical coordinate, with the negative axis being up, and the negative axis being down."

    def __repr__(self) -> str:
        x = self.x
        y = self.y
        return f"{self.__class__.__qualname__}({x=}, {y=})"

    def __iter__(self) -> Iterator[Value]:
        """
        :return: :attr:`.x` then :attr:`.y`, in that order.
        """
        return iter((self.x, self.y))

    def __eq__(self, other: Any) -> bool:
        """
        :return: If compared with other :class:`Coordinates`, whether both individual coordinates are equal. Otherwise, :obj:`NotImplemented`.
        """
        if isinstance(other, Coordinates):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __ne__(self, other: Any) -> bool:
        """
        :return: If compared with other :class:`Coordinates`, whether either coordinate is not equal to its corrispective. Otherwise, :obj:`NotImplemented`.
        """
        if isinstance(other, Coordinates):
            return self.x != other.x or self.y != other.y
        else:
            return NotImplemented
