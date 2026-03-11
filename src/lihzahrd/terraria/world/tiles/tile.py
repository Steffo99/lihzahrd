# language=rst
"""
Submodule containing :class:`.Tile`.
"""

from typing import Literal, Any

from numpy import ndarray, zeros

from lihzahrd.terraria.data.classenums.block_enum import BlockEnum
from lihzahrd.terraria.data.classenums.liquid_enum import LiquidEnum
from lihzahrd.terraria.data.classenums.wall_enum import WallEnum
from lihzahrd.terraria.data.classmembers.block_base import BlockBase
from lihzahrd.terraria.data.classmembers.liquid_base import LiquidBase
from lihzahrd.terraria.data.classmembers.wall_base import WallBase
from lihzahrd.terraria.data.enums.block_shape import BlockShapeEnum
from lihzahrd.terraria.data.enums.paint import PaintEnum
from lihzahrd.terraria.world.frame_important.world_frame_important import WorldFrameImportant
from lihzahrd.terraria.world.tiles.array_dtype import TILE_DTYPE
from lihzahrd.terraria.world.tiles.wiring import Wiring


class Tile:
    """
    Developer-friendly representation of a tile in a Terraria world, with its characteristics.
    """

    __slots__ = (
        "block",
        "wall",
        "liquid",
        "wiring",
    )

    def __init__(
        self,
        *,
        block: BlockBase | None = None,
        wall: WallBase | None = None,
        liquid: LiquidBase | None = None,
        wiring: Wiring | None = None,
    ):
        self.block: BlockBase | None = block
        "The foreground block present in the tile, or :obj:`None` if there isn't any."

        self.wall: WallBase | None = wall
        "The background wall present in the tile, or :obj:`None` if there isn't any."

        self.liquid: LiquidBase | None = liquid
        "The liquid present in the tile, or :obj:`None` if there isn't any."

        self.wiring: Wiring = wiring or Wiring()
        "The wiring present in the tile."

    def __repr__(self):
        block = self.block
        wall = self.wall
        liquid = self.liquid
        wiring = self.wiring
        params = ""
        if block is not None:
            params += f"{block=}, "
        if wall is not None:
            params += f"{wall=}, "
        if liquid is not None:
            params += f"{liquid=}, "
        if wiring is not None:
            params += f"{wiring=}"
        return f"{self.__class__.__qualname__}({params})"

    def to_scalar(self) -> ndarray[tuple[Literal[1]], Any]:
        """
        Convert a :class:`.Tile` into a scalar :class:`numpy.ndarray` of :obj:`~lihzahrd.terraria.world.tiles.array_dtype.TILE_DTYPE`.

        :param self: The :class:`.Tile` to convert.
        :returns: The resulting scalar :class:`numpy.ndarray`.
        """

        # noinspection PyTypeChecker
        scalar: ndarray[tuple[Literal[1]], Any] = zeros(shape=(1,), dtype=TILE_DTYPE)

        if self.block is not None:
            scalar["block_id"] = self.block.ID + 1
            scalar["block_inactive"] = self.block.is_inactive
            scalar["block_illuminant"] = self.block.is_illuminant
            scalar["block_echo"] = self.block.is_echo
            scalar["block_paint"] = self.block.paint.value
            scalar["block_shape"] = self.block.shape.value

            if self.block.u is not None:
                scalar["block_u"] = self.block.u
            if self.block.v is not None:
                scalar["block_v"] = self.block.v
        else:
            scalar["block_id"] = 0

        if self.wall is not None:
            scalar["wall_id"] = self.wall.ID + 1
            scalar["wall_illuminant"] = self.wall.is_illuminant
            scalar["wall_echo"] = self.wall.is_echo
            scalar["wall_paint"] = self.wall.paint
        else:
            scalar["wall_id"] = 0

        if self.liquid is not None:
            scalar["liquid_id"] = self.liquid.ID
            scalar["liquid_volume"] = self.liquid.volume
        else:
            scalar["liquid_id"] = 0

        scalar["wire_red"] = self.wiring.has_red
        scalar["wire_green"] = self.wiring.has_green
        scalar["wire_blue"] = self.wiring.has_blue
        scalar["wire_yellow"] = self.wiring.has_yellow
        scalar["wire_actuator"] = self.wiring.has_actuator

        return scalar

    def __array__(self, dtype=None, copy=None) -> ndarray[tuple[Literal[1]], Any]:
        """
        Allow :mod:`numpy` to treat this as an array.

        .. seealso::

            `The __array__() method on NumPy docs <https://numpy.org/doc/stable/user/basics.interoperability.html#dunder-array-interface>`_

        """
        if copy is False:
            raise ValueError("Cannot return numpy view of Tile object")
        if dtype is TILE_DTYPE:
            return self.to_scalar()
        else:
            raise TypeError("Invalid dtype requested")

    @classmethod
    def from_scalar(cls, scalar: ndarray[tuple[Literal[1]], Any], *, frame_important: WorldFrameImportant) -> Tile:
        """
        Convert a scalar :class:`numpy.ndarray` of :obj:`~lihzahrd.terraria.world.tiles.array_dtype.TILE_DTYPE` into a :class:`.Tile`.

        .. tip::

            Useful to get a :class:`.Tile` out of :class:`~lihzahrd.terraria.world.tiles.world_tiles.WorldTiles`!

        :param scalar: The scalar :class:`numpy.ndarray` of :obj:`~lihzahrd.terraria.world.tiles.array_dtype.TILE_DTYPE` to convert.
        :param frame_important: The value of :class:`~lihzahrd.terraria.world.frame_important.world_frame_important.WorldFrameImportant` to use to determine which blocks should have associated UV values, and which shouldn't.
        :return: The resulting :class:`.Tile`.
        """

        block: BlockBase | None = None
        if scalar["block_id"] != 0:
            block_id: int = (scalar["block_id"] - 1).item()
            block_class: type[BlockBase] = BlockEnum.INDEXES["ID"][block_id]

            if frame_important[block_id]:
                block_frame = (
                    scalar["block_u"].item(),
                    scalar["block_v"].item(),
                )
            else:
                block_frame = None

            block_shape = BlockShapeEnum(scalar["block_shape"].item())
            block_paint = PaintEnum(scalar["block_paint"].item())

            block_inactive = scalar["block_inactive"].item()
            block_illuminant = scalar["block_illuminant"].item()
            block_echo = scalar["block_echo"].item()

            block = block_class(
                frame=block_frame,
                shape=block_shape,
                is_inactive=block_inactive,
                paint=block_paint,
                is_illuminant=block_illuminant,
                is_echo=block_echo,
            )

        wall: WallBase | None = None
        if scalar["wall_id"] != 0:
            wall_id: int = (scalar["wall_id"] - 1).item()
            wall_class: type[WallBase] = WallEnum.INDEXES["ID"][wall_id]

            wall_paint = PaintEnum(scalar["wall_paint"].item())
            wall_illuminant = scalar["wall_illuminant"].item()
            wall_echo = scalar["wall_echo"].item()

            wall = wall_class(
                paint=wall_paint,
                is_illuminant=wall_illuminant,
                is_echo=wall_echo,
            )

        liquid: LiquidBase | None = None
        if scalar["liquid_id"] != 0:
            liquid_id: int = scalar["liquid_id"].item()
            liquid_class = LiquidEnum.INDEXES["ID"][liquid_id]

            liquid_volume = scalar["liquid_volume"].item()

            liquid = liquid_class(volume=liquid_volume)

        wiring: Wiring = Wiring(
            has_red=scalar["wiring_red"].item(),
            has_green=scalar["wiring_green"].item(),
            has_blue=scalar["wiring_blue"].item(),
            has_yellow=scalar["wiring_yellow"].item(),
            has_actuator=scalar["wiring_actuator"].item(),
        )

        return cls(
            block=block,
            wall=wall,
            liquid=liquid,
            wiring=wiring,
        )


__all__ = ("Tile",)
