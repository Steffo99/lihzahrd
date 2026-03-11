from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class InvasionKindEnum(IntEnum):
    """
    Possible kinds of invasions.
    """

    NONE = 0
    "No invasion is currently ongoing."

    GOBLIN = 1
    "A goblin army has arrived!"

    FROST = 2
    "The Frost Legion has arrived!"

    PIRATE = 3
    "The pirates have arrived!"

    MARTIAN = 4
    "Martians are invading!"


class InvasionKind(PackEnum[InvasionKindEnum, int], PackInt):
    """
    The kind of invasion that is currently ongoing.
    """

    _LOG = getLogger(__name__)

    ENUM = InvasionKindEnum


__all__ = (
    "InvasionKindEnum",
    "InvasionKind",
)
