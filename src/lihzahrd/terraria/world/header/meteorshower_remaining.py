from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.pack.primitive.int import PackInt
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class MeteorShowerRemaining(OpInteger[int], PackInt):
    """
    How many meteors are left in the shower.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        if self.value:
            return f"<{self.__class__.__qualname__}: {self.value} meteors remaining>"
        else:
            return f"<{self.__class__.__qualname__}: not ongoing>"


__all__ = ("MeteorShowerRemaining",)
