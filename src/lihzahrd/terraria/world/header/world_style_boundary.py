from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackInt
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class WorldStyleBoundary(OpInteger[int], PackInt):
    """
    The horizontal tile coordinate at which something changes style.

    Might be forest trees and background, or cavern background.
    """

    _LOG = getLogger(__name__)


__all__ = ("WorldStyleBoundary",)
