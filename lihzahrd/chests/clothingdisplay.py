import typing
from .itemstack import ItemStack


class ClothingDisplay:
    """Data pertaining to an item to display clothing."""

    __slots__ = "wearing_items", "wearing_dyes"

    def __init__(self,
                 wearing_items: typing.List[ItemStack],
                 wearing_dyes: typing.List[ItemStack]):

        self.wearing_items: typing.List[ItemStack] = wearing_items
        """What items is the mannequin wearing."""
        self.wearing_dyes: typing.List[ItemStack] = wearing_dyes
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


class Mannequin(ClothingDisplay):
    """A `Mannequin <https://terraria.gamepedia.com/Mannequin>`_
    / `Womannequin <https://terraria.gamepedia.com/Womannequin>`_ containing up to 3 dyed armor pieces and up
    to 5 dyed accessories."""
    def __init__(self, wearing_items: typing.List[ItemStack], wearing_dyes: typing.List[ItemStack]):
        super().__init__(wearing_items, wearing_dyes)
        assert len(wearing_items) == 8
        assert len(wearing_dyes) == 8


class HatRack(ClothingDisplay):
    """A `Hat Rack <https://terraria.gamepedia.com/Hat_Rack>`_ containing up to 2 dyed helmets."""
    def __init__(self, wearing_items: typing.List[ItemStack], wearing_dyes: typing.List[ItemStack]):
        super().__init__(wearing_items, wearing_dyes)
        assert len(wearing_items) == 2
        assert len(wearing_dyes) == 2
