from typing import *
from ..items.itemstack import ItemStack


class ClothingDisplay:
    """Data pertaining to an item to display clothing."""

    __slots__ = "wearing_items", "wearing_dyes"

    def __init__(self,
                 wearing_items: List[ItemStack],
                 wearing_dyes: List[ItemStack]):

        self.wearing_items: List[ItemStack] = wearing_items
        """What items is the mannequin wearing."""
        self.wearing_dyes: List[ItemStack] = wearing_dyes
        """What dyes is the mannequin wearing."""

    def __repr__(self):
        return f"<{self.__class__.__qualname__} with {self.total_count} items inside>"

    @property
    def items_count(self):
        return len(list(filter(lambda x: x is not None, self.wearing_items)))

    @property
    def dyes_count(self):
        return len(list(filter(lambda x: x is not None, self.wearing_dyes)))

    @property
    def total_count(self):
        return self.items_count + self.dyes_count
