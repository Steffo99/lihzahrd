from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.composite.count_array import PackCountArray
from lihzahrd.terraria.world.pressure_plates.world_weighted_pressure_plate import WorldWeightedPressurePlate


class WorldWeightedPressurePlatesCollection(PackCountArray[WorldWeightedPressurePlate]):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.count_array.PackCountArray` of all the Weighted Pressure Plates in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ITEM = WorldWeightedPressurePlate

    @classmethod
    def _read_count(cls, fp: FileProcessor) -> int:
        return fp.read_int()

    @classmethod
    def _write_count(cls, fp: FileProcessor, count: int) -> None:
        fp.write_int(count)


__all__ = ("WorldWeightedPressurePlatesCollection",)
