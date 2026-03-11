# language=rst
"""
Submodule containing :class:`.WorldSections`.
"""

from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class WorldSections(PackPrimitive[list[int]]):
    """
    :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` representing a fixed-length :class:`list` of addresses of the start of the various regions of a Terraria world save file.
    """

    _LOG = getLogger(__name__)

    class UnexpectedSectionCountError(PackPrimitive[list[int]].ValidationError, OverflowError):
        """
        There is a different amount of section than there usually are in a Terraria world save file.
        """

    class AddressOverflowError(PackPrimitive[list[int]].ValidationError, OverflowError):
        """
        An address is not within the representable range.
        """

    @property
    def file_metadata(self) -> int:
        """
        The pointer to the file metadata section, which is always ``0``.
        """

        return 0

    @property
    def header(self) -> int:
        """
        The pointer to the world metadata section.
        """
        return self.value[0]

    @header.setter
    def header(self, value: int) -> None:
        self.value[0] = value

    @property
    def tiles(self) -> int:
        """
        The pointer to the tiles section.
        """
        return self.value[1]

    @tiles.setter
    def tiles(self, value: int) -> None:
        self.value[1] = value

    @property
    def chests(self) -> int:
        """
        The pointer to the chests section.
        """
        return self.value[2]

    @chests.setter
    def chests(self, value: int) -> None:
        self.value[2] = value

    @property
    def signs(self) -> int:
        """
        The pointer to the signs section.
        """
        return self.value[3]

    @signs.setter
    def signs(self, value: int) -> None:
        self.value[3] = value

    @property
    def npcs(self) -> int:
        """
        The pointer to the NPCs section.
        """
        return self.value[4]

    @npcs.setter
    def npcs(self, value: int) -> None:
        self.value[4] = value

    @property
    def tile_entities(self) -> int:
        """
        The pointer to the tile entities section.
        """
        return self.value[5]

    @tile_entities.setter
    def tile_entities(self, value: int) -> None:
        self.value[5] = value

    @property
    def pressure_plates(self) -> int:
        """
        The pointer to the pressure plates section.
        """
        return self.value[6]

    @pressure_plates.setter
    def pressure_plates(self, value: int) -> None:
        self.value[6] = value

    @property
    def rooms(self) -> int:
        """
        The pointer to the rooms section.
        """
        return self.value[7]

    @rooms.setter
    def rooms(self, value: int) -> None:
        self.value[7] = value

    @property
    def bestiary(self) -> int:
        """
        The pointer to the bestiary section.
        """
        return self.value[8]

    @bestiary.setter
    def bestiary(self, value: int) -> None:
        self.value[8] = value

    @property
    def journey(self) -> int:
        """
        The pointer to the journey section.
        """
        return self.value[9]

    @journey.setter
    def journey(self, value: int) -> None:
        self.value[9] = value

    @property
    def footer(self) -> int:
        """
        The pointer to the checksum section.
        """
        return self.value[-1]

    @footer.setter
    def footer(self, value: int) -> None:
        self.value[-1] = value

    def __str__(self) -> str:
        """
        :return: A debugging :class:`str` describing name and offsets of each section.
        """
        file_metadata = self.file_metadata
        header = self.header
        tiles = self.tiles
        chests = self.chests
        signs = self.signs
        npcs = self.npcs
        tile_entities = self.tile_entities
        pressure_plates = self.pressure_plates
        rooms = self.rooms
        bestiary = self.bestiary
        journey = self.journey
        footer = self.footer
        return (
            f"{file_metadata = } | "
            f"{header = } | "
            f"{tiles = } | "
            f"{chests = } | "
            f"{signs = } | "
            f"{npcs = } | "
            f"{tile_entities = } | "
            f"{pressure_plates = } | "
            f"{rooms = } | "
            f"{bestiary = } | "
            f"{journey = } | "
            f"{footer = }"
        )

    @classmethod
    @override
    def _validate(cls, value: list[int], **kwargs) -> None:
        if len(value) != 11:
            raise cls.UnexpectedSectionCountError(value)

        for item in value:
            if not FileProcessor.INT_MIN <= item <= FileProcessor.INT_MAX:
                raise cls.AddressOverflowError(value)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs) -> list[int]:
        count = fp.read_short()
        value: list[int] = []

        for _ in range(count):
            item = fp.read_int()
            value.append(item)

        return value

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: list[int], **kwargs) -> None:
        count = len(value)

        fp.write_short(count)
        for item in value:
            fp.write_int(item)


__all__ = ("WorldSections",)
