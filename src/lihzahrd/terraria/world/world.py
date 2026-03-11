# language=rst
"""
Submodule containing the class :class:`.PackWorld` itself.
"""

from logging import getLogger
from typing import Any, Self, override

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.common.file_metadata import FileMetadata
from lihzahrd.terraria.utils.pack.pack import Pack, PackRead, PackWrite
from lihzahrd.terraria.utils.pack.primitive.bytes import PackUnknown
from lihzahrd.terraria.world.bestiary.bestiary import Bestiary
from lihzahrd.terraria.world.characters.world_characters import WorldCharacters
from lihzahrd.terraria.world.chests.world_chests_collection import WorldChestsCollection
from lihzahrd.terraria.world.footer.world_footer import WorldFooter
from lihzahrd.terraria.world.frame_important.world_frame_important import WorldFrameImportant
from lihzahrd.terraria.world.header.world_header import WorldHeader
from lihzahrd.terraria.world.journey.journey_settings_collection import JourneySettingsCollection
from lihzahrd.terraria.world.pressure_plates.world_weighted_pressure_plates_collection import (
    WorldWeightedPressurePlatesCollection,
)
from lihzahrd.terraria.world.rooms.rooms_collection import RoomsCollection
from lihzahrd.terraria.world.sections.world_sections import WorldSections
from lihzahrd.terraria.world.signs.world_signs_collection import WorldSignsCollection
from lihzahrd.terraria.world.tile_entities.tile_entities_collection import TileEntitiesCollection
from lihzahrd.terraria.world.tiles.world_tiles import WorldTiles


