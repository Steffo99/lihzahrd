import typing
from ..items import ItemStack
from ..fileutils import Coordinates


class Chest:
    """A chest with its contents."""

    __slots__ = "position", "name", "contents"

    def __init__(self, position: Coordinates, name: str, contents: typing.List[ItemStack]):
        self.position: Coordinates = position
        self.name: str = name
        self.contents: typing.List[ItemStack] = contents

    def __repr__(self):
        return f'<Chest "{self.name}" at {self.position} ' \
               f'with {len(list(filter(lambda x: x is not None, self.contents)))} items>'
