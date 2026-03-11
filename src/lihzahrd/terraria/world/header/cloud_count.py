from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackShort
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class CloudCount(OpInteger[int], PackShort):
    """
    Unknown.
    """

    _LOG = getLogger(__name__)


__all__ = ("CloudCount",)
