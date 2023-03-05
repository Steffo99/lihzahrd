import typing
from ..enums import WallType


class Wall:
    """A wall that has been placed in the world."""

    __slots__ = "type", "paint", "is_illuminant", "is_echo"

    def __init__(
        self,
        type_: WallType,
        paint: typing.Optional[int] = None,
        is_illuminant: bool = False,
        is_echo: bool = False,
    ):
        self.type: WallType = type_
        self.paint: typing.Optional[int] = paint

        self.is_illuminant: bool = is_illuminant
        """If the wall had Illuminant Coating applied, and is unaffected by lighting."""

        self.is_echo: bool = is_echo
        """If the wall had Echo Coating applied, and is invisible."""

    def __repr__(self):
        return f"Wall(type_={repr(self.type)}, paint={self.paint}, is_illuminant={self.is_illuminant}, is_echo={self.is_echo})"
