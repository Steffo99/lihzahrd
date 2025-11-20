from .clothingdisplay import ClothingDisplay
from ..items.itemstack import ItemStack


class Mannequin(ClothingDisplay):
    """A `Mannequin <https://terraria.gamepedia.com/Mannequin>`_
    / `Womannequin <https://terraria.gamepedia.com/Womannequin>`_ containing up to 3 dyed armor pieces and up
    to 5 dyed accessories."""

    def __init__(self, items: list[ItemStack], dyes: list[ItemStack]):
        super().__init__(items, dyes)
        assert len(items) == 8
        assert len(dyes) == 8
