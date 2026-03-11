from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.float import PackDouble
from lihzahrd.terraria.utils.pack.primitive.op.floating import OpFloating


class Clock(OpFloating[float], PackDouble):
    """
    The in-game time of the world, at the moment it was saved.
    """

    _LOG = getLogger(__name__)


__all__ = ("Clock",)
