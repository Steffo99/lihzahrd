from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.pack.primitive.int import PackByte
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class ShadowOrbCount(OpInteger[int], PackByte):
    """
    How many *Shadow Orbs* / *Crimson Hearts* have been smashed since the last time *Eater of Worlds* / *Brain of Cthulhu* was fought.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        return f"<{self.__class__.__qualname__}: {self.value} / {self.REQUIRED_FOR_BOSS}>"

    REQUIRED_FOR_BOSS = 3
    "How many shadow orbs need to be smashed to summon the World Evil boss in general."

    def remaining_before_boss(self):
        """
        :return: How many shadow orbs still need to be smashed to summon the World Evil boss in the current world.
        """

        return self.REQUIRED_FOR_BOSS - self.value

    class UnexpectedOrbCountError(OpInteger[int].ValidationError):
        """
        The number of smashed shadow orbs is unexpectedly out of range.
        """

    @classmethod
    @override
    def _validate(cls, value: int, **kwargs) -> None:
        super()._validate(value, **kwargs)

        if not 0 <= value < cls.REQUIRED_FOR_BOSS:
            raise cls.UnexpectedOrbCountError(value)


__all__ = ("ShadowOrbCount",)
