import enum


class Shape(enum.IntEnum):
    """The shape of a block, given to it with an hammer.

    The directions refer to the missing slope corner."""

    NORMAL = 0
    HALF_TILE = 1
    TOP_RIGHT_SLOPE = 2
    TOP_LEFT_SLOPE = 3
    BOTTOM_RIGHT_SLOPE = 4
    BOTTOM_LEFT_SLOPE = 5

    @classmethod
    def from_flags(cls, flags2):
        return cls(flags2[6] * 4 + flags2[5] * 2 + flags2[4])
