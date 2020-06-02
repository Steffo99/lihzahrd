import typing
from .itemstack import ItemStack

class SingleItemDisplay:
    """Data pertaining to a single display item.
    Currently weapon rack (https://terraria.gamepedia.com/Weapon_Rack)
    and food plate (https://terraria.gamepedia.com/Plate).
     """

    __slots__ = "display_item", "display_type"

    def __init__(self,
                display_item: typing.List[ItemStack],
                display_type: str):

        self.display_item: typing.List[ItemStack] = display_item
        """What item is on display."""

        self.display_type: str =  display_type
        """What type of single item display this is."""

    def __repr__(self):
        return f"SingleItemDisplay(display_type={self.display_type}, display_item={self.display_item})"
