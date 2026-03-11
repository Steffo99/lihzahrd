# language=rst
"""
Submodule containing :class:`.HatRackExtra`.
"""

from dataclasses import dataclass
from typing import override

from lihzahrd.terraria.world.tile_entities.dyed_stack_data import DyedStackData
from lihzahrd.terraria.world.tile_entities.tile_entity_extra import TileEntityExtra


@dataclass
class HatRackExtra(TileEntityExtra):
    """
    Extra data about a :class:`HatRack`.
    """

    left: DyedStackData
    "The hat on the left."

    right: DyedStackData
    "The hat on the right."

    @staticmethod
    @override
    def tile_entity_kind() -> int:
        return 5


__all__ = ("HatRackExtra",)
