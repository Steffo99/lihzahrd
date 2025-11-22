from typing import Self

from ...utils import FilePacker
from ..worldversionedpackable import WorldVersionedPackable
from ..version import Version


class Favorite(WorldVersionedPackable):
    """
    Whether the world is among the favorites or not.

    This uses an :class:`int` internally because for some reason this property is represented in the save file with a ``uint8``, and I want to be able to add more values to it if more are added without breaking compatibility (again).
    """

    __slots__ = ("value",)

    def __init__(self, value: int|bool):
        self.value: int = int(value)

    def serialize(self, f: FilePacker, *, v: Version) -> None:
        f.write_uint8(self.value)

    @classmethod
    def deserialize(cls, f: FilePacker, *, v: Version) -> Self:
        return cls(f.read_uint8())

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.value})"

    def __str__(self) -> str:
        match self.value:
            case 1:
                return "*"
            case 0:
                return ""
            case _:
                return "?"

    def __bool__(self) -> bool:
        return bool(self.value)


__all__ = (
    "Favorite",
)
