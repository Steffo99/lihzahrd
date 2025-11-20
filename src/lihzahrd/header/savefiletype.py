from enum import IntEnum
from typing import Self

from lihzahrd.fileutils import Packable, FilePacker
from lihzahrd.header import Version


class SaveFileType(Packable, IntEnum):
    """
    Terraria save file type.

    I do not know the meaning of this.
    """

    TWO = 2
    """Currently, Terraria worlds use this value."""

    def write(self, f: FilePacker, v: Version | None):
        f.write_uint1(self.value)

    @classmethod
    def read(cls, f: FilePacker, v: Version | None) -> Self:
        return cls(f.read_uint1())

    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.value})"

    def __str__(self):
        return self.value
