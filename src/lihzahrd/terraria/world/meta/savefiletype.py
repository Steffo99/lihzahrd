from enum import IntEnum
from typing import Self

from ...utils import FilePacker
from ..worldversionedpackable import WorldVersionedPackable
from ..version import Version


class SaveFileType(WorldVersionedPackable, IntEnum):
    """
    Terraria save file type.

    I do not know the meaning of this.
    """

    TWO = 2
    """Currently, Terraria worlds use this value."""

    def serialize(self, f: FilePacker, *, v: Version) -> None:
        f.write_uint1(self.value)

    @classmethod
    def deserialize(cls, f: FilePacker, *, v: Version) -> Self:
        return cls(f.read_uint1())

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.value})"

    def __str__(self) -> str:
        return str(self.value)


__all__ = (
    "SaveFileType",
)
