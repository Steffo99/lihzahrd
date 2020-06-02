import typing
from .itemstack import ItemStack

class ClothingDisplay:
    """Data pertaining to an item to display clothing.
    Currently this is a Womannequin/Mannequin (https://terraria.gamepedia.com/Womannequin)
    and hat rack (https://terraria.gamepedia.com/Hat_Rack).
    """

    __slots__ = "item_flags", "dye_flags", "wearing_items", "wearing_dyes", "display_type"

    def __init__(self,
                item_flags: typing.List[bool],
                dye_flags: typing.List[bool],
                wearing_items: typing.List[ItemStack],
                wearing_dyes: typing.List[ItemStack],
                display_type: str,):

        self.item_flags: typing.List[bool] = item_flags
        """Which slots have items in them."""
        self.dye_flags: typing.List[bool] = dye_flags
        """Which slots have dyes in them."""
        self.wearing_items: typing.List[ItemStack] = wearing_items
        """What items is the mannequin wearing."""
        self.wearing_dyes: typing.List[ItemStack] = wearing_dyes
        """What dyes is the mannequin wearing."""
        self.display_type: str = display_type
        """What type of display is this?"""


    def __repr__(self):
        return f"ClothingDisplay(type={self.display_type}, dyes={len(self.wearing_dyes)}, )"
