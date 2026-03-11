from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class DesertBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the crimson biome.
    """

    DESERT_0 = 0
    "Unknown."

    DESERT_1 = 1
    "Unknown."

    DESERT_2 = 2
    "Unknown."

    DESERT_3 = 3
    "Unknown."

    DESERT_4 = 4
    "Unknown."

    DESERT_51 = 51
    "Unknown."

    DESERT_52 = 52
    "Unknown."

    DESERT_53 = 53
    "Unknown."


class DesertBackground(PackEnum[DesertBackgroundEnum, int], PackByte):
    """
    The style of the desert background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = DesertBackgroundEnum


__all__ = (
    "DesertBackgroundEnum",
    "DesertBackground",
)
