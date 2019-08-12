import typing
from .npctype import EntityType
from ..fileutils import Coordinates


class NPC:
    """A NPC somewhere in the world."""

    __slots__ = "type", "name", "position", "home"

    def __init__(self,
                 type_: EntityType,
                 name: str,
                 position: Coordinates,
                 home: typing.Optional[Coordinates] = None):
        self.type: EntityType = type_
        """The NPC this object represents."""

        self.name: str = name
        """The name of this NPC."""

        self.position: Coordinates = position
        """The position of the mob in the game world."""

        self.home: typing.Optional[Coordinates] = home
        """The coordinates of the home of this NPC, or None if the NPC is homeless."""

    def __repr__(self):
        return f"<NPC {repr(self.type)} at {self.position}>"
