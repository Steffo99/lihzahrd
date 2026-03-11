# language=rst
"""
Submodule containing :class:`.WorldSignData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.utils.structures.coordinates import Coordinates


@dataclass
class WorldSignData:
    """
    Data about a readable block (a sign).
    """

    text: str
    "The displayed text."

    position: Coordinates
    "The position of the block which displays the text."


__all__ = ("WorldSignData",)
