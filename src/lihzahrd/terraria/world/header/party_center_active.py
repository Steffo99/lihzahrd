from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool
from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean


class PartyCenterActive(OpBoolean[bool], PackBool):
    """
    Whether a Party Center is active or not.
    """

    _LOG = getLogger(__name__)

    def __repr__(self):
        if self.value:
            return f"<{self.__class__.__qualname__}: PARTY TIME!!!>"
        else:
            return f"<{self.__class__.__qualname__}: inactive>"


__all__ = ("PartyCenterActive",)
