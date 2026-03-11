from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class JungleSurfaceBackground(PackByte):
    """
    The style of the surface jungle background in a segment of a Terraria world.

    Possible values are currently unknown.
    """

    _LOG = getLogger(__name__)


__all__ = ("JungleSurfaceBackground",)
