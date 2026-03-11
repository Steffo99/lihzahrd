# language=rst
"""
Submodule containing :class:`.TileEntityData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.utils.structures.coordinates import Coordinates
from lihzahrd.terraria.world.tile_entities.tile_entity_extra import TileEntityExtra


@dataclass
class TileEntityData:
    """
    Data about any tile entity.

    The kind of entity that this class represents is given by the specific class of the value of the :attr:`.extra` parameter.
    """

    id: int
    "Unknown."

    position: Coordinates[int]
    "The position of the tile entity in world coordinates."

    extra: TileEntityExtra
    """
    Extra data about the tile entity. The kind of tile entity is determined by the class of this value.
    
    .. todo::
    
        A better, more extensible way to implement this would be via a :term:`ClassEnum` and inheritance, as that would allow new kinds of tile entities to be registered without having to edit :mod:`lihzahrd`.
    """

    def kind(self) -> int:
        """
        :return: The kind ID of the tile entity, as determined by the :meth:`TileEntityExtra.tile_entity_kind` of the :attr:`.extra` parameter.
        """
        return self.extra.tile_entity_kind()


__all__ = ("TileEntityData",)
