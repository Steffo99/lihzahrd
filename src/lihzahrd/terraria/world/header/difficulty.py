from enum import IntEnum
from typing import Self

from ..version import Version
from ..worldversionedpackable import WorldVersionedPackable
from ...utils import FilePacker


class Difficulty(WorldVersionedPackable, IntEnum):
    """A world's raw difficulty level."""

    JOURNEY = 3
    """Journey mode."""

    CLASSIC = 0
    """Classic mode, or Expert mode in for-the-worthy worlds."""

    EXPERT = 1
    """Expert mode, or Master mode in for-the-worthy worlds."""

    MASTER = 2
    """Master mode, or Legendary mode in for-the-worthy worlds."""

    def __repr__(self):
        return f"{self.__class__.__qualname__}.{self.name}"

    def serialize(self, f: FilePacker, *, v: Version) -> None:
        f.write_int4(self.value)

    @classmethod
    def deserialize(cls, f: FilePacker, *, v: Version) -> Self:
        return cls(f.read_int4())
