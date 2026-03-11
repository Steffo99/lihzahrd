from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class WorldID(PackInt):
    """
    The (regular) ID of a Terraria world, used to name the corresponding map file.
    """

    _LOG = getLogger(__name__)


__all__ = ("WorldID",)
