from ..fileutils import Coordinates


class Sign:
    """A sign with something written on it."""

    __slots__ = "position", "text"

    def __init__(self, position: Coordinates, text: str = ""):
        self.position: Coordinates = position
        self.text: str = text

    def __repr__(self):
        return f"<Sign at {self.position}>"
