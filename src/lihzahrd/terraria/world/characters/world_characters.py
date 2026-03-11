# language=rst
"""
Submodule containing :class:`.WorldCharacters`.
"""

from logging import getLogger
from typing import Self, override

from lihzahrd.terraria.utils.pack.composite.composite import PackComposite as PaCo
from lihzahrd.terraria.utils.pack.pack import Pack
from lihzahrd.terraria.world.characters.world_enemies_collection import WorldEnemiesCollection
from lihzahrd.terraria.world.characters.world_npcs_collection import WorldNPCCollection
from lihzahrd.terraria.world.characters.world_shimmered_npcs_collection import WorldShimmeredNPCsCollection


class WorldCharacters(PaCo):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.composite.PackComposite` containing information about the characters present in the Terraria world.

    For some reason, shimmer status of the town NPCs is saved in a separate array than the rest of the NPC data.
    """

    _LOG = getLogger(__name__)

    shimmered_npcs: PaCo.Field[Self, WorldShimmeredNPCsCollection] = PaCo.Field(WorldShimmeredNPCsCollection)

    npcs: PaCo.Field[Self, WorldNPCCollection] = PaCo.Field(WorldNPCCollection)

    enemies: PaCo.Field[Self, WorldEnemiesCollection] = PaCo.Field(WorldEnemiesCollection)

    # noinspection PyTypeChecker
    @override
    def __init__(self, *args: Pack):
        self.shimmered_npcs: WorldShimmeredNPCsCollection = ...
        self.npcs: WorldNPCCollection = ...
        self.enemies: WorldEnemiesCollection = ...

        super().__init__(*args)

    @classmethod
    @override
    def _fields(cls, **kwargs) -> list[PaCo.Field[Self, Pack]]:
        return [cls.shimmered_npcs, cls.npcs, cls.enemies]


__all__ = ("WorldCharacters",)
