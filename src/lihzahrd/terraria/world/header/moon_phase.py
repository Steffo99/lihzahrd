from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackUInt


class MoonPhaseEnum(IntEnum):
    """
    Possible moon phases.
    """

    FULL = 0
    "Full Moon."

    WANING_GIBBOUS = 1
    "Waning Gibbous Moon."

    THIRD_QUARTER = 2
    "Third Quarter Moon."

    WANING_CRESCENT = 3
    "Waning Crescent Moon."

    NEW = 4
    "New Moon."

    WAXING_CRESCENT = 5
    "Waxing Crescent Moon."

    FIRST_QUARTER = 6
    "First Quarter Moon."

    WAXING_GIBBOUS = 7
    "Waxing Gibbous Moon."


class MoonPhase(PackEnum[MoonPhaseEnum, int], PackUInt):
    """
    The phase of the moon in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = MoonPhaseEnum


__all__ = (
    "MoonPhaseEnum",
    "MoonPhase",
)
