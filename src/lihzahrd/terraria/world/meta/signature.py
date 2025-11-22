from typing import Self
from enum import Enum

from ...utils import FilePacker
from ..worldversionedpackable import WorldVersionedPackable
from ..version import Version


class Signature(WorldVersionedPackable, Enum):
    """
    File signature written at the start of a Terraria world file.

    Has two different variants, one for the international Terraria version, and one for the Chinese version specifically.
    """

    RELOGIC = "relogic"
    """International Terraria."""

    XINDONG = "xindong"
    """Chinese Terraria."""

    def serialize(self, f: FilePacker, *, v: Version) -> None:
        # noinspection PyTypeChecker
        # i'm pretty sure self.value is a str
        f.write_string_fixed(self.value, 7)

    @classmethod
    def deserialize(cls, f: FilePacker, *, v: Version) -> Self:
        return cls(f.read_string_fixed(7))

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.value})"

    def __str__(self) -> str:
        return self.value


__all__ = (
    "Signature",
)
