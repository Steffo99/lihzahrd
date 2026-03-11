from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.float import PackDouble
from lihzahrd.terraria.utils.pack.primitive.op.floating import OpFloating


class SlimeRainDuration(OpFloating[float], PackDouble):
    """
    Unknown.
    """

    _LOG = getLogger(__name__)


__all__ = ("SlimeRainDuration",)
