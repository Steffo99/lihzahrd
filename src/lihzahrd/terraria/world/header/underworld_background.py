from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class UnderworldBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the underworld biome.
    """

    UNDERWORLD_0 = 0
    "Unknown."

    UNDERWORLD_1 = 1
    "Unknown."

    UNDERWORLD_2 = 2
    "Unknown."


class UnderworldBackground(PackEnum[UnderworldBackgroundEnum, int], PackByte):
    """
    The style of the underworld background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = UnderworldBackgroundEnum


__all__ = (
    "UnderworldBackgroundEnum",
    "UnderworldBackground",
)
