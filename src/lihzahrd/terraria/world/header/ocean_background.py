from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class OceanBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the ocean biome.
    """

    OCEAN_0 = 0
    "Unknown."

    OCEAN_1 = 1
    "Unknown."

    OCEAN_2 = 2
    "Unknown."

    OCEAN_3 = 3
    "Unknown."

    OCEAN_4 = 4
    "Unknown."

    OCEAN_5 = 5
    "Unknown."

    OCEAN_6 = 6
    "Unknown."

    OCEAN_7 = 7
    "Unknown."


class OceanBackground(PackEnum[OceanBackgroundEnum, int], PackByte):
    """
    The style of the ocean background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = OceanBackgroundEnum


__all__ = (
    "OceanBackgroundEnum",
    "OceanBackground",
)
