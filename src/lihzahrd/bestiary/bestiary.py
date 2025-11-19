from ..enums import EntityType


class Bestiary:
    """A bestiary entry."""

    __slots__ = "chats", "kills", "sightings"

    def __init__(self, chats: list[EntityType], kills: dict[EntityType, int], sightings: list[EntityType]):
        self.chats: list[EntityType] = chats
        self.kills: dict[EntityType, int] = kills
        self.sightings: list[EntityType] = sightings

    def __repr__(self):
        return f"<Bestiary with {len(self.chats) + len(self.kills.keys()) + len(self.sightings)} entries>"
