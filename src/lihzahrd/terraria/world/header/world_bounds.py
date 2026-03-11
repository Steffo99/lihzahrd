from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.rectangle import PackRectangleInt


class WorldBounds(PackRectangleInt):
    """
    Camera bounds of the world.
    """

    _LOG = getLogger(__name__)


__all__ = ("WorldBounds",)
