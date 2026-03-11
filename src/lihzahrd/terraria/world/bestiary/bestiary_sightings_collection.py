# language=rst
"""
Submodule containing :class:`.BestiarySightingsCollection`.
"""

from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.composite.count_array import PackCountArray
from lihzahrd.terraria.utils.pack.primitive.str import PackStrVariable


class BestiarySightingsCollection(PackCountArray):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.count_array.PackCountArray` of the Bestiary names of sighted characters.
    """

    _LOG = getLogger(__name__)

    ITEM = PackStrVariable

    @classmethod
    def _read_count(cls, fp: FileProcessor) -> int:
        return fp.read_int()

    @classmethod
    def _write_count(cls, fp: FileProcessor, count: int) -> None:
        fp.write_int(count)


__all__ = ("BestiarySightingsCollection",)
