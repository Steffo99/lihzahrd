from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class CorruptionBackgroundEnum(IntEnum):
    """
    Possible backgrounds of the corruption biome.
    """

    CORRUPTION_0 = 0
    "Unknown."

    CORRUPTION_1 = 1
    "Unknown."

    CORRUPTION_2 = 2
    "Unknown."

    CORRUPTION_3 = 3
    "Unknown."

    CORRUPTION_4 = 4
    "Unknown."

    CORRUPTION_51 = 51
    "Unknown."

    CORRUPTION_52 = 52
    "Unknown."


class CorruptionBackground(PackEnum[CorruptionBackgroundEnum, int], PackByte):
    """
    The style of the corruption background in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = CorruptionBackgroundEnum


__all__ = (
    "CorruptionBackgroundEnum",
    "CorruptionBackground",
)
