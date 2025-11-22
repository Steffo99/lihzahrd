import enum


class MoonStyle(enum.IntEnum):
    """All possible moon styles."""

    WHITE = 0
    ORANGE = 1
    RINGED_GREEN = 2
    BLUE = 3
    ICE = 4
    GREEN = 5
    PINK = 6
    PINK_ORANGE = 7
    TRIPLE_PURPLE = 8

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"
