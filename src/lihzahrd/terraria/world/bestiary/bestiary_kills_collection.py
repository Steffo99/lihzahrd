# language=rst
"""
Submodule containing :class:`.BestiaryKillsCollection`.
"""

from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.composite.count_array import PackCountArray
from lihzahrd.terraria.world.bestiary.bestiary_dict_entry import BestiaryDictEntry


class BestiaryKillsCollection(PackCountArray):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.count_array.PackCountArray` of the Bestiary counts of killed monsters.
    """

    _LOG = getLogger(__name__)

    ITEM = BestiaryDictEntry

    @classmethod
    def _read_count(cls, fp: FileProcessor) -> int:
        return fp.read_int()

    @classmethod
    def _write_count(cls, fp: FileProcessor, count: int) -> None:
        fp.write_int(count)


__all__ = ("BestiaryKillsCollection",)
