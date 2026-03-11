# language=rst
"""
Submodule containing :class:`.WorldChestData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.data.classmembers.item_base import ItemBase
from lihzahrd.terraria.utils.structures.coordinates import Coordinates


@dataclass
class WorldChestData:
    """
    Data about an item container (a chest).
    """

    position: Coordinates
    "The position of the chest, in world coordinates."

    name: str
    "The name of the chest."

    contents: list[ItemBase | None]
    "The stacks of items stored inside the chest, or :obj:`None` for empty slots."


__all__ = ("WorldChestData",)
