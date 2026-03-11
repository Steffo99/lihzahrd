from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackInt
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class CultistsCooldown(OpInteger[int], PackInt):
    """
    Unknown.
    """

    _LOG = getLogger(__name__)


__all__ = ("CultistsCooldown",)
