from numpy import array

from lihzahrd.terraria.world.tiles.array_dtype import TILE_DTYPE
from lihzahrd.terraria.world.tiles.world_tiles import WorldTiles

a = array(
    [
        [
            # Three tiles of air
            (0, 0, 0, 0, False, 0, False, False, 0, 0, False, False, 0, 0, False, False, False, False, False),
            (0, 0, 0, 0, False, 0, False, False, 0, 0, False, False, 0, 0, False, False, False, False, False),
            (0, 0, 0, 0, False, 0, False, False, 0, 0, False, False, 0, 0, False, False, False, False, False),
        ],
        [
            # One tile of air, two tiles of glowing mushroom
            (0, 0, 0, 0, False, 0, False, False, 0, 0, False, False, 0, 0, False, False, False, False, False),
            (190, 0, 0, 0, False, 0, False, False, 0, 0, False, False, 0, 0, False, False, False, False, False),
            (190, 0, 0, 0, False, 0, False, False, 0, 0, False, False, 0, 0, False, False, False, False, False),
        ],
        [
            # One tile of air, one tile of glowing mushroom, one tile of glowing mushroom with wall
            (0, 0, 0, 0, False, 0, False, False, 0, 0, False, False, 0, 0, False, False, False, False, False),
            (190, 0, 0, 0, False, 0, False, False, 0, 0, False, False, 0, 0, False, False, False, False, False),
            (190, 0, 0, 0, False, 0, False, False, 74, 0, False, False, 0, 0, False, False, False, False, False),
        ],
    ],
    dtype=TILE_DTYPE,
)


def test_difference_matrix():
    d = WorldTiles._create_difference_matrix(a)

    # Three tiles of air
    assert d[0][0]
    assert not d[0][1]
    assert not d[0][2]

    # One tile of air, two tiles of glowing mushroom
    assert d[1][0]
    assert d[1][1]
    assert not d[1][2]

    # One tile of air, one tile of glowing mushroom, one tile of glowing mushroom with wall
    assert d[2][0]
    assert d[2][1]
    assert d[2][2]


def test_tile_batches():
    t = WorldTiles._create_tile_batches(a)

    # Three tiles of air
    assert t[0][1] == 3

    # One tile of air, two tiles of glowing mushroom
    assert t[1][1] == 1
    assert t[2][1] == 2

    # One tile of air, one tile of glowing mushroom, one tile of glowing mushroom with wall
    assert t[3][1] == 1
    assert t[4][1] == 1
    assert t[5][1] == 1
