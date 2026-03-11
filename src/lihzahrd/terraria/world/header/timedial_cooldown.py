from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackByte
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class TimedialCooldown(OpInteger, PackByte):
    """
    How many days a *Sundial* or *Moondial* is in cooldown for.
    """

    _LOG = getLogger(__name__)


__all__ = ("TimedialCooldown",)
