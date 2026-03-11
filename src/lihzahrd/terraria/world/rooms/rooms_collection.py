from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.composite.count_array import PackCountArray
from lihzahrd.terraria.world.rooms.room import Room


class RoomsCollection(PackCountArray[Room]):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.count_array.PackCountArray` of all the rooms assigned to NPCs in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ITEM = Room

    @classmethod
    def _read_count(cls, fp: FileProcessor) -> int:
        return fp.read_int()

    @classmethod
    def _write_count(cls, fp: FileProcessor, count: int) -> None:
        fp.write_int(count)


__all__ = ("RoomsCollection",)
