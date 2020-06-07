import typing
from ..enums import EntityType
from ..fileutils import Coordinates


class Mob:
    """A Mob somewhere in the world."""

    __slots__ = "type", "position"

    def __init__(self,
                 type_: EntityType,
                 position: Coordinates, ):
        self.type: EntityType = type_
        """The type of entity this object represents."""

        self.position: Coordinates = position
        """The position of the mob in the game world."""

    def __repr__(self):
        return f"<Mob {repr(self.type)} at {self.position}>"
