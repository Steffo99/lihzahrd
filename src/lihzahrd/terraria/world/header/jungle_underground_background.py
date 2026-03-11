from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class JungleUndergroundBackgroundEnum(IntEnum):
    UNDERGROUND_JUNGLE_0 = 0
    UNDERGROUND_JUNGLE_1 = 1
    UNDERGROUND_JUNGLE_2 = 2
    UNDERGROUND_JUNGLE_3 = 3
    UNDERGROUND_JUNGLE_4 = 4
    UNDERGROUND_JUNGLE_5 = 5


class JungleUndergroundBackground(PackEnum[JungleUndergroundBackgroundEnum, int], PackInt):
    """
    The style of the underground jungle background in a segment of a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = JungleUndergroundBackgroundEnum


__all__ = (
    "JungleUndergroundBackgroundEnum",
    "JungleUndergroundBackground",
)
