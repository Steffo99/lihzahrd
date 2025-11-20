from typing import Self

from lihzahrd.fileutils import Packable, FilePacker
from lihzahrd.header import Version


class Revision(Packable):
    """
    The number of times a world was saved.
    """

    __slots__ = ("number",)

    def __init__(self, number: int):
        self.number: int = number

    def write(self, f: FilePacker, v: Version):
        f.write_uint4(self.number)

    @classmethod
    def read(cls, f: FilePacker, v: Version) -> Self:
        return cls(f.read_uint4())

    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.number})"

    def __str__(self):
        return str(self.number)

    def __eq__(self, other):
        return self.number == other.number

    def __gt__(self, other):
        return self.number > other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number
