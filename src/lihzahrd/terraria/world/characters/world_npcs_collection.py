from logging import getLogger

from lihzahrd.terraria.utils.pack.composite.flag_array import PackFlagArray
from lihzahrd.terraria.world.characters.world_npc import WorldNPC


class WorldNPCCollection(PackFlagArray[WorldNPC]):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.flag_array.PackFlagArray` of all the NPCs in a Terraria world.
    """

    _LOG = getLogger(__name__)

    ITEM = WorldNPC
