from enum import IntEnum
from typing import Self

from lihzahrd.fileutils import Packable, FilePacker
from lihzahrd.header import Version


class Favorite(Packable, IntEnum):
    """
    Whether the world is among the favorites or not.

    This uses an :class:`IntEnum` because for some reason this property is represented in the save file with a ``uint8``, and I want to be able to add more values to it if more are added without breaking compatibility (again).
    """

    NO = 0
    YES = 1

    def write(self, f: FilePacker, v: Version):
        f.write_uint8(self.value)

    @classmethod
    def read(cls, f: FilePacker, v: Version) -> Self:
        return cls(f.read_uint8())

    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.value})"

    def __str__(self):
        match self:
            case Favorite.NO:
                return ""
            case Favorite.YES:
                return "*"
