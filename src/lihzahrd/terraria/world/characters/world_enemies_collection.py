from logging import getLogger

from lihzahrd.terraria.utils.pack.composite.flag_array import PackFlagArray
from lihzahrd.terraria.world.characters.world_enemy import WorldEnemy


class WorldEnemiesCollection(PackFlagArray[WorldEnemy]):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.flag_array.PackFlagArray` of all the mobs in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ITEM = WorldEnemy


__all__ = ("WorldEnemiesCollection",)
