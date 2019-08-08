import math
import struct
import uuid
import enum
import datetime
import typing


class Rect:
    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def __repr__(self):
        return f"Rect(left={self.left}, right={self.right}, top={self.top}, bottom={self.bottom})"


class FileReader:
    def __init__(self, file):
        self.file = file

    def bool(self):
        return struct.unpack("?", self.file.read(1))[0]

    def int1(self):
        return struct.unpack("B", self.file.read(1))[0]

    def uint1(self):
        return struct.unpack("B", self.file.read(1))[0]

    def int2(self):
        return struct.unpack("h", self.file.read(2))[0]

    def uint2(self):
        return struct.unpack("H", self.file.read(2))[0]

    def int4(self):
        return struct.unpack("i", self.file.read(4))[0]

    def uint4(self):
        return struct.unpack("I", self.file.read(4))[0]

    def int8(self):
        return struct.unpack("q", self.file.read(8))[0]

    def uint8(self):
        return struct.unpack("Q", self.file.read(8))[0]

    def single(self):
        return struct.unpack("f", self.file.read(4))[0]

    def double(self):
        return struct.unpack("d", self.file.read(8))[0]

    def bit(self):
        data = struct.unpack("B", self.file.read(1))[0]
        return (bool(data & 0b1000_0000),
                bool(data & 0b0100_0000),
                bool(data & 0b0010_0000),
                bool(data & 0b0001_0000),
                bool(data & 0b0000_1000),
                bool(data & 0b0000_0100),
                bool(data & 0b0000_0010),
                bool(data & 0b0000_0001))

    def rect(self):
        left, right, top, bottom = struct.unpack("iiii", self.file.read(16))
        return Rect(left, right, top, bottom)

    def string(self, size=None):
        if size is None:
            size = self.uint1()
        return str(self.file.read(size), encoding="latin1")

    def uuid(self):
        # TODO: convert to uuid
        # https://docs.microsoft.com/en-us/dotnet/api/system.guid.tobytearray?view=netframework-4.8
        uuid_bytes = self.file.read(16)
        return uuid_bytes

    def datetime(self):
        # TODO: convert to datetime
        # https://docs.microsoft.com/it-it/dotnet/api/system.datetime.kind?view=netframework-4.8#System_DateTime_Kind
        datetime_bytes = self.file.read(8)
        return datetime_bytes


class Version:
    """A Terraria version."""

    _version_ids = {
        71: "1.2.0.3.1",
        77: "1.2.2",
        104: "1.2.3",
        140: "1.3.0.1",
        151: "1.3.0.4",
        153: "1.3.0.5",
        154: "1.3.0.6",
        155: "1.3.0.7",
        156: "1.3.0.8",
        170: "1.3.2",
        174: "1.3.3",
        178: "1.3.4",
        194: "1.3.5.3"
    }

    def __init__(self, data: typing.Union[int, str]):
        if isinstance(data, int):
            self.id = data
        else:
            for version in self._version_ids:
                if self._version_ids[version] == data:
                    self.id = version
                    break
            else:
                raise ValueError("No such version")

    @property
    def name(self):
        # TODO: Add all versions
        try:
            return self._version_ids[self.id]
        except KeyError:
            return "Unknown"

    def __repr__(self):
        return f"Version({self.id})"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other

    def __gt__(self, other):
        return self.id > other

    def __lt__(self, other):
        return self.id < other


class GeneratorInfo:
    """Information about the world generator."""

    def __init__(self, seed, version):
        self.seed = seed
        """The seed this world was generated with."""

        self.version = version
        """The version of the generator that created this world."""


