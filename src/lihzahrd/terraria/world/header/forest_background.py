from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class ForestBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the forest biome.
    """

    FOREST_0 = 0
    "Unknown."

    FOREST_1 = 1
    "Unknown."

    FOREST_2 = 2
    "Unknown."

    FOREST_3 = 3
    "Unknown."

    FOREST_4 = 4
    "Unknown."

    FOREST_5 = 5
    "Unknown."

    FOREST_6 = 6
    "Unknown."

    FOREST_7 = 7
    "Unknown."

    FOREST_8 = 8
    "Unknown."

    FOREST_9 = 9
    "Unknown."

    FOREST_10 = 10
    "Unknown."

    FOREST_11 = 11
    "Unknown."

    FOREST_12 = 12
    "Unknown."

    FOREST_13 = 13
    "Unknown."

    FOREST_31 = 31
    "Unknown."

    FOREST_51 = 51
    "Unknown."

    FOREST_71 = 71
    "Unknown."

    FOREST_72 = 72
    "Unknown."

    FOREST_73 = 73
    "Unknown."


class ForestBackground(PackEnum[ForestBackgroundEnum, int], PackByte):
    """
    The style of the forest background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = ForestBackgroundEnum


__all__ = (
    "ForestBackgroundEnum",
    "ForestBackground",
)
