from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.composite.count_array import PackCountArray
from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class WorldShimmeredNPCsCollection(PackCountArray[PackInt]):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.count_array.PackCountArray` of NPC IDs that are in their shimmered form.
    """

    _LOG = getLogger(__name__)

    MAX_COUNT = FileProcessor.INT_MAX

    ITEM = PackInt

    @classmethod
    def _read_count(cls, fp: FileProcessor) -> int:
        return fp.read_int()

    @classmethod
    def _write_count(cls, fp: FileProcessor, count: int) -> None:
        fp.write_uint(count)
