from __future__ import annotations
from typing import Self

from ...utils import FilePacker
from ..worldversionedpackable import WorldVersionedPackable
from ..version import Version


class Revision(WorldVersionedPackable):
    """
    The number of times a world was saved.
    """

    __slots__ = ("number",)

    def __init__(self, number: int):
        self.number: int = number

    def serialize(self, f: FilePacker, *, v: Version) -> None:
        f.write_uint4(self.number)

    @classmethod
    def deserialize(cls, f: FilePacker, *, v: Version) -> Self:
        return cls(f.read_uint4())

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.number})"

    def __str__(self) -> str:
        return str(self.number)

    def __eq__(self, other: Revision) -> bool:
        return self.number == other.number

    def __gt__(self, other: Revision) -> bool:
        return self.number > other.number

    def __ge__(self, other: Revision) -> bool:
        return self.number >= other.number

    def __lt__(self, other: Revision) -> bool:
        return self.number < other.number

    def __le__(self, other: Revision) -> bool:
        return self.number <= other.number


__all__ = (
    "Revision",
)
