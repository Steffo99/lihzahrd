from .block import Block
from .liquid import Liquid
from .wall import Wall
from .wiring import Wiring
from ..chests import Chest
from ..pressureplates import WeighedPressurePlate
from ..signs import Sign
from ..tileentities import TileEntity


class Tile:
    """A tile, composed by a block, a wall, a liquid and wires."""

    __slots__ = "block", "wall", "liquid", "wiring", "extra"

    def __init__(
            self,
            block: Block | None = None,
            wall: Wall | None = None,
            liquid: Liquid | None = None,
            wiring: Wiring | None = None,
            extra: Chest | Sign | WeighedPressurePlate | TileEntity | None = None,
    ):
        if wiring is None:
            wiring = Wiring()

        self.block: Block | None = block
        self.wall: Wall | None = wall
        self.liquid: Liquid | None = liquid
        self.wiring: Wiring | None = wiring

        self.extra: Chest | Sign | WeighedPressurePlate | TileEntity | None = extra
        """A reference to the extra data of this tile, such as Chest or Sign data."""

    def __repr__(self):
        tile_status = (
            f"{'B' if self.block else ''}"
            f"{'W' if self.wall else ''}"
            f"{'L' if self.liquid else ''}"
            f"{'W' if self.wiring else ''}"
            f"{'E' if self.extra else ''}"
        )
        return f"<Tile{' ' if tile_status else ''}{tile_status}>"
