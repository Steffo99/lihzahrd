# language=rst
"""
Submodule containing :class:`.KiteExtra`.
"""

from dataclasses import dataclass
from typing import override

from lihzahrd.terraria.world.tile_entities.tile_entity_extra import TileEntityExtra


@dataclass
class KiteExtra(TileEntityExtra):
    """
    Extra data about a placed and anchored kite.
    """

    kind: int
    "The ID of the placed kite."

    @staticmethod
    @override
    def tile_entity_kind() -> int:
        return 9


__all__ = ("KiteExtra",)
