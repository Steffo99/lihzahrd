from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool
from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean


class SpecialSeedActive(OpBoolean[bool], PackBool):
    """
    A flag denoting whether a world is running a special world seed.

    As of 1.4.5.4, special world seeds are:

    - Drunk world
    - For the worthy
    - 10th Anniversary
    - Don't Starve
    - Not the bees
    - Remix
    - No traps
    - Zenith
    - Skyblock
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        if self.value:
            return f"<{self.__class__.__qualname__}: ACTIVE!>"
        else:
            return f"<{self.__class__.__qualname__}: inactive>"


__all__ = ("SpecialSeedActive",)
