from typing import *
from ..items.itemstack import ItemStack
from .clothingdisplay import ClothingDisplay


class HatRack(ClothingDisplay):
    """A `Hat Rack <https://terraria.gamepedia.com/Hat_Rack>`_ containing up to 2 dyed helmets."""
    def __init__(self, items: List[ItemStack], dyes: List[ItemStack]):
        super().__init__(items, dyes)
        assert len(items) == 2
        assert len(dyes) == 2
