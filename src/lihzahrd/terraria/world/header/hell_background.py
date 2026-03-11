from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class HellBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the hell biome.
    """

    HELL_0 = 0
    "Unknown."

    HELL_1 = 1
    "Unknown."

    HELL_2 = 2
    "Unknown."


class HellBackground(PackEnum[HellBackgroundEnum, int], PackInt):
    """
    The style of the hell background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = HellBackgroundEnum


__all__ = (
    "HellBackgroundEnum",
    "HellBackground",
)
