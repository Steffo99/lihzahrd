# language=rst
"""
Submodule for :class:`.ItemBase`.
"""

from logging import getLogger

from lihzahrd.terraria.data.classenums.item_enum import ItemEnum
from lihzahrd.terraria.data.classenums.prefix_enum import PrefixEnum
from lihzahrd.terraria.data.classmembers.prefix_base import PrefixBase

log = getLogger(__name__)


class ItemBase(metaclass=ItemEnum, register=False):
    """
    The kind of Terraria item.

    All items inherit from this; it's a :term:`ClassMemberBase` for members of :class:`.ItemEnum`.

    It:

    - annotates the mandatory attributes that all items should have.
    - defines the :meth:`__init__` method to create a :term:`ClassInstance`.

    :param quantity: The amount of items in the stack.
    :param prefix: The prefix of the items in the stack.
    """

    __slots__ = (
        "quantity",
        "prefix",
    )

    ID: int
    "The ID of the item."

    NAME: str
    "The name of the item."

    def __init__(self, quantity: int = 1, prefix: type[PrefixBase] | None = None) -> None:
        self.quantity: int = quantity
        "The amount of items in the stack."

        self.prefix: type[PrefixBase] | None = prefix
        "The prefix of the items in the stack."

    def __repr__(self):
        if self.prefix:
            return f"<{self.__class__.__qualname__}: {self.quantity}x, {self.prefix.NAME}>"
        else:
            return f"<{self.__class__.__qualname__}: {self.quantity}x>"

    def __str__(self):
        if self.prefix:
            return f"{self.quantity}x {self.prefix} {self.NAME}"
        else:
            return f"{self.quantity}x {self.NAME}"


__all__ = ("ItemBase",)
