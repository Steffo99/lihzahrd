from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.float import PackDouble
from lihzahrd.terraria.utils.pack.primitive.op.floating import OpFloating


class InvasionPosition(OpFloating[float], PackDouble):
    """
    The current horizontal position of an invasion.

    Approaches the spawn point's horizontal position at 60 tiles per second.
    """

    _LOG = getLogger(__name__)


__all__ = ("InvasionPosition",)
