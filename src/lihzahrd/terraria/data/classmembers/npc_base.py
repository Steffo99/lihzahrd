# language=rst
"""
Submodule for :class:`.NPCBase`.
"""

from logging import getLogger

from lihzahrd.terraria.data.classenums.npc_enum import NPCEnum
from lihzahrd.terraria.utils.structures.coordinates import Coordinates

log = getLogger(__name__)


class NPCBase(metaclass=NPCEnum, register=False):
    """
    The kind of Terraria NPC.

    All NPCs inherit from this; it's a :term:`ClassMemberBase` for members of :class:`.NPCEnum`.

    It:

    - annotates the mandatory attributes that all NPCs should have.
    """

    __slots__ = (
        "name",
        "position",
        "is_homeless",
        "home",
        "is_town_npc",
        "flag_1",
        "flag_2",
        "flag_3",
        "flag_4",
        "flag_5",
        "flag_6",
        "flag_7",
        "variation_index",
        "homeless_despawn",
    )

    ID: int
    "The ID of the NPC."

    JOB: str
    "The job name of the NPC."

    def __init__(
        self,
        name: str,
        position: Coordinates[float],
        is_homeless: bool,
        home: Coordinates[int],
        is_town_npc: bool,
        flag_1: bool,
        flag_2: bool,
        flag_3: bool,
        flag_4: bool,
        flag_5: bool,
        flag_6: bool,
        flag_7: bool,
        variation_index: int | None,
        homeless_despawn: bool,
    ):
        self.name: str = name
        "The name of the NPC."

        self.position: Coordinates[float] = position
        "The current position of the NPC."

        self.is_homeless: bool = is_homeless
        "Whether this NPC has a home or not."

        self.home: Coordinates[int] = home
        "The position of the last home of the NPC."

        self.is_town_npc: bool = is_town_npc
        "Unknown. Determines whether :attr:`variation_index` is saved for this NPC."

        self.flag_1: bool = flag_1
        "Currently unused."

        self.flag_2: bool = flag_2
        "Currently unused."

        self.flag_3: bool = flag_3
        "Currently unused."

        self.flag_4: bool = flag_4
        "Currently unused."

        self.flag_5: bool = flag_5
        "Currently unused."

        self.flag_6: bool = flag_6
        "Currently unused."

        self.flag_7: bool = flag_7
        "Currently unused."

        self.variation_index: int | None = variation_index
        "Unknown."

        self.homeless_despawn: bool = homeless_despawn
        "Unknown."

    def __repr__(self):
        return f"<{self.__class__.__qualname__}>"


__all__ = ("NPCBase",)
