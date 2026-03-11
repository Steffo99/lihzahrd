from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class WorldDifficulty(IntEnum):
    """
    The difficulties a world can be in.
    """

    CLASSIC = 0
    "Classic mode, or Expert in For The Worthy."

    EXPERT = 1
    "Expert mode, or Master in For The Worthy."

    MASTER = 2
    "Master mode, or Legendary in For The Worthy."

    JOURNEY = 3
    "Journey mode."


class PackWorldDifficulty(PackEnum[WorldDifficulty, int], PackInt):
    """
    The base difficulty a Terraria world is set to.

    .. note::

        Having the "For The Worthy" special world seed increases the difficulty by one tier, and this class does not take that into account.
    """

    _LOG = getLogger(__name__)

    ENUM = WorldDifficulty

    def is_journey(self) -> bool:
        return self.value == WorldDifficulty.JOURNEY.value

    def is_classic(self) -> bool:
        return self.value == WorldDifficulty.CLASSIC.value

    def is_expert(self) -> bool:
        return self.value == WorldDifficulty.EXPERT.value

    def is_master(self) -> bool:
        return self.value == WorldDifficulty.MASTER.value

    def set_journey(self) -> None:
        self.value = WorldDifficulty.JOURNEY.value

    def set_classic(self) -> None:
        self.value = WorldDifficulty.CLASSIC.value

    def set_expert(self) -> None:
        self.value = WorldDifficulty.EXPERT.value

    def set_master(self) -> None:
        self.value = WorldDifficulty.MASTER.value


__all__ = (
    "WorldDifficulty",
    "PackWorldDifficulty",
)
