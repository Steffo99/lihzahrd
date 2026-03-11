from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.float import PackDouble
from lihzahrd.terraria.utils.pack.primitive.op.floating import OpFloating


class WorldLayerBoundary(OpFloating[float], PackDouble):
    """
    The vertical tile coordinate at which the active layer changes.

    For example, the underground-cavern boundary.
    """

    _LOG = getLogger(__name__)


__all__ = ("WorldLayerBoundary",)
