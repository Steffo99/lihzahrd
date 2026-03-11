# language=rst
"""
Submodule containing :class:`.FoodPlateExtra`.
"""

from dataclasses import dataclass
from typing import override

from lihzahrd.terraria.data.classmembers.item_base import ItemBase
from lihzahrd.terraria.world.tile_entities.tile_entity_extra import TileEntityExtra


@dataclass
class FoodPlateExtra(TileEntityExtra):
    """
    Extra data about a :class:`Plate`.
    """

    item: ItemBase
    "The stored item."

    @staticmethod
    @override
    def tile_entity_kind() -> int:
        return 6


__all__ = ("FoodPlateExtra",)
