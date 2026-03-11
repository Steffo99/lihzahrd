# language=rst
"""
Submodule containing :class:`.WorldSignsCollection`.
"""

from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.composite.count_array import PackCountArray
from lihzahrd.terraria.world.signs.world_sign import WorldSign


class WorldSignsCollection(PackCountArray[WorldSign]):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.count_array.PackCountArray` of all the readable blocks (signs) in a Terraria world.
    """

    _LOG = getLogger(__name__)

    MAX_COUNT = 32_000

    ITEM = WorldSign

    @classmethod
    def _read_count(cls, fp: FileProcessor) -> int:
        return fp.read_short()

    @classmethod
    def _write_count(cls, fp: FileProcessor, count: int) -> None:
        fp.write_short(count)


__all__ = ("WorldSignsCollection",)
