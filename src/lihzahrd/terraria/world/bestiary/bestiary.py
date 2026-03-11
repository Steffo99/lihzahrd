# language=rst
"""
Submodule containing :class:`.Bestiary`.
"""

from logging import getLogger
from typing import Self, override

from lihzahrd.terraria.utils.pack.composite.composite import PackComposite as PaCo
from lihzahrd.terraria.utils.pack.pack import Pack
from lihzahrd.terraria.world.bestiary.bestiary_chatted_with_collection import BestiaryChattedWithCollection
from lihzahrd.terraria.world.bestiary.bestiary_kills_collection import BestiaryKillsCollection
from lihzahrd.terraria.world.bestiary.bestiary_sightings_collection import BestiarySightingsCollection


class Bestiary(PaCo):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.composite.PackComposite` to process everything that's tracked by a Terraria world's Bestiary.
    """

    _LOG = getLogger(__name__)

    kills: PaCo.Field[Self, BestiaryKillsCollection] = PaCo.Field(BestiaryKillsCollection)
    "Monster kill counts."

    sightings: PaCo.Field[Self, BestiarySightingsCollection] = PaCo.Field(BestiarySightingsCollection)
    "Character sightings."

    chatted_with: PaCo.Field[Self, BestiaryChattedWithCollection] = PaCo.Field(BestiaryChattedWithCollection)
    "NPCs spoken to."

    # noinspection PyTypeChecker
    @override
    def __init__(self, *args: Pack):
        self.kills: BestiaryKillsCollection = ...
        self.sightings: BestiarySightingsCollection = ...
        self.chatted_with: BestiaryChattedWithCollection = ...

        super().__init__(*args)

    @classmethod
    @override
    def _fields(cls, **kwargs) -> list[PaCo.Field[Self, Pack]]:
        return [cls.kills, cls.sightings, cls.chatted_with]


__all__ = ("Bestiary",)
