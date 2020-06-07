import typing


class Bestiary:
    """A bestiary entry."""

    __slots__ = "npc_chats_count", "npc_chats_data", "npc_kill_count", "npc_kill_data", "npc_sighting_count", "npc_sighting_data"

    def __init__(self,
                 npc_chats_count: int,
                 npc_chats_data: typing.Dict[str, int],
                 npc_kill_count: int,
                 npc_kill_data: typing.List[str],
                 npc_sighting_count: int,
                 npc_sighting_data: typing.List[str], ):
        self.npc_chats_count: int = npc_chats_count
        self.npc_chats_data: typing.Dict[str, int] = npc_chats_data
        self.npc_kill_count: int = npc_kill_count
        self.npc_kill_data: typing.List[str] = npc_kill_data
        self.npc_sighting_count: int = npc_sighting_count
        self.npc_sighting_data: typing.List[str] = npc_sighting_data

    def __repr__(self):
        return f"<Bestiary entry: chats={self.npc_chats_count}: {self.npc_chats_data}, kills={self.npc_kill_count}: {self.npc_kill_data}, sightings={self.npc_sighting_count}: {self.npc_sighting_data}>"
