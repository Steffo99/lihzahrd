from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackInt
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class PartySpontaneousCooldown(OpInteger[int], PackInt):
    """
    How much time must pass before a new party can spontaneously start again.
    """

    _LOG = getLogger(__name__)


__all__ = ("PartySpontaneousCooldown",)
