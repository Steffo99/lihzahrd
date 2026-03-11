from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool
from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean


class PartySpontaneousActive(OpBoolean[bool], PackBool):
    """
    Whether a (spontaneous) party is ongoing or not.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        if self.value:
            return f"<{self.__class__.__qualname__}: PARTY TIME!!!>"
        else:
            return f"<{self.__class__.__qualname__}: inactive>"


__all__ = ("PartySpontaneousActive",)
