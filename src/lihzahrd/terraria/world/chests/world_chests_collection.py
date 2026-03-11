from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.composite.count_array import PackCountArray
from lihzahrd.terraria.world.chests.world_chest import WorldChest


class WorldChestsCollection(PackCountArray[WorldChest]):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.count_array.PackCountArray` of all the item containers (chests) in a Terraria world.
    """

    _LOG = getLogger(__name__)

    MAX_COUNT = 8_000

    ITEM = WorldChest

    @classmethod
    def _read_count(cls, fp: FileProcessor) -> int:
        return fp.read_short()

    @classmethod
    def _write_count(cls, fp: FileProcessor, count: int) -> None:
        fp.write_short(count)
