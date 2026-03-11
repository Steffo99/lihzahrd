# language=rst
"""
Submodule containing :class:`.ItemFrameExtra`.
"""

from dataclasses import dataclass
from typing import override

from lihzahrd.terraria.data.classmembers.item_base import ItemBase
from lihzahrd.terraria.world.tile_entities.tile_entity_extra import TileEntityExtra


@dataclass
class ItemFrameExtra(TileEntityExtra):
    """
    Extra data about an :class:`ItemFrame`.
    """

    item: ItemBase
    "The contained item."

    @staticmethod
    @override
    def tile_entity_kind() -> int:
        return 1


__all__ = ("ItemFrameExtra",)
