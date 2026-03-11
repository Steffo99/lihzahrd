# language=rst
"""
Submodule containing :class:`.DyedStackData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.data.classmembers.item_base import ItemBase


@dataclass
class DyedStackData:
    """
    Data about an item with a dye applied to it.

    Used in mannequins and weapon racks.
    """

    item: ItemBase | None
    "The item slot."

    dye: ItemBase | None
    "The dye slot."


__all__ = ("DyedStackData",)
