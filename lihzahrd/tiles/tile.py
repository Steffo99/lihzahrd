import typing
from .block import Block
from .wall import Wall
from .liquid import Liquid
from .wiring import Wiring
from ..chests import Chest
from ..signs import Sign
from ..pressureplates import WeighedPressurePlate
from ..tileentities import TileEntity


class Tile:
    """A tile, composed by a block, a wall, a liquid and wires."""

    __slots__ = "block", "wall", "liquid", "wiring", "extra"

    def __init__(self,
                 block: typing.Optional[Block] = None,
                 wall: typing.Optional[Wall] = None,
                 liquid: typing.Optional[Liquid] = None,
                 wiring: typing.Optional[Wiring] = None,
                 extra: typing.Optional[typing.Union[Chest, Sign, WeighedPressurePlate, TileEntity]] = None):
        if wiring is None:
            wiring = Wiring()

        self.block: typing.Optional[Block] = block
        self.wall: typing.Optional[Wall] = wall
        self.liquid: typing.Optional[Liquid] = liquid
        self.wiring: typing.Optional[Wiring] = wiring

        self.extra: typing.Optional[typing.Union[Chest, Sign, WeighedPressurePlate, TileEntity]] = extra
        """A reference to the extra data of this tile, such as Chest or Sign data."""

    def __repr__(self):
        tile_status = f"{'B' if self.block else ''}" \
                      f"{'W' if self.wall else ''}" \
                      f"{'L' if self.liquid else ''}" \
                      f"{'W' if self.wiring else ''}" \
                      f"{'E' if self.extra else ''}"
        return f"<Tile{' ' if tile_status else ''}{tile_status}>"
