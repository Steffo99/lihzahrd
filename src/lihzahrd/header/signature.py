from typing import Self
from enum import Enum

from lihzahrd.fileutils import Packable, FilePacker
from lihzahrd.header import Version


class Signature(Packable, Enum):
    """
    File signature written at the start of a Terraria world file.

    Has two different variants, one for the international Terraria version, and one for the Chinese version specifically.
    """

    __slots__ = ("text",)

    RELOGIC = "relogic"
    """International Terraria."""

    XINDONG = "xindong"
    """Chinese Terraria."""

    def write(self, f: FilePacker, v: Version):
        # noinspection PyTypeChecker
        # i'm pretty sure self.value is a str
        f.write_string_fixed(self.value, 7)

    @classmethod
    def read(cls, f: FilePacker, v: Version) -> Self:
        return cls(f.read_string_fixed(7))

    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.value})"

    def __str__(self):
        return self.value
