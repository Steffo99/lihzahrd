from logging import getLogger
from typing import override

from lihzahrd.terraria.world.header.milestone import Milestone


class NPCRescued(Milestone):
    """
    A flag denoting whether a NPC was rescued in a Terraria world.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        if self.value:
            return f"<{self.__class__.__qualname__}: RESCUED!>"
        else:
            return f"<{self.__class__.__qualname__}: missing>"


__all__ = ("NPCRescued",)
