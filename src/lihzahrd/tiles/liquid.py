from ..enums import LiquidType


class Liquid:
    """A liquid present in a tile."""

    __slots__ = "type", "volume"

    def __init__(self, type_: LiquidType, volume: int = 255):
        self.type: LiquidType = type_
        """The type of liquid present in the tile."""

        self.volume: int = volume
        """The volume of liquid present in the tile.
        
        0 means the tile has no liquid, while 255 means the tile is full of liquid.
        
        Values over 255 aren't supported."""
        assert 0 <= volume <= 255
