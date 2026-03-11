# language=rst
"""
Submodule containing :class:`.ItemFlaskExtra`.
"""

from dataclasses import dataclass
from typing import override

from lihzahrd.terraria.data.classmembers.item_base import ItemBase
from lihzahrd.terraria.world.tile_entities.tile_entity_extra import TileEntityExtra


@dataclass
class ItemFlaskExtra(TileEntityExtra):
    """
    Extra data about a :class:`DeadCellsDisplayJar`.
    """

    item: ItemBase
    "The stored item."

    @staticmethod
    @override
    def tile_entity_kind() -> int:
        return 8


__all__ = ("ItemFlaskExtra",)