class PackWorld(Pack):
    """
    :class:`~lihzahrd.terraria.utils.pack.pack.Pack` which represents a Terraria world save file in its totality.

    World save files are split in sections; this class represents each section with a separate :class:`~lihzahrd.terraria.utils.pack.pack.Pack`.

    .. warning::

        Very, **very** slow to :attr:`~lihzahrd.terraria.utils.pack.pack.Pack.read` and :attr:`~lihzahrd.terraria.utils.pack.pack.Pack.write` because of the compression Terraria uses to store :attr:`.tiles`.

    .. danger::

        **Denial-of-service vector**: Maliciously structured world files may cause :attr:`~lihzahrd.terraria.utils.pack.pack.Pack.read` and :attr:`~lihzahrd.terraria.utils.pack.pack.Pack.write` to block for a very, very long time. Only load world files you trust!

    :kwarg debug_skip_tiles: Skip reading or writing :attr:`.tiles`, and read the whole section to :attr:`.unknown_tiles_bytes` instead.
    :kwarg tile_cache_path: Instead of reading :attr:`.tiles`, if a file at the given path exists, load them from there, and read the section to :attr:`.unknown_tiles_bytes` instead. Otherwise, read :attr:`.tiles` as normal, but additionally save the read data in an efficient (but large) format as a file at the given path.
    """

    _LOG = getLogger(__name__)

    @override
    def __init__(
        self,
        file_metadata: FileMetadata,
        section_addresses: WorldSections,
        frame_important: WorldFrameImportant,
        unknown_file_metadata_bytes: PackUnknown,
        header: WorldHeader,
        unknown_header_bytes: PackUnknown,
        tiles: WorldTiles,
        unknown_tiles_bytes: PackUnknown,
        chests: WorldChestsCollection,
        unknown_chests_bytes: PackUnknown,
        signs: WorldSignsCollection,
        unknown_signs_bytes: PackUnknown,
        characters: WorldCharacters,
        unknown_npcs_bytes: PackUnknown,
        tile_entities: TileEntitiesCollection,
        unknown_tile_entities_bytes: PackUnknown,
        pressure_plates: WorldWeightedPressurePlatesCollection,
        unknown_pressure_plates_bytes: PackUnknown,
        rooms: RoomsCollection,
        unknown_rooms_bytes: PackUnknown,
        bestiary: Bestiary,
        unknown_bestiary_bytes: PackUnknown,
        journey: JourneySettingsCollection,
        unknown_journey_bytes: PackUnknown,
        footer: WorldFooter,
        unknown_footer_bytes: PackUnknown,
    ):
        self.file_metadata: FileMetadata = file_metadata
        """
        The file metadata header, stopping right before the list of pointers to the various sections.
        """

        self.sections: WorldSections = section_addresses
        """
        Pointers to the byte offsets where the various sections of the save file start.
        
        .. warning::
            
            Automatically overwritten with the correct values once :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.write` is called.
        
        """

        self.frame_important: WorldFrameImportant = frame_important
        """
        Array describing which block IDs have been written as :term:`FrameImportant`.
        """

        self.unknown_file_metadata_bytes: PackUnknown = unknown_file_metadata_bytes
        """
        Bytes between :attr:`.frame_important` and :attr:`.header`.        
        """

        self.header: WorldHeader = header
        """
        The world metadata header.
        
        Contains most important information about the game's progress, like which NPCs have been rescued and which bosses have been defeated.
        """

        self.unknown_header_bytes: PackUnknown = unknown_header_bytes
        """
        Bytes between :attr:`.header` and :attr:`.tiles`.
        """

        self.tiles: WorldTiles = tiles
        """
        The world's tile matrix.
        """

        self.unknown_tiles_bytes: PackUnknown = unknown_tiles_bytes
        """
        Bytes between :attr:`.tiles` and :attr:`.chests`.
        """

        self.chests: WorldChestsCollection = chests
        """
        Collection of all the chests in the world and their contents.
        """

        self.unknown_chests_bytes: PackUnknown = unknown_chests_bytes
        """
        Bytes between :attr:`.chests` and :attr:`.signs`.
        """

        self.signs: WorldSignsCollection = signs
        """
        Collection of all the signs in the world and their text.
        """

        self.unknown_signs_bytes: PackUnknown = unknown_signs_bytes
        """
        Bytes between :attr:`.signs` and :attr:`.characters`.
        """

        self.characters: WorldCharacters = characters
        """
        Collection of all the characters (monsters, critters, and NPCs) in the world and their locations.
        """

        self.unknown_characters_bytes: PackUnknown = unknown_npcs_bytes
        """
        Bytes between :attr:`.characters` and :attr:`.tile_entities`.
        """

        self.tile_entities: TileEntitiesCollection = tile_entities
        """
        Collection of all the tile entities (mannequins, hat racks, ...) in the world and their locations and metadata.
        """

        self.unknown_tile_entities_bytes: PackUnknown = unknown_tile_entities_bytes
        """
        Bytes between :attr:`.tile_entities` and :attr:`.pressure_plates`.
        """

        self.pressure_plates: WorldWeightedPressurePlatesCollection = pressure_plates
        """
        Collection of all the weighted pressure plates in the world and their positions.
        """

        self.unknown_pressure_plates_bytes: PackUnknown = unknown_pressure_plates_bytes
        """
        Bytes between :attr:`.pressure_plates` and :attr:`.rooms`.
        """

        self.rooms: RoomsCollection = rooms
        """
        Collection of all the assignments of rooms to NPCs.
        """

        self.unknown_rooms_bytes: PackUnknown = unknown_rooms_bytes
        """
        Bytes between :attr:`.rooms` and :attr:`.bestiary`.
        """

        self.bestiary: Bestiary = bestiary
        """
        Status of the bestiary in the world.
        """

        self.unknown_bestiary_bytes: PackUnknown = unknown_bestiary_bytes
        """
        Bytes between :attr:`.bestiary` and :attr:`.journey`.
        """

        self.journey: JourneySettingsCollection = journey
        """
        Current configuration of Journey mode powers.
        """

        self.unknown_journey_bytes: PackUnknown = unknown_journey_bytes
        """
        Bytes between :attr:`.journey` and :attr:`.footer`.
        """

        self.footer: WorldFooter = footer
        """
        Extra validation data for the world.
        """

        self.unknown_footer_bytes: PackUnknown = unknown_footer_bytes
        """
        Bytes after :attr:`.footer`, but before the end of the file.
        """

    @override
    def validate(self, *, strict: bool = True, **kwargs: Any) -> bool:
        valid = True

        valid &= self.file_metadata.validate(strict=strict)
        valid &= self.sections.validate(strict=strict)
        valid &= self.frame_important.validate(strict=strict)
        valid &= self.unknown_file_metadata_bytes.validate(strict=strict)
        valid &= self.header.validate(strict=strict)
        valid &= self.unknown_header_bytes.validate(strict=strict)
        valid &= self.tiles.validate(strict=strict)
        valid &= self.unknown_tiles_bytes.validate(strict=strict)
        valid &= self.chests.validate(strict=strict)
        valid &= self.unknown_chests_bytes.validate(strict=strict)
        valid &= self.signs.validate(strict=strict)
        valid &= self.unknown_signs_bytes.validate(strict=strict)
        valid &= self.characters.validate(strict=strict)
        valid &= self.unknown_characters_bytes.validate(strict=strict)
        valid &= self.tile_entities.validate(strict=strict)
        valid &= self.unknown_tile_entities_bytes.validate(strict=strict)
        valid &= self.pressure_plates.validate(strict=strict)
        valid &= self.unknown_pressure_plates_bytes.validate(strict=strict)
        valid &= self.rooms.validate(strict=strict)
        valid &= self.unknown_rooms_bytes.validate(strict=strict)
        valid &= self.bestiary.validate(strict=strict)
        valid &= self.unknown_bestiary_bytes.validate(strict=strict)
        valid &= self.journey.validate(strict=strict)
        valid &= self.unknown_journey_bytes.validate(strict=strict)
        valid &= self.footer.validate(strict=strict)
        valid &= self.unknown_footer_bytes.validate(strict=strict)

        valid &= self.header.name == self.footer.name
        valid &= self.header.id == self.footer.id

        return valid

    @classmethod
    @override
    def read(cls, fp: FileProcessor, *, strict: bool = True, **kwargs: Any) -> PackRead[Self]:
        debug_skip_tiles = kwargs.get("debug_skip_tiles", False)
        tile_cache_path = kwargs.get("tile_cache_path")

        valid = True

        def __unwrap[T](prr: PackRead[T]) -> T:
            cls._LOG.info("Read section: %s", prr)
            nonlocal valid
            valid &= prr.valid
            return prr.instance

        file_metadata = __unwrap(FileMetadata.read(fp, strict=strict))
        sections = __unwrap(WorldSections.read(fp, strict=strict))
        frame_important = __unwrap(WorldFrameImportant.read(fp, strict=strict))
        unknown_file_metadata_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=sections.header))
        header = __unwrap(WorldHeader.read(fp, strict=strict))
        unknown_header_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=sections.tiles))
        if not debug_skip_tiles:
            tiles = __unwrap(
                WorldTiles.read(
                    fp, strict=strict, size=header.size, frame_important=frame_important, cache_path=tile_cache_path
                )
            )
        else:
            tiles = None
        unknown_tiles_bytes = __unwrap(
            PackUnknown.read(
                fp, strict=strict, until=sections.chests, acceptable=tile_cache_path is not None or debug_skip_tiles
            )
        )
        chests = __unwrap(WorldChestsCollection.read(fp, strict=strict))
        unknown_chests_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=sections.signs))
        signs = __unwrap(WorldSignsCollection.read(fp, strict=strict))
        unknown_signs_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=sections.npcs))
        npcs = __unwrap(WorldCharacters.read(fp, strict=strict))
        unknown_npcs_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=sections.tile_entities))
        tile_entities = __unwrap(TileEntitiesCollection.read(fp, strict=strict))
        unknown_tile_entities_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=sections.pressure_plates))
        pressure_plates = __unwrap(WorldWeightedPressurePlatesCollection.read(fp, strict=strict))
        unknown_pressure_plates_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=sections.rooms))
        rooms = __unwrap(RoomsCollection.read(fp, strict=strict))
        unknown_rooms_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=sections.bestiary))
        bestiary = __unwrap(Bestiary.read(fp, strict=strict))
        unknown_bestiary_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=sections.journey))
        journey = __unwrap(JourneySettingsCollection.read(fp, strict=strict))
        unknown_journey_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=sections.footer))
        footer = __unwrap(WorldFooter.read(fp, strict=strict))
        unknown_footer_bytes = __unwrap(PackUnknown.read(fp, strict=strict, until=None))

        instance = cls(
            file_metadata=file_metadata,
            section_addresses=sections,
            frame_important=frame_important,
            unknown_file_metadata_bytes=unknown_file_metadata_bytes,
            header=header,
            unknown_header_bytes=unknown_header_bytes,
            tiles=tiles,
            unknown_tiles_bytes=unknown_tiles_bytes,
            chests=chests,
            unknown_chests_bytes=unknown_chests_bytes,
            signs=signs,
            unknown_signs_bytes=unknown_signs_bytes,
            characters=npcs,
            unknown_npcs_bytes=unknown_npcs_bytes,
            tile_entities=tile_entities,
            unknown_tile_entities_bytes=unknown_tile_entities_bytes,
            pressure_plates=pressure_plates,
            unknown_pressure_plates_bytes=unknown_pressure_plates_bytes,
            rooms=rooms,
            unknown_rooms_bytes=unknown_rooms_bytes,
            bestiary=bestiary,
            unknown_bestiary_bytes=unknown_bestiary_bytes,
            journey=journey,
            unknown_journey_bytes=unknown_journey_bytes,
            footer=footer,
            unknown_footer_bytes=unknown_footer_bytes,
        )

        return PackRead(instance=instance, valid=valid)

    @override
    def write(self, fp: FileProcessor, *, strict: bool = True, **kwargs: Any) -> PackWrite[Self]:
        debug_skip_tiles = kwargs.get("debug_skip_tiles", False)

        valid = True

        def __unwrap[T](prw: PackWrite[T]) -> T:
            self._LOG.info("Written section: %s", prw)
            nonlocal valid
            valid &= prw.valid

        sections_start = str(self.sections)

        __unwrap(self.file_metadata.write(fp, strict=strict))

        sections_section = fp.stream.tell()
        __unwrap(self.sections.write(fp, strict=strict))

        __unwrap(self.frame_important.write(fp, strict=strict))
        __unwrap(self.unknown_file_metadata_bytes.write(fp, strict=strict))

        self.sections.header = fp.stream.tell()
        __unwrap(self.header.write(fp, strict=strict))
        __unwrap(self.unknown_header_bytes.write(fp, strict=strict))

        self.sections.tiles = fp.stream.tell()
        if self.tiles is not None and not debug_skip_tiles:
            __unwrap(self.tiles.write(fp, strict=strict, frame_important=self.frame_important, size=self.header.size))
        __unwrap(self.unknown_tiles_bytes.write(fp, strict=strict, acceptable=debug_skip_tiles))

        self.sections.chests = fp.stream.tell()
        __unwrap(self.chests.write(fp, strict=strict))
        __unwrap(self.unknown_chests_bytes.write(fp, strict=strict))

        self.sections.signs = fp.stream.tell()
        __unwrap(self.signs.write(fp, strict=strict))
        __unwrap(self.unknown_signs_bytes.write(fp, strict=strict))

        self.sections.npcs = fp.stream.tell()
        __unwrap(self.characters.write(fp, strict=strict))
        __unwrap(self.unknown_characters_bytes.write(fp, strict=strict))

        self.sections.tile_entities = fp.stream.tell()
        __unwrap(self.tile_entities.write(fp, strict=strict))
        __unwrap(self.unknown_tile_entities_bytes.write(fp, strict=strict))

        self.sections.pressure_plates = fp.stream.tell()
        __unwrap(self.pressure_plates.write(fp, strict=strict))
        __unwrap(self.unknown_pressure_plates_bytes.write(fp, strict=strict))

        self.sections.rooms = fp.stream.tell()
        __unwrap(self.rooms.write(fp, strict=strict))
        __unwrap(self.unknown_rooms_bytes.write(fp, strict=strict))

        self.sections.bestiary = fp.stream.tell()
        __unwrap(self.bestiary.write(fp, strict=strict))
        __unwrap(self.unknown_bestiary_bytes.write(fp, strict=strict))

        self.sections.journey = fp.stream.tell()
        __unwrap(self.journey.write(fp, strict=strict))
        __unwrap(self.unknown_journey_bytes.write(fp, strict=strict))

        self.sections.footer = fp.stream.tell()
        __unwrap(self.footer.write(fp, strict=strict))
        __unwrap(self.unknown_footer_bytes.write(fp, strict=strict))

        fp.stream.seek(sections_section)
        __unwrap(self.sections.write(fp, strict=strict))

        sections_end = str(self.sections)

        if sections_start != sections_end:
            self._LOG.debug(
                "Written sections do not match initial sections; world may have changed:\n%s\n%s",
                sections_start,
                sections_end,
            )

        return PackWrite(valid=valid)


__all__ = ("PackWorld",)
