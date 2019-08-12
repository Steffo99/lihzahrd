import typing
from .block import Block
from .wall import Wall
from .liquid import Liquid
from .wiring import Wiring
from ..chests import Chest


class Tile:
    """A tile, composed by a block, a wall, a liquid and wires."""

    __slots__ = "block", "wall", "liquid", "wiring", "extra"

    def __init__(self,
                 block: typing.Optional[Block] = None,
                 wall: typing.Optional[Wall] = None,
                 liquid: typing.Optional[Liquid] = None,
                 wiring: typing.Optional[Wiring] = None,
                 extra: typing.Optional[typing.Union[Chest]] = None):
        if wiring is None:
            wiring = Wiring()

        self.block: typing.Optional[Block] = block
        self.wall: typing.Optional[Wall] = wall
        self.liquid: typing.Optional[Liquid] = liquid
        self.wiring: typing.Optional[Wiring] = wiring
        self.extra: typing.Optional[typing.Union[Chest]] = extra

    def __repr__(self):
        return f"<Tile {'B' if self.block else '_'}{'W' if self.wall else '_'}{'L' if self.liquid else '_'}{'W' if self.wiring else '_'}{'E' if self.extra else '_'}>"
