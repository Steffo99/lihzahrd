from typing import Dict, List
from ..enums import EntityType


class Bestiary:
    """A bestiary entry."""

    __slots__ = "chats", "kills", "sightings"

    def __init__(self, chats: List[EntityType], kills: Dict[EntityType, int], sightings: List[EntityType]):
        self.chats: List[EntityType] = chats
        self.kills: Dict[EntityType, int] = kills
        self.sightings: List[EntityType] = sightings

    def __repr__(self):
        return f"<Bestiary with {len(self.chats) + len(self.kills.keys()) + len(self.sightings)} entries>"