class Coordinates:
    """A pair of coordinates."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coordinates({self.x}, {self.y})"

    def __str__(self):
        return f"{self.x}, {self.y}"


class MoonStyle(enum.IntEnum):
    """All possible moon styles."""
    WHITE = 0
    ORANGE = 1
    RINGED_GREEN = 2

    def __repr__(self):
        return f"MoonStyle({self.value})"


class FourPartSplit:
    """A world property split in four parts, separated by three vertical lines at a certain x coordinate."""
    def __init__(self, separators: typing.List[int], properties: typing.List):
        self.separators: typing.List[int] = separators
        """The three x coordinates of the vertical separators, in increasing order."""

        self.properties: typing.List = properties
        """The four properties, in order:
        
        - The far left property, the one between the left world edge and the first separator.
        - The nearby left property, between the first and the second separator.
        - The nearby right property, between the second and the third separator.
        - The far right property, between the third separator and the right world edge."""

    def __repr__(self):
        return f"FourPartSplit({repr(self.separators)}, {repr(self.properties)})"

    def __str__(self):
        return f"{self.far_left} [{self.separators[0]}] {self.nearby_left} [{self.separators[1]}] {self.nearby_right} [{self.separators[2]}] {self.far_right}"

    def get_property_at_x(self, x: int):
        if x < self.separators[0]:
            return self.properties[0]
        elif x < self.separators[1]:
            return self.properties[1]
        elif x < self.separators[2]:
            return self.properties[2]
        else:
            return self.properties[3]

    @property
    def far_left(self):
        return self.properties[0]

    @far_left.setter
    def far_left(self, value):
        self.properties[0] = value

    @property
    def nearby_left(self):
        return self.properties[1]

    @nearby_left.setter
    def nearby_left(self, value):
        self.properties[1] = value

    @property
    def nearby_right(self):
        return self.properties[2]

    @nearby_right.setter
    def nearby_right(self, value):
        self.properties[2] = value

    @property
    def far_right(self):
        return self.properties[2]

    @far_right.setter
    def far_right(self, value):
        self.properties[2] = value


class WorldStyles:
    """The styles of various world elements."""
    def __init__(self,
                 moon: MoonStyle,
                 trees: FourPartSplit,
                 moss: FourPartSplit,):
        self.moon: MoonStyle = moon
        self.trees: FourPartSplit = trees
        self.moss: FourPartSplit = moss

    def __repr__(self):
        return f"WorldStyles(moon={repr(self.moon)}, trees={repr(self.trees)}, moss={repr(self.moss)})"


class WorldBackgrounds:
    """The backgrounds of various world biomes."""
    def __init__(self,
                 bg_underground_snow: int,
                 bg_underground_jungle: int,
                 bg_hell: int,
                 bg_forest: int,
                 bg_corruption: int,
                 bg_jungle: int,
                 bg_snow: int,
                 bg_hallow: int,
                 bg_crimson: int,
                 bg_desert: int,
                 bg_ocean: int):
        self.bg_underground_snow: int = bg_underground_snow
        self.bg_underground_jungle: int = bg_underground_jungle
        self.bg_hell: int = bg_hell
        self.bg_forest: int = bg_forest
        self.bg_corruption: int = bg_corruption
        self.bg_jungle: int = bg_jungle
        self.bg_snow: int = bg_snow
        self.bg_hallow: int = bg_hallow
        self.bg_crimson: int = bg_crimson
        self.bg_desert: int = bg_desert
        self.bg_ocean: int = bg_ocean

    def __repr__(self):
        return f"WorldBackgrounds({self.bg_underground_snow}, {self.bg_underground_jungle}, {self.bg_hell}, {self.bg_forest}, {self.bg_corruption}, {self.bg_jungle}, {self.bg_snow}, {self.bg_hallow}, {self.bg_crimson}, {self.bg_desert}, {self.bg_ocean})"


class World:
    """The Python representation of a Terraria world."""
    def __init__(self,
                 version: Version,
                 savefile_type: int,
                 revision: int,
                 is_favorite: bool,
                 name: str,
                 generator: GeneratorInfo,
                 uuid_: uuid.UUID,
                 id_: int,
                 bounds: Rect,
                 size: Coordinates,
                 is_expert: bool,
                 created_on,
                 styles: WorldStyles,
                 backgrounds: WorldBackgrounds,
                 spawn_point: Coordinates,
                 underground_level: int,
                 cavern_level: int):

        self.version: Version = version
        """The game version when this savefile was last saved."""

        self.savefile_type = savefile_type
        """The format of the save file. Should be 2 for all versions following 1.2."""

        self.revision: int = revision
        """The number of times this world was saved."""

        self.is_favorite: bool = is_favorite
        """If the world is marked as favorite or not."""

        self.name: str = name
        """The name the world was given at creation. Doesn't always match the filename."""

        self.generator: GeneratorInfo = generator
        """Information about the generation of this world."""

        self.uuid: uuid.UUID = uuid_
        """The Universally Unique ID of this world."""

        self.id: int = id_
        """The world id. Used to name the minimap file."""

        self.bounds: Rect = bounds
        """The world size in pixels."""

        self.size: Coordinates = size
        """The world size in tiles."""

        self.is_expert: bool = is_expert
        """If the world is in expert mode or not."""

        self.created_on = created_on
        """The date and time this world was created in."""

        self.styles: WorldStyles = styles
        """The styles of various world elements."""

        self.backgrounds: WorldBackgrounds = backgrounds
        """The backgrounds of the various biomes."""

        self.spawn_point: Coordinates = spawn_point
        """The coordinates of the spawn point."""

        self.underground_level: float = underground_level
        """The depth at which the underground biome starts."""

        self.cavern_level: float = cavern_level
        """The depth at which the cavern biome starts."""

    @classmethod
    def create_from_file(cls, file):
        f = FileReader(file)

        version = Version(f.int4())
        relogic = f.string(7)
        savefile_type = f.uint1()
        if version != Version("1.3.5.3") or relogic != "relogic" or savefile_type != 2:
            raise NotImplementedError("This parser can only read Terraria 1.3.5.3 save files.")

        revision = f.uint4()
        is_favorite = f.uint8() != 0

        pointers = [f.int4() for _ in range(f.int2())]
        tileframeimportant_size = math.ceil(f.int2() / 8)
        tileframeimportant = []
        for _ in range(tileframeimportant_size):
            current_bit = f.bit()
            tileframeimportant = [*tileframeimportant, *current_bit]

        name = f.string()
        seed = f.string()
        generator_version = f.int4()
        uuid_ = f.uuid()
        id_ = f.int8()
        bounds = f.rect()
        world_size = Coordinates(y=f.int4(), x=f.int4())
        is_expert = f.bool()
        created_on = f.datetime()

        world_styles = WorldStyles(moon=MoonStyle(f.uint1()),
                                   trees=FourPartSplit(separators=[f.int4(), f.int4(), f.int4()],
                                                       properties=[f.int4(), f.int4(), f.int4(), f.int4()]),
                                   moss=FourPartSplit(separators=[f.int4(), f.int4(), f.int4()],
                                                      properties=[f.int4(), f.int4(), f.int4(), f.int4()]))

        bg_underground_snow = f.int4()
        bg_underground_jungle = f.int4()
        bg_hell = f.int4()

        spawn_point = Coordinates(f.int4(), f.int4())
        underground_level = int(f.double())
        cavern_level = int(f.double())
        current_time = f.double()
        is_daytime = f.bool()
        moon_phase = f.uint4()
        blood_moon = f.bool()
        eclipse = f.bool()
        dungeon_point = (f.int4(), f.int4())
        is_crimson = f.bool()
        defeated_eye_of_cthulhu = f.bool()  # Possibly. I'm not sure.
        defeated_eater_of_worlds = f.bool()  # Possibly. I'm not sure.
        defeated_skeletron = f.bool()  # Possibly. I'm not sure.
        defeated_queen_bee = f.bool()
        defeated_the_twins = f.bool()
        defeated_the_destroyer = f.bool()
        defeated_skeletron_prime = f.bool()
        defeated_any_mechnical_boss = f.bool()
        defeated_plantera = f.bool()
        defeated_golem = f.bool()
        defeated_king_slime = f.bool()
        saved_goblin_tinkerer = f.bool()
        saved_wizard = f.bool()
        saved_mechanic = f.bool()
        defeated_goblin_army = f.bool()
        defeated_clown = f.bool()
        defeated_frost_moon = f.bool()
        defeated_pirates = f.bool()
        smashed_shadow_orb = f.bool()
        spawn_meteor = f.bool()
        smashed_shadow_orb_mod3 = f.int4()
        smashed_altars_count = f.int4()
        is_hardmode = f.bool()
        invasion_delay = f.int4()
        invasion_size = f.int4()
        invasion_type = f.int4()
        invasion_position = f.double()
        time_left_slime_rain = f.double()
        cooldown_sundial = f.uint1()
        is_raining = f.bool()
        time_left_rain = f.int4()
        max_rain = f.single()  # ???
        hardmode_ore_1 = f.int4()
        hardmode_ore_2 = f.int4()
        hardmode_ore_3 = f.int4()

        bg_forest = f.int1()
        bg_corruption = f.int1()
        bg_jungle = f.int1()
        bg_snow = f.int1()
        bg_hallow = f.int1()
        bg_crimson = f.int1()
        bg_desert = f.int1()
        bg_ocean = f.int1()

        backgrounds = WorldBackgrounds(bg_underground_snow=bg_underground_snow,
                                       bg_underground_jungle=bg_underground_jungle,
                                       bg_hell=bg_hell,
                                       bg_forest=bg_forest,
                                       bg_corruption=bg_corruption,
                                       bg_jungle=bg_jungle,
                                       bg_snow=bg_snow,
                                       bg_hallow=bg_hallow,
                                       bg_crimson=bg_crimson,
                                       bg_desert=bg_desert,
                                       bg_ocean=bg_ocean)

        bg_cloud = f.int4()  # ???
        cloud_number = f.int2()  # ???
        wind_speed = f.single()  # ???
        angler_today_quest_completed_by_count = f.uint1()
        angler_today_quest_completed_by = []
        for _ in range(angler_today_quest_completed_by_count):
            angler_today_quest_completed_by.append(f.string())
        saved_angler = f.bool()
        angler_today_quest_target = f.int4()
        saved_stylist = f.bool()
        saved_tax_collector = f.bool()
        invasion_size_start = f.int4()  # ???
        cultist_delay = f.int4()  # ???
        ...
        mob_types_count = f.int2()
        mob_kills = {}
        for mob_id in range(mob_types_count):
            mob_kills[mob_id] = f.int4()
        fast_forward_time = f.bool()
        defeated_duke_fishron = f.bool()
        defeated_moon_lord = f.bool()
        defeated_pumpking = f.bool()
        defeated_mourning_wood = f.bool()
        defeated_ice_queen = f.bool()
        defeated_santa_nk1 = f.bool()
        defeated_everscream = f.bool()
        defeated_pillar_solar = f.bool()
        defeated_pillar_vortex = f.bool()
        defeated_pillar_nebula = f.bool()
        defeated_pillar_stardust = f.bool()
        solar_pillar_active = f.bool()
        vortex_pillar_active = f.bool()
        nebula_pillar_active = f.bool()
        stardust_pillar_active = f.bool()
        lunar_events_active = f.bool()
        party_center_active = f.bool()
        party_natural_active = f.bool()
        party_cooldown = f.int4()
        partying_npcs_count = f.int4()
        partying_npcs = []
        for _ in range(partying_npcs_count):
            partying_npcs.append(f.int4())
        is_sandstorm = f.bool()
        time_left_sandstorm = f.int4()
        sandstorm_severity = f.single()  # ???
        sandstorm_intended_severity = f.single()  # ???
        saved_bartender = f.bool()
        defeated_old_ones_army_tier_1 = f.bool()
        defeated_old_ones_army_tier_2 = f.bool()
        defeated_old_ones_army_tier_3 = f.bool()
        # Tile data starts here
        ...


if __name__ == "__main__":
    with open("Small_Example.wld", "rb") as f:
        w = World.create_from_file(f)
