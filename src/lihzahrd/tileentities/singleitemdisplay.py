from ..items.itemstack import ItemStack


class SingleItemDisplay:
    """A display case for a single item, such as a `Weapon Rack <https://terraria.gamepedia.com/Weapon_Rack>`_,
    a `Item Frame <https://terraria.gamepedia.com/Item_Frame>`_ or a `Plate <https://terraria.gamepedia.com/Plate>`_.
    """

    __slots__ = ("item",)

    def __init__(self, item: ItemStack):
        self.item: ItemStack = item
        """The item which is on display."""

    def __repr__(self):
        return f"<{self.__class__.__qualname__} with {repr(self.item)} inside>"
