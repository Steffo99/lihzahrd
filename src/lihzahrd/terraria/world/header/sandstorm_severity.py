from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.float import PackFloat
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class SandstormSeverity(OpInteger[float], PackFloat):
    """
    Unknown.
    """

    _LOG = getLogger(__name__)


__all__ = ("SandstormSeverity",)
