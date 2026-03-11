from logging import getLogger
from typing import override
from copy import deepcopy

from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.coordinates import PackCoordinatesInt
from lihzahrd.terraria.utils.pack.primitive.op.equality import OpEquality
from lihzahrd.terraria.utils.structures.coordinates import Coordinates


class WorldSize(OpEquality[Coordinates], PackCoordinatesInt):
    """
    The size of a Terraria world, in tiles.

    .. note::

        For some reason, y is serialized before x.

        This is not an error.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        note = ""
        if self.is_small():
            note = " (small)"
        elif self.is_medium():
            note = " (medium)"
        elif self.is_large():
            note = " (large)"

        return f"<{self.__class__.__qualname__}: {self.value.x}x{self.value.y}{note}>"

    SMALL = Coordinates(x=4200, y=1200)
    """
    Size of a small world.
    """

    MEDIUM = Coordinates(x=6400, y=1800)
    """
    Size of a medium world.
    """

    LARGE = Coordinates(x=8400, y=2400)
    """
    Size of a large world.
    """

    def is_small(self) -> bool:
        """
        :return: Whether the world's size matches the size of a small world exactly.
        """
        return self.value == self.SMALL

    def is_medium(self) -> bool:
        """
        :return: Whether the world's size matches the size of a medium world exactly.
        """
        return self.value == self.MEDIUM

    def is_large(self) -> bool:
        """
        :return: Whether the world's size matches the size of a large world exactly.
        """
        return self.value == self.LARGE

    def set_small(self) -> None:
        """
        Set :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` to the size of a small world.
        """
        self.value = deepcopy(self.SMALL)

    def set_medium(self) -> None:
        """
        Set :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` to the size of a medium world.
        """
        self.value = deepcopy(self.MEDIUM)

    def set_large(self) -> None:
        """
        Set :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` to the size of a large world.
        """
        self.value = deepcopy(self.LARGE)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs) -> Coordinates:
        # Yes, they are swapped!
        return Coordinates(
            y=fp.read_int(),
            x=fp.read_int(),
        )

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: Coordinates, **kwargs) -> None:
        # Yes, they are swapped!
        fp.write_int(value.y)
        fp.write_int(value.x)


__all__ = ("WorldSize",)
