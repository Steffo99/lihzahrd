from dataclasses import dataclass

from lihzahrd.terraria.data.classmembers.npc_base import NPCBase
from lihzahrd.terraria.utils.structures.coordinates import Coordinates


@dataclass
class RoomData:
    """
    Data about a room assigned to an NPC.
    """

    npc: type[NPCBase]
    "The NPC assigned to the room."

    position: Coordinates[int]
    "The position of the room, in world coordinates."


__all__ = ("RoomData",)
