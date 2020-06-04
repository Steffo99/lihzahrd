from typing import *
from ..items.itemstack import ItemStack
from .clothingdisplay import ClothingDisplay


class HatRack(ClothingDisplay):
    """A `Hat Rack <https://terraria.gamepedia.com/Hat_Rack>`_ containing up to 2 dyed helmets."""
    def __init__(self, wearing_items: List[ItemStack], wearing_dyes: List[ItemStack]):
        super().__init__(wearing_items, wearing_dyes)
        assert len(wearing_items) == 2
        assert len(wearing_dyes) == 2
