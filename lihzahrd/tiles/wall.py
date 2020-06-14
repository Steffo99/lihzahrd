import typing
from ..enums import WallType


class Wall:
    """A wall that has been placed in the world."""

    __slots__ = "type", "paint"

    def __init__(self, type_: WallType, paint: typing.Optional[int] = None):
        self.type: WallType = type_
        self.paint: typing.Optional[int] = paint

    def __repr__(self):
        return f"Wall(type_={repr(self.type)}, paint={self.paint})"
