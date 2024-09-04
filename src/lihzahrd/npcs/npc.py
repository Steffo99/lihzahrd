from typing import Optional
from ..enums import EntityType
from ..fileutils import Coordinates
from .mob import Mob


class NPC(Mob):
    """A NPC somewhere in the world."""

    __slots__ = "type", "name", "position", "home", "variation_index"

    def __init__(
        self,
        type_: EntityType,
        position: Coordinates,
        name: str,
        variation_index: int,
        home: Optional[Coordinates] = None,
    ):

        super().__init__(type_, position)

        self.name: str = name
        """The name of this NPC."""

        self.home: Optional[Coordinates] = home
        """The coordinates of the home of this NPC, or ``None`` if the NPC is homeless."""

        self.variation_index: int = variation_index
        """(Unknown) Possibly the current Zoologist (https://terraria.gamepedia.com/Zoologist) form?"""

    def __repr__(self):
        return f"<NPC {repr(self.type)} at {self.position}>"
