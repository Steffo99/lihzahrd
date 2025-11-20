from ..fileutils import Coordinates
from ..items import ItemStack


class Chest:
    """A chest with its contents."""

    __slots__ = "position", "name", "contents"

    def __init__(self, position: Coordinates, name: str, contents: list[ItemStack]):
        self.position: Coordinates = position
        self.name: str = name
        self.contents: list[ItemStack] = contents

    def __repr__(self):
        return (
            f'<Chest "{self.name}" at {self.position} '
            f"with {len(list(filter(lambda x: x is not None, self.contents)))} items>"
        )
