from ..enums import EntityType
from ...utils import Coordinates


class Room:
    __slots__ = "npc", "position"

    def __init__(self, npc: EntityType, position: Coordinates):
        self.npc: EntityType = npc
        self.position: Coordinates = position

    def __repr__(self):
        return f"<Room for {self.npc} at {self.position}>"
