from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class CrimsonBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the crimson biome.
    """

    CRIMSON_0 = 0
    "Unknown."

    CRIMSON_1 = 1
    "Unknown."

    CRIMSON_2 = 2
    "Unknown."

    CRIMSON_3 = 3
    "Unknown."

    CRIMSON_4 = 4
    "Unknown."

    CRIMSON_5 = 4
    "Unknown."


class CrimsonBackground(PackEnum[CrimsonBackgroundEnum, int], PackByte):
    """
    The style of the crimson background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = CrimsonBackgroundEnum


__all__ = (
    "CrimsonBackgroundEnum",
    "CrimsonBackground",
)
