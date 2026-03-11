# language=rst
"""
Submodule containing processors for :class:`~lihzahrd.terraria.utils.structures.coordinates.Coordinates`.
"""

from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.utils.structures.coordinates import Coordinates


class PackCoordinatesInt(PackPrimitive[Coordinates[int]]):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing a pair of :class:`int` as :class:`~lihzahrd.terraria.utils.structures.coordinates.Coordinates`.
    """

    _LOG = getLogger(__name__)

    @classmethod
    @override
    def _validate(cls, value: Coordinates, **kwargs) -> None:
        for item in value:
            if not FileProcessor.INT_MIN <= item <= FileProcessor.INT_MAX:
                raise cls.OverflowError(value)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs) -> Coordinates:
        return Coordinates(
            x=fp.read_int(),
            y=fp.read_int(),
        )

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: Coordinates, **kwargs) -> None:
        fp.write_int(value.x)
        fp.write_int(value.y)

    @override
    def __repr__(self):
        return f"<{self.__class__.__qualname__}: ({self.value.x}, {self.value.y})>"

    class OverflowError(PackPrimitive[Coordinates].ValidationError):
        """
        The bounds are not within the representable range.
        """


__all__ = ("PackCoordinatesInt",)
