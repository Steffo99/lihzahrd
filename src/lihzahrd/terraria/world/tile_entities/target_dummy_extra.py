# language=rst
"""
Submodule containing :class:`.TargetDummyExtra`.
"""

from dataclasses import dataclass
from typing import override

from lihzahrd.terraria.world.tile_entities.tile_entity_extra import TileEntityExtra


@dataclass
class TargetDummyExtra(TileEntityExtra):
    """
    Extra data about a :class:`TargetDummy`.
    """

    character_index: int

    @staticmethod
    @override
    def tile_entity_kind() -> int:
        return 0


__all__ = ("TargetDummyExtra",)
