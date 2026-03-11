from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.float import PackFloat
from lihzahrd.terraria.utils.pack.primitive.op.floating import OpFloating


class RainStrength(OpFloating[float], PackFloat):
    """
    Unknown.
    """

    _LOG = getLogger(__name__)


__all__ = ("RainStrength",)
