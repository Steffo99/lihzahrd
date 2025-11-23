from typing import TypeVar

CoordinateType = TypeVar("CoordinateType")


class Coordinates:
    """A pair of coordinates."""

    __slots__ = ("x", "y")

    def __init__(self, x: CoordinateType, y: CoordinateType):
        self.x: CoordinateType = x
        self.y: CoordinateType = y

    def __repr__(self):
        x = self.x
        y = self.y
        return f"Coordinates({x=}, {y=})"

    def __str__(self):
        return f"({self.x}, {self.y})"


__all__ = (
    "Coordinates",
)