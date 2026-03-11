from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class MushroomBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the glowing mushroom biome.
    """

    MUSHROOM_0 = 0
    "Unknown."

    MUSHROOM_1 = 1
    "Unknown."

    MUSHROOM_2 = 2
    "Unknown."

    MUSHROOM_3 = 3
    "Unknown."

    MUSHROOM_4 = 4
    "Unknown."


class MushroomBackground(PackEnum[MushroomBackgroundEnum, int], PackByte):
    """
    The style of the mushroom background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = MushroomBackgroundEnum


__all__ = (
    "MushroomBackgroundEnum",
    "MushroomBackground",
)
