import typing
from .tile import Tile
from ..fileutils import Coordinates


class TileMatrix:
    """A huge matrix containing the tiles of a whole world."""

    __slots__ = "_tiles"

    def __init__(self):
        self._tiles: typing.List[typing.List[Tile]] = []

    def __repr__(self):
        if len(self._tiles) > 0:
            return f"<TileMatrix {len(self._tiles)}x{len(self._tiles[0])}>"
        return f"<TileMatrix 0x0>"

    def __getitem__(self, item: typing.Union[typing.Tuple, Coordinates]):
        """Get a tile at specific coordinates.

        (x=0, y=0) returns the top-left tile in the map.

        You can specify a negative coordinate to count tiles respectively from the right or from the bottom:
        (x=-1, y=-1) returns the bottom-right tile in the map."""
        if isinstance(item, Coordinates):
            return self._tiles[item.x][item.y]
        elif isinstance(item, tuple):
            return self._tiles[item[0]][item[1]]
        else:
            raise TypeError(f"Unsupported type: {item.__class__.__name__}")

    def __setitem__(self, key: typing.Union[typing.Tuple, Coordinates], value: Tile):
        """Change a tile at specific coordinates.

        The same properties that apply to __getitem__ are valid for __setitem__."""
        if not isinstance(value, Tile):
            raise TypeError(f"Invalid type: {value.__class__.__name__} instead of Tile")
        if isinstance(key, Coordinates):
            self._tiles[key.x][key.y] = value
        elif isinstance(key, tuple):
            self._tiles[key[0]][key[1]] = value
        else:
            raise TypeError(f"Invalid type: {key.__class__.__name__} instead of tuple or Coordinates")

    def __len__(self):
        """Return the amount of tiles present in the matrix."""
        if len(self._tiles) > 0:
            return len(self._tiles) * len(self._tiles[0])
        return 0

    def add_column(self, column: typing.List[Tile]):
        """Add a new column to the matrix."""
        if len(self._tiles) > 0 and len(column) != len(self._tiles[0]):
            raise ValueError("column has a different length than the others in the matrix")
        self._tiles.append(column)

    @property
    def size(self) -> Coordinates:
        """Return the size of the matrix as a pair of coordinates."""
        if len(self._tiles) > 0:
            return Coordinates(len(self._tiles), len(self._tiles[0]))
        return Coordinates(0, 0)
