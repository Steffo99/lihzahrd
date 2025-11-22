from typing import Self

from .version import Version
from .worldversionedpackable import WorldVersionedPackable
from ..utils import FilePacker


class Pointers(WorldVersionedPackable):
    """
    Pointers to the various sections of a Terraria world save file.

    All values are in number of bytes from the start.
    """

    __slots__ = (
        "file_format",
        "header",
        "tiles",
        "chests",
        "signs",
        "npcs",
        "tile_entities",
        "pressure_plates",
        "town_manager",
        "bestiary",
        "journey_powers",
        "footer",
    )

    meta: int = 0
    """
    Meta section is always at byte 0 in all worlds, and cannot be changed.
    """

    def __init__(
            self,
            world_header: int,
            world_tiles: int,
            chests: int,
            signs: int,
            npcs: int,
            tile_entities: int,
            pressure_plates: int,
            town_manager: int,
            bestiary: int,
            journey_powers: int,
            footer: int,
            *unknown,
    ):
        self.header: int = world_header
        self.tiles: int = world_tiles
        self.chests: int = chests
        self.signs: int = signs
        self.npcs: int = npcs
        self.tile_entities: int = tile_entities
        self.pressure_plates: int = pressure_plates
        self.town_manager: int = town_manager
        self.bestiary: int = bestiary
        self.journey_powers: int = journey_powers
        self.footer: int = footer
        self.unknown: list[int] = list(unknown)

    def serialize(self, f: FilePacker, *, v: Version) -> None:
        count = 11 + len(self.unknown)
        f.write_int2(count)

        f.write_int4(self.header)
        f.write_int4(self.tiles)
        f.write_int4(self.chests)
        f.write_int4(self.signs)
        f.write_int4(self.npcs)
        f.write_int4(self.tile_entities)
        f.write_int4(self.pressure_plates)
        f.write_int4(self.town_manager)
        f.write_int4(self.bestiary)
        f.write_int4(self.journey_powers)
        f.write_int4(self.footer)

        for unknown in self.unknown:
            f.write_uint4(unknown)

    @classmethod
    def deserialize(cls, f: FilePacker, *, v: Version) -> Self:
        pointers = []

        count = f.read_int2()
        for _ in range(count):
            pointers.append(f.read_int4())

        return cls(*pointers)


__all__ = (
    "Pointers",
)