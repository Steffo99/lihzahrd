from typing import *
from ..items.itemstack import ItemStack


class ClothingDisplay:
    """Data pertaining to an item to display clothing."""

    __slots__ = "items", "dyes"

    def __init__(self, items: List[ItemStack], dyes: List[ItemStack]):

        self.items: List[ItemStack] = items
        """What items is the display wearing."""

        self.dyes: List[ItemStack] = dyes
        """What dyes is the display wearing."""

    def __repr__(self):
        return f"<{self.__class__.__qualname__} with {self.total_count} items inside>"

    @property
    def items_count(self):
        return len(list(filter(lambda x: x is not None, self.items)))

    @property
    def dyes_count(self):
        return len(list(filter(lambda x: x is not None, self.dyes)))

    @property
    def total_count(self):
        return self.items_count + self.dyes_count
