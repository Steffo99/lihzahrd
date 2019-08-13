from ..chests import ItemStack


class ItemFrame:
    """Data pertaining to an https://terraria.gamepedia.com/Item_Frame ."""

    __slots__ = ("item", )

    def __init__(self, item: ItemStack):
        self.item: ItemStack = item

    def __repr__(self):
        return f"<ItemFrame with {repr(self.item)} inside>"
