import typing


class Pointers:
    __slots__ = (
        "file_format",
        "world_header",
        "world_tiles",
        "chests",
        "signs",
        "npcs",
        "tile_entities",
        "pressure_plates",
        "town_manager",
        "bestiary",
        "journey_powers",
        "footer",
        "unknown",
    )

    def __init__(self,
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
                 *unknown):
        self.file_format: int = 0
        self.world_header: int = world_header
        self.world_tiles: int = world_tiles
        self.chests: int = chests
        self.signs: int = signs
        self.npcs: int = npcs
        self.tile_entities: int = tile_entities
        self.pressure_plates: int = pressure_plates
        self.town_manager: int = town_manager
        self.bestiary: int = bestiary
        self.journey_powers: int = journey_powers
        self.footer: int = footer
        self.unknown: typing.List[int] = list(unknown)
