import typing
from ..items import ItemStack
from ..fileutils import Coordinates


class Chest:
    """A chest with its contents."""

    def __init__(self, position: Coordinates, name: str, contents: typing.List[ItemStack]):
        self.position: Coordinates = position
        self.name: str = name
        self.contents: typing.List[ItemStack] = contents

    def __repr__(self):
        if self.name:
            return f'<Chest "{self.name}" at {self.position} with {len(self.contents)} items>'
        return f"<Chest at {self.position} with {len(self.contents)} items>"
