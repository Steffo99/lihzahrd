from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class IceBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the ice biome.
    """

    ICE_0 = 0
    "Unknown."

    ICE_1 = 1
    "Unknown."

    ICE_2 = 2
    "Unknown."

    ICE_3 = 3
    "Unknown."


class IceBackground(PackEnum[IceBackgroundEnum, int], PackInt):
    """
    The style of the ice (underground snow) background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = IceBackgroundEnum


__all__ = (
    "IceBackgroundEnum",
    "IceBackground",
)
