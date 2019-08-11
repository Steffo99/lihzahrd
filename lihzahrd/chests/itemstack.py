from .itemtype import ItemType


class ItemStack:
    """A stack of a certain item."""
    def __init__(self,
                 type_: ItemType,
                 quantity: int = 1,
                 modifier: int = 0):

        self.type: ItemType = type_
        """The type of item represented in this stack."""

        self.quantity: int = quantity
        """A number from 1 to 999 representing the number of items inside this stack."""

        self.modifier: int = modifier
        """The modifier of the item in this stack. Should be set only when quantity is 1."""

    def __repr__(self):
        return f"<ItemStack of {self.quantity}x {repr(self.type)} ({self.modifier})>"
