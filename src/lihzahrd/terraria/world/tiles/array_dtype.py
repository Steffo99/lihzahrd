# language=rst
"""
Submodule containing :obj:`TILE_DTYPE`.
"""

from numpy import dtype

TILE_DTYPE = dtype(
    [
        ("block_id", "u2"),
        ("block_u", "u2"),
        ("block_v", "u2"),
        ("block_shape", "u1"),
        ("block_inactive", "?"),
        ("block_paint", "u1"),
        ("block_illuminant", "?"),
        ("block_echo", "?"),
        ("wall_id", "u2"),
        ("wall_paint", "u1"),
        ("wall_illuminant", "?"),
        ("wall_echo", "?"),
        ("liquid_id", "u1"),
        ("liquid_volume", "u1"),
        ("wire_red", "?"),
        ("wire_green", "?"),
        ("wire_blue", "?"),
        ("wire_yellow", "?"),
        ("wire_actuator", "?"),
    ]
)
"""
The :class:`numpy.dtype` with which :class:`~lihzahrd.terraria.world.tiles.world_tiles.WorldTiles` stores tiles.

The fields ``block_id`` and ``wall_id`` are special:

- if their value is ``0``, it means that the tile has no block or wall present
- if their value is ``1`` or more, if means that a block or wall is present, and that its ID is the value, **minus one**.
"""

__all__ = ("TILE_DTYPE",)
