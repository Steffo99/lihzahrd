from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class HallowBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the hallow biome.
    """

    HALLOW_0 = 0
    "Unknown."

    HALLOW_1 = 1
    "Unknown."

    HALLOW_2 = 2
    "Unknown."

    HALLOW_3 = 3
    "Unknown."

    HALLOW_4 = 4
    "Unknown."


class HallowBackground(PackEnum[HallowBackgroundEnum, int], PackByte):
    """
    The style of the hallow background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = HallowBackgroundEnum


__all__ = (
    "HallowBackgroundEnum",
    "HallowBackground",
)
