from itertools import batched
from math import ceil
from typing import Self

from ..version import Version
from ..worldversionedpackable import WorldVersionedPackable
from ...utils import FilePacker


class FrameImportantArray(WorldVersionedPackable):
    __slots__ = ("data",)

    def __init__(self, *data):
        self.data: list[bool] = list(data)

    def serialize(self, f: FilePacker, *, v: Version) -> None:
        count_bits = len(self.data)
        f.write_int2(count_bits)

        for bits in batched(self.data, n=8):
            f.write_bits(bits)

    @classmethod
    def deserialize(cls, f: FilePacker, *, v: Version) -> Self:
        data = []

        count_bits = f.read_int2()
        count_bytes = ceil(count_bits / 8)

        for _ in range(count_bytes):
            bits = f.read_bits()
            data = [*data, *bits]

        return cls(*data)


__all__ = (
    "FrameImportantArray",
)
