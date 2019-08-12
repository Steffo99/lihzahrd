import typing
from ..fileutils import Coordinates


class NPC:
    """A NPC somewhere in the world."""
    def __init__(self,
                 sprite_id: int,
                 name: str,
                 position: Coordinates,
                 home: typing.Optional[Coordinates] = None):
        self.sprite_id: int = sprite_id
        self.name: str = name
        self.position: Coordinates = position
        self.home: typing.Optional[Coordinates] = home

    def __repr__(self):
        return f"<NPC {self.name if self.name else '_'} at {self.position}>"
