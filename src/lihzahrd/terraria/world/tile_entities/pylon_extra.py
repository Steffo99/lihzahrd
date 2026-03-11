# language=rst
"""
Submodule containing :class:`.PylonExtra`.
"""

from dataclasses import dataclass
from typing import override

from lihzahrd.terraria.world.tile_entities.tile_entity_extra import TileEntityExtra


@dataclass
class PylonExtra(TileEntityExtra):
    """
    Extra data about a Pylon.
    """

    @staticmethod
    @override
    def tile_entity_kind() -> int:
        return 7


__all__ = ("PylonExtra",)
