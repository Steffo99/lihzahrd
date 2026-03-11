from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class CavernBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the cavern biome.
    """

    CAVERN_0 = 0
    "Unknown."

    CAVERN_1 = 1
    "Unknown."

    CAVERN_2 = 2
    "Unknown."

    CAVERN_3 = 3
    "Unknown."

    CAVERN_4 = 4
    "Unknown."

    CAVERN_5 = 5
    "Unknown."

    CAVERN_6 = 6
    "Unknown."

    CAVERN_7 = 7
    "Unknown."


class CavernBackground(PackEnum[CavernBackgroundEnum, int], PackInt):
    """
    The style of the cavern background in a segment of a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = CavernBackgroundEnum


__all__ = (
    "CavernBackgroundEnum",
    "CavernBackground",
)
