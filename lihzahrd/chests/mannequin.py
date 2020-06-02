import typing
from .itemstack import ItemStack

class Mannequin:
    """Data pertaining to a Logic Sensor (https://terraria.gamepedia.com/Mannequin)."""

    __slots__ = "item_flags", "dye_flags", "wearing_items", "wearing_dyes"

    def __init__(self,
                item_flags: typing.List[bool],
                dye_flags: typing.List[bool],
                wearing_items: typing.List[ItemStack],
                wearing_dyes: typing.List[ItemStack],):

        self.item_flags: typing.List[bool] = item_flags
        """Which slots have items in them."""
        self.dye_flags: typing.List[bool] = dye_flags
        """Which slots have dyes in them."""
        self.wearing_items: typing.List[ItemStack] = wearing_items
        """What items is the mannequin wearing."""
        self.wearing_dyes: typing.List[ItemStack] = wearing_dyes
        """What dyes is the mannequin wearing."""


    def __repr__(self):
        return f"Mannequin()"
