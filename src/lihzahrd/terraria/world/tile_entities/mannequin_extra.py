# language=rst
"""
Submodule containing :class:`.MannequinExtra`.
"""

from dataclasses import dataclass
from typing import override

from lihzahrd.terraria.data.classmembers.item_base import ItemBase
from lihzahrd.terraria.world.tile_entities.dyed_stack_data import DyedStackData
from lihzahrd.terraria.world.tile_entities.tile_entity_extra import TileEntityExtra


@dataclass
class MannequinExtra(TileEntityExtra):
    """
    Extra data about a :class:`Mannequin` or a :class:`Womannequin`.
    """

    pose: int
    """
    The pose the mannequin is in.
    
    .. todo::
    
        Determine and validate which kinds of poses exist.
    """

    helmet: DyedStackData
    "The helmet slot."

    shirt: DyedStackData
    "The shirt slot."

    pants: DyedStackData
    "The pants slot."

    accessory_1: DyedStackData
    "The first accessory slot."

    accessory_2: DyedStackData
    "The second accessory slot."

    accessory_3: DyedStackData
    "The third accessory slot."

    accessory_4: DyedStackData
    "The fourth accessory slot."

    accessory_5: DyedStackData
    "The fifth accessory slot."

    mount: DyedStackData
    "The mount slot."

    weapon: ItemBase | None
    "The weapon slot."

    @staticmethod
    @override
    def tile_entity_kind() -> int:
        return 3


__all__ = ("MannequinExtra",)
