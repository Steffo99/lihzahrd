from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool
from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean


class Milestone(OpBoolean[bool], PackBool):
    """
    A flag denoting whether a certain thing was accomplished in a Terraria world.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        if self.value:
            return f"<{self.__class__.__qualname__}: REACHED!>"
        else:
            return f"<{self.__class__.__qualname__}: incomplete>"


__all__ = ("Milestone",)
