from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackInt
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class LanternNightSpontaneousCooldown(OpInteger[int], PackInt):
    """
    How much time must pass before a new *Lantern Night* can spontaneously start again (if Moon Lord is defeated).
    """

    _LOG = getLogger(__name__)


__all__ = ("LanternNightSpontaneousCooldown",)
