from logging import getLogger
from typing import override

from lihzahrd.terraria.world.header.milestone import Milestone


class EnemyDefeated(Milestone):
    """
    A flag denoting whether a certain enemy (tipically a boss) was defeated in a Terraria world.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        if self.value:
            return f"<{self.__class__.__qualname__}: DEFEATED!>"
        else:
            return f"<{self.__class__.__qualname__}: alive>"


__all__ = ("EnemyDefeated",)
