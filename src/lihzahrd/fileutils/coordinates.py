class Coordinates:
    """A pair of coordinates."""
    
    __slots__ = "x", "y"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coordinates({self.x}, {self.y})"

    def __str__(self):
        return f"{self.x}, {self.y}"
