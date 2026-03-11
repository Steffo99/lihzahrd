# language=rst
"""
Submodule containing processors for :class:`~lihzahrd.terraria.utils.structures.rectangle.Rectangle`.
"""

from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.utils.structures.rectangle import Rectangle


class PackRectangleInt(PackPrimitive[Rectangle[int]]):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing four :class:`int` as a :class:`~lihzahrd.terraria.utils.structures.rectangle.Rectangle`.

    On validation, it ensures that the represented value is between :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.INT_MIN` and :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.INT_MAX`.
    """

    _LOG = getLogger(__name__)

    class OverflowError(PackPrimitive[Rectangle].ValidationError):
        """
        One of the :class:`~lihzahrd.terraria.utils.structures.rectangle.Rectangle` edges is not within representable range.
        """

    @classmethod
    def _validate(cls, value: Rectangle, **kwargs) -> None:
        for item in value:
            if not FileProcessor.INT_MIN <= item <= FileProcessor.INT_MAX:
                raise cls.OverflowError(value)

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs) -> Rectangle:
        return fp.read_rect()

    @classmethod
    def _write(cls, fp: FileProcessor, value: Rectangle, **kwargs) -> None:
        fp.write_rect(value)


__all__ = ("PackRectangleInt",)
