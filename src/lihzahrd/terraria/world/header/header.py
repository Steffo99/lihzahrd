from typing import Self
from uuid import UUID

from .challenges import Challenges
from .generator import Generator
from ..version import Version
from ..worldversionedpackable import WorldVersionedPackable
from ...utils import FilePacker, Rect, Coordinates


class Header(WorldVersionedPackable):
    def __init__(
            self,
            name_: str,
            generator_: Generator,
            uuid_: UUID,
            id_: int,
            bounds_: Rect,
            size_: Coordinates,
            challenges_: Challenges,
            createdon_: bytearray,
            # styles_: Styles,
            # spawn_: Coordinates,
            # undergroundheight_: float,
            # cavernheight_: float,
            # time_: Time,  # TODO: Not packable, add bloodmoon and eclipse
            # dungeon_: Coordinates,
            # evil_: Evil,
            # bosses_: BossesDefeated,  # TODO: Not packable
            # npcs_: SavedNPCs,  # TODO: Mixed with bosses_
            # shadoworbs_: ShadowOrbs,  # TODO: Merge with Evil?
            # altarssmashed_: int,  # TODO: Merge with Evil?
            # hardmode_: bool,  # TODO: Merge with Evil into Progression?
            # partydoom_: bool,  # TODO: ugh
            # invasion: Invasion,
    ):
        self.name: str = name_
        """The name the world was given at creation. Doesn't always match the filename."""

        self.generator: Generator = generator_
        """Information about the generation of this world."""

        self.uuid: UUID = uuid_
        """The Universally Unique ID of this world."""

        self.id: int = id_
        """The world id. Used to name the minimap file."""

        self.bounds: Rect = bounds_
        """The world size in pixels."""

        self.size: Coordinates = size_
        """The world size in tiles."""

        self.challenges: Challenges = challenges_
        """The challenges selected for the world, like the difficulty, or the custom seeds."""

        self.created_on: bytearray = createdon_
        """The timestamp on which the world was created."""

    def serialize(self, f: FilePacker, v: Version):
        f.write_string_variable(self.name)
        self.generator.serialize(f, v=v)
        f.write_uuid(self.uuid)
        f.write_int4(self.id)
        f.write_rect(self.bounds)
        f.write_int4(self.size.x), f.write_int4(self.size.y)
        self.challenges.serialize(f, v=v)
        f.write_datetime(self.created_on)

    @classmethod
    def deserialize(cls, f: FilePacker, v: Version) -> Self:
        name_ = f.read_string_variable()
        generator_ = Generator.deserialize(f, v=v)
        uuid_ = f.read_uuid()
        id_ = f.read_int4()
        bounds_ = f.read_rect()
        size_ = Coordinates(x=f.read_int4(), y=f.read_int4())
        challenges_ = Challenges.deserialize(f, v=v)
        createdon_ = f.read_datetime()
        return cls(
            name_=name_,
            generator_=generator_,
            uuid_=uuid_,
            id_=id_,
            bounds_=bounds_,
            size_=size_,
            challenges_=challenges_,
            createdon_=createdon_,
        )


__all__ = (
    "Header",
)
