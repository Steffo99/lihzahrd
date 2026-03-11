from dataclasses import dataclass

from lihzahrd.terraria.utils.structures.coordinates import Coordinates


@dataclass
class WorldEnemyData:
    """
    Data about an enemy in a Terraria world.
    """

    kind: int
    "The kind of enemy represented by this data."

    position: Coordinates[float]
    "The position of the enemy."


__all__ = ("WorldEnemyData",)
