# language=rst
"""
Submodule containing :class:`.LogicSensorExtra`.
"""

from dataclasses import dataclass
from typing import override

from lihzahrd.terraria.world.tile_entities.tile_entity_extra import TileEntityExtra


@dataclass
class LogicSensorExtra(TileEntityExtra):
    """
    Extra data about a logic sensor, like :class:`LogicGateAND`.
    """

    kind: int
    "The kind of logic sensor."

    enabled: bool
    "Whether the logic sensor is currently on or off."

    @staticmethod
    @override
    def tile_entity_kind() -> int:
        return 2


__all__ = ("LogicSensorExtra",)
