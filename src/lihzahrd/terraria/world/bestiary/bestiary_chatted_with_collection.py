# language=rst
"""
Submodule containing :class:`.BestiaryChattedWithCollection`.
"""

from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.composite.count_array import PackCountArray
from lihzahrd.terraria.utils.pack.primitive.str import PackStrVariable


class BestiaryChattedWithCollection(PackCountArray):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.count_array.PackCountArray` of the Bestiary counts of NPCs that were spoken to.
    """

    _LOG = getLogger(__name__)

    ITEM = PackStrVariable

    @classmethod
    def _read_count(cls, fp: FileProcessor) -> int:
        return fp.read_int()

    @classmethod
    def _write_count(cls, fp: FileProcessor, count: int) -> None:
        fp.write_int(count)


__all__ = ("BestiaryChattedWithCollection",)
