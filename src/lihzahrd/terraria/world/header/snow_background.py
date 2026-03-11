from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class SnowBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the snow biome.
    """

    SNOW_0 = 0
    "Unknown."

    SNOW_1 = 1
    "Unknown."

    SNOW_2 = 2
    "Unknown."

    SNOW_3 = 3
    "Unknown."

    SNOW_4 = 4
    "Unknown."

    SNOW_5 = 5
    "Unknown."

    SNOW_6 = 6
    "Unknown."

    SNOW_7 = 7
    "Unknown."

    SNOW_21 = 21
    "Unknown."

    SNOW_22 = 22
    "Unknown."

    SNOW_31 = 31
    "Unknown."

    SNOW_32 = 32
    "Unknown."

    SNOW_41 = 41
    "Unknown."

    SNOW_42 = 42
    "Unknown."


class SnowBackground(PackEnum[SnowBackgroundEnum, int], PackByte):
    """
    The style of the snow (surface ice) background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = SnowBackgroundEnum


__all__ = (
    "SnowBackgroundEnum",
    "SnowBackground",
)
