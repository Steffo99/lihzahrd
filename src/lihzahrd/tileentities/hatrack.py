from .clothingdisplay import ClothingDisplay
from ..items.itemstack import ItemStack


class HatRack(ClothingDisplay):
    """A `Hat Rack <https://terraria.gamepedia.com/Hat_Rack>`_ containing up to 2 dyed helmets."""

    def __init__(self, items: list[ItemStack], dyes: list[ItemStack]):
        super().__init__(items, dyes)
        assert len(items) == 2
        assert len(dyes) == 2
