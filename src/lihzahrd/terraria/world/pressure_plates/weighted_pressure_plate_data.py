# language=rst
"""
Submodule containing :class:`.WeightedPressurePlateData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.utils.structures.coordinates import Coordinates


@dataclass
class WeightedPressurePlateData:
    """
    Data about a :class:`WeightedPressurePlate`.
    """

    position: Coordinates[int]
    "The position of the pressure plate."


__all__ = ("WeightedPressurePlateData",)
