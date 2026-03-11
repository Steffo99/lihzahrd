from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.float import PackFloat


class WindSpeed(PackFloat):
    """
    Unknown.
    """

    _LOG = getLogger(__name__)


__all__ = ("WindSpeed",)
