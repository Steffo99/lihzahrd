# language=rst
"""
Submodule containing :class:`.TileEntitiesCollection`.
"""

from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.composite.count_array import PackCountArray
from lihzahrd.terraria.world.tile_entities.tile_entity import TileEntity


class TileEntitiesCollection(PackCountArray[TileEntity]):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.count_array.PackCountArray` of all the tile entities (item frames, mannequins, etc.) in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ITEM = TileEntity

    @classmethod
    def _read_count(cls, fp: FileProcessor) -> int:
        return fp.read_int()

    @classmethod
    def _write_count(cls, fp: FileProcessor, count: int) -> None:
        fp.write_int(count)


__all__ = ("TileEntitiesCollection",)
