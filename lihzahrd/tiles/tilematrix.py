import typing
from .tile import Tile
from ..fileutils import FileReader, Coordinates


class TileMatrix:
    """A huge matrix containing the tiles of a whole world."""

    def __init__(self, width: int, height: int):
        self._stride = [
            x * height for x in range(width)
        ]
        self._width = width
        self._height = height
        self._tiles: typing.List[typing.List[Tile]] = [Tile()] * (width * height)

    def __repr__(self):
        return f"<TileMatrix {self._width}x{self._height}>"

    def __getitem__(self, item: typing.Union[typing.Tuple, Coordinates]):
        """Get a tile at specific coordinates.

        (x=0, y=0) returns the top-left tile in the map.

        You can specify a negative coordinate to count tiles respectively from the right or from the bottom:
        (x=-1, y=-1) returns the bottom-right tile in the map."""
        if isinstance(item, Coordinates):
            return self._tiles[self._stride[item.x] + item.y]
        elif isinstance(item, tuple):
            return self._tiles[self._stride[item[0]] + item[1]]
        else:
            raise TypeError(f"Unsupported type: {item.__class__.__name__}")

    def __setitem__(self, key: typing.Union[typing.Tuple, Coordinates], value: Tile):
        """Change a tile at specific coordinates.

        The same properties that apply to __getitem__ are valid for __setitem__."""
        if not isinstance(value, Tile):
            raise TypeError(f"Invalid type: {value.__class__.__name__} instead of Tile")
        if isinstance(key, Coordinates):
            self._tiles[self._stride[key.x] + key.y] = value
        elif isinstance(key, tuple):
            self._tiles[self._stride[key[0]] + key[1]] = value
        else:
            raise TypeError(f"Invalid type: {key.__class__.__name__} instead of tuple or Coordinates")

    def __len__(self):
        """Return the amount of tiles present in the matrix."""
        return len(self._tiles)

    def fill(self, tiles: typing.Iterable[Tile]):
        "Fill all the tile matrix using an iterable"
        for pos, tile in enumerate(tiles):
            self._tiles[pos] = tile

    @property
    def size(self) -> Coordinates:
        """Return the size of the matrix as a pair of coordinates."""
        return Coordinates(self._width, self._height)
