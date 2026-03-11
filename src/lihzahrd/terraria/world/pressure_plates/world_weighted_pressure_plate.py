# language=rst
"""
Submodule containing :class:`.WorldWeightedPressurePlate`.
"""

from logging import getLogger
from typing import Any

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.utils.structures.coordinates import Coordinates
from lihzahrd.terraria.world.pressure_plates.weighted_pressure_plate_data import WeightedPressurePlateData


class WorldWeightedPressurePlate(PackPrimitive[WeightedPressurePlateData]):
    """
    A :class:`WeighedPressurePlate` that's placed in a Terraria world.
    """

    _LOG = getLogger(__name__)

    @classmethod
    def _validate(cls, value: WeightedPressurePlateData, **kwargs: Any) -> None:
        pass

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> WeightedPressurePlateData:
        return WeightedPressurePlateData(
            position=Coordinates(
                x=fp.read_int(),
                y=fp.read_int(),
            )
        )

    @classmethod
    def _write(cls, fp: FileProcessor, value: WeightedPressurePlateData, **kwargs: Any) -> None:
        fp.write_int(value.position.x)
        fp.write_int(value.position.y)


__all__ = ("WorldWeightedPressurePlate",)
