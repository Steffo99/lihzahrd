from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackInt
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class InvasionPower(OpInteger[int], PackInt):
    """
    How many enemies are in the invasion, either remaining or total.
    """

    _LOG = getLogger(__name__)


__all__ = ("InvasionPower",)
