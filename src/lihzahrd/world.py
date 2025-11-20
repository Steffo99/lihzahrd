import logging
import math
import sys
import uuid

from .bestiary import *
from .chests import *
from .enums import *
from .errors import InvalidFooterError
from .fileutils import *
from .header import *
from .items import *
from .journeypowers import *
from .npcs import *
from .pressureplates import *
from .signs import *
from .tileentities import *
from .tiles import *
from .townmanager import *


class World:
    """The Python representation of a Terraria world."""

    def __init__(
            self,
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
            difficulty: Difficulty,
            is_drunk_world: bool,
            is_for_the_worthy: bool,
            is_tenth_anniversary: bool,
            is_the_constant: bool,
            is_bee_world: bool,
            is_upside_down: bool,
            is_trap_world: bool,
            is_zenith_world: bool,
            created_on,
            styles: Styles,
            backgrounds: Backgrounds,
            spawn_point: Coordinates,
            underground_level: float,
            cavern_level: float,
            time: Time,
            events: Events,
            dungeon_point: Coordinates,
            world_evil: WorldEvilType,
            saved_npcs: SavedNPCs,
            altars_smashed: int,
            is_hardmode: bool,
            shadow_orbs: ShadowOrbs,
            bosses_defeated: BossesDefeated,
            anglers_quest: AnglerQuest,
            clouds: Clouds,
            cultist_delay: int,
            tiles: TileMatrix,
            bestiary: Bestiary,
            journey_powers: JourneyPowers,
            chests: list[Chest],
            signs: list[Sign],
            shimmered_npcs: list[int],
            npcs: list[NPC],
            mobs: list[Mob],
            tile_entities: list[TileEntity],
            weighed_pressure_plates: list[WeighedPressurePlate],
            rooms: list[Room],
            pets: Pets,
            halloween_today: bool,
            xmas_today: bool,
            treetop_variants: TreetopVariants,
            saved_ore_tiers: SavedOreTiers,
            unknown_file_format_data: bytes = b"",
            unknown_world_header_data: bytes = b"",
            unknown_world_tiles_data: bytes = b"",
            unknown_chests_data: bytes = b"",
            unknown_signs_data: bytes = b"",
            unknown_npcs_data: bytes = b"",
            unknown_tile_entities_data: bytes = b"",
            unknown_pressure_plates_data: bytes = b"",
            unknown_town_manager_data: bytes = b"",
            unknown_bestiary_data: bytes = b"",
            unknown_journey_powers_data: bytes = b"",
    ):

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

        self.difficulty: Difficulty = difficulty
        """The difficulty (https://terraria.gamepedia.com/Difficulty) the game is in."""

        self.is_drunk_world: bool = is_drunk_world
        """If the world was created with the `Drunk world <https://terraria.wiki.gg/wiki/Secret_world_seeds#Drunk_world>`_ seed."""

        self.is_for_the_worthy: bool = is_for_the_worthy
        """If the world was created with the `For the worthy <https://terraria.wiki.gg/wiki/Secret_world_seeds#For_the_worthy>`_ seed."""

        self.is_tenth_anniversary: bool = is_tenth_anniversary
        """If the world was created with the `Celebrationmk10 <https://terraria.wiki.gg/wiki/Secret_world_seeds#Celebrationmk10>` seed."""

        self.is_the_constant: bool = is_the_constant
        """If the world was created with `The Constant <https://terraria.wiki.gg/wiki/Secret_world_seeds#The_Constant>`_ seed."""

        self.is_bee_world: bool = is_bee_world
        """If the world was created with the `Not the bees <https://terraria.wiki.gg/wiki/Secret_world_seeds#Not_the_bees>`_ seed."""

        self.is_upside_down: bool = is_upside_down
        """If the world was created with the `Don't dig up <https://terraria.wiki.gg/wiki/Secret_world_seeds#Don't_dig_up>`_ seed."""

        self.is_trap_world: bool = is_trap_world
        """If the world was created with the `No traps <https://terraria.wiki.gg/wiki/Secret_world_seeds#No_traps>`_ seed."""

        self.is_zenith_world: bool = is_zenith_world
        """If the world was created with the `Get fixed boi <https://terraria.wiki.gg/wiki/Secret_world_seeds#Get_fixed_boi>`_ seed."""

        self.created_on = created_on
        """The date and time this world was created in."""

        self.styles: Styles = styles
        """The styles of various world elements."""

        self.backgrounds: Backgrounds = backgrounds
        """The backgrounds of the various biomes."""

        self.spawn_point: Coordinates = spawn_point
        """The coordinates of the spawn point."""

        self.underground_level: float = underground_level
        """The depth at which the underground biome starts."""

        self.cavern_level: float = cavern_level
        """The depth at which the cavern biome starts."""

        self.time: Time = time
        """Game time related information."""

        self.events: Events = events
        """Currently ongoing world events."""

        self.dungeon_point: Coordinates = dungeon_point
        """The Old Man spawn point."""

        self.world_evil: WorldEvilType = world_evil
        """Whether the world has Corruption or Crimson."""

        self.saved_npcs: SavedNPCs = saved_npcs
        """The NPCs that were rescued by the player."""

        self.altars_smashed: int = altars_smashed
        """The number of Demon Altars smashed with a Pwnhammer (or better)."""

        self.is_hardmode: bool = is_hardmode
        """Whether or not the world is in hardmode."""

        self.shadow_orbs: ShadowOrbs = shadow_orbs
        """Information related to the Shadow Orbs or Crimson Hearts in the world."""

        self.bosses_defeated: BossesDefeated = bosses_defeated
        """Which bosses have been defeated in the world."""

        self.anglers_quest: AnglerQuest = anglers_quest
        """Information about today's Angler's Quest."""

        self.tiles: TileMatrix = tiles
        """A matrix of all the tiles present in the world."""

        self.chests: list[Chest] = chests
        """A list of all the containers (chests, barrels) in the world."""

        self.signs: list[Sign] = signs
        """A list of all non-empty signs in the world."""

        self.shimmered_npcs: list[int] = shimmered_npcs
        """A list of the ids of the NPCs that have been shimmered."""

        self.npcs: list[NPC] = npcs
        """A list of all the NPCs currently living in the world, including the Old Man."""

        self.mobs: list[Mob] = mobs
        """(Unknown, possibly a list of mobs in the world?)"""

        self.tile_entities: list[TileEntity] = tile_entities
        """A list of tile entities in the world, such as Training Dummies, Item Frames and Logic Sensors."""

        self.weighed_pressure_plates: list[WeighedPressurePlate] = weighed_pressure_plates
        """A list of all Weighed Pressure Plates in the world."""

        self.pets: Pets = pets
        """Which pets have bene purchased."""

        self.halloween_today: bool = halloween_today
        """Is today an Halloween reward day?
        Triggered by reaching Wave 15 of the Pumpkin Moon."""

        self.xmas_today: bool = xmas_today
        """Is today a Xmas reward day?
        Triggered by reaching Wave 20 of the Frost Moon."""

        self.treetop_variants: TreetopVariants = treetop_variants
        """Treetops variants that can exist in the world."""

        self.saved_ore_tiers: SavedOreTiers = saved_ore_tiers
        """The metals that generated in the world."""

        self.rooms: list[Room] = rooms
        self.clouds: Clouds = clouds
        self.cultist_delay: int = cultist_delay
        self.unknown_file_format_data: bytes = unknown_file_format_data
        self.unknown_world_header_data: bytes = unknown_world_header_data
        self.unknown_world_tiles_data: bytes = unknown_world_tiles_data
        self.unknown_chests_data: bytes = unknown_chests_data
        self.unknown_signs_data: bytes = unknown_signs_data
        self.unknown_npcs_data: bytes = unknown_npcs_data
        self.unknown_tile_entities_data: bytes = unknown_tile_entities_data
        self.unknown_pressure_plates_data: bytes = unknown_pressure_plates_data
        self.unknown_town_manager_data: bytes = unknown_town_manager_data
        self.unknown_bestiary_data: bytes = unknown_bestiary_data
        self.unknown_journey_powers_data: bytes = unknown_journey_powers_data

        self.bestiary: Bestiary = bestiary
        """Information about the bestiary, including sightings, kills and takling to NPCs."""

        self.journey_powers: JourneyPowers = journey_powers
        """Status of powers available in Journey mode."""

    def __repr__(self):
        return f'<World "{self.name}">'

    @property
    def crimson_hearts(self) -> ShadowOrbs:
        """Information related to the Shadow Orbs or Crimson Hearts in the world."""
        return self.shadow_orbs

    @crimson_hearts.setter
    def crimson_hearts(self, value):
        self.shadow_orbs = value

    @staticmethod
    def _read_tile_block(fr: FilePacker, tileframeimportant) -> tuple[Tile, int]:
        flags1 = fr.read_bits()
        has_flags2 = flags1[0]
        flags2 = fr.read_bits() if has_flags2 else BITS[0]
        has_flags3 = flags2[0]
        flags3 = fr.read_bits() if has_flags3 else BITS[0]
        has_flags4 = flags3[0]
        flags4 = fr.read_bits() if has_flags4 else BITS[0]

        has_block = flags1[1]
        has_extended_block_id = flags1[5]
        is_block_painted = flags3[3]
        is_block_active = not flags3[2]
        is_block_echo = flags4[1]
        is_block_illuminant = flags4[3]

        has_wall = flags1[2]
        has_extended_wall_id = flags3[6]
        is_wall_painted = flags3[4]
        is_wall_echo = flags4[2]
        is_wall_illuminant = flags4[4]

        liquid_type = LiquidType.from_flags(flags1, flags3)
        rle_compression = RLEEncoding.from_flags(flags1)
        block_shape = Shape.from_flags(flags2)
        wiring = Wiring.from_flags(flags2, flags3)

        # Parse block
        if has_block:
            if has_extended_block_id:
                block_type = BlockType(fr.read_uint2())
            else:
                block_type = BlockType(fr.read_uint1())
            if tileframeimportant[block_type]:
                frame = FrameImportantData(fr.read_uint2(), fr.read_uint2())
            else:
                frame = None
            if is_block_painted:
                block_paint = fr.read_uint1()
            else:
                block_paint = None
            block = Block(
                type_=block_type,
                frame=frame,
                paint=block_paint,
                is_active=is_block_active,
                shape=block_shape,
                is_illuminant=is_block_illuminant,
                is_echo=is_block_echo,
            )
        else:
            block = None

        # Parse wall
        if has_wall:
            wall_type_l = fr.read_uint1()
            if is_wall_painted:
                wall_paint = fr.read_uint1()
            else:
                wall_paint = None
        else:
            wall_type_l = 0
            wall_paint = None

        # Parse liquid
        if liquid_type != LiquidType.NO_LIQUID:
            liquid = Liquid(type_=liquid_type, volume=fr.read_uint1())
        else:
            liquid = None

        # Parse wall, again
        if has_extended_wall_id:
            wall_type_g = fr.read_uint1()
        else:
            wall_type_g = 0

        if has_wall:
            wall_type = WallType(wall_type_g * 256 + wall_type_l)
            wall = Wall(
                type_=wall_type,
                paint=wall_paint,
                is_illuminant=is_wall_illuminant,
                is_echo=is_wall_echo,
            )
        else:
            wall = None

        # Find RLE Compression multiplier
        if rle_compression == RLEEncoding.DOUBLE_BYTE:
            multiply_by = fr.read_uint2() + 1
        elif rle_compression == RLEEncoding.SINGLE_BYTE:
            multiply_by = fr.read_uint1() + 1
        else:
            multiply_by = 1

        # Create tile
        tile = Tile(block=block, wall=wall, liquid=liquid, wiring=wiring)
        return tile, multiply_by

    @property
    def is_classic(self):
        """If the world is in classic difficulty or not."""
        return self.difficulty == 0

    @property
    def is_expert(self):
        """If the world is in expert difficulty or not."""
        return self.difficulty == 1 or self.difficulty == 0 and (self.is_for_the_worthy or self.is_zenith_world)

    @property
    def is_master(self):
        """If the world is in master difficulty or not."""
        return self.difficulty == 2 or self.difficulty == 1 and (self.is_for_the_worthy or self.is_zenith_world)

    @property
    def is_legendary(self):
        """If the world is in legendary difficulty or not."""
        return self.difficulty == 2 and (self.is_for_the_worthy or self.is_zenith_world)

    @property
    def is_journey(self):
        """If the world is in journey difficulty or not."""
        return self.difficulty == 3

    @classmethod
    def _create_tilematrix(cls, f, world_size: Coordinates, tileframeimportant: list[bool]):
        """Create a TileMatrix object from a file."""
        tm = TileMatrix()
        while tm.size.x < world_size.x:
            column = []
            while len(column) < world_size.y:
                tile, multiply_by = cls._read_tile_block(f, tileframeimportant)
                for _ in range(multiply_by):
                    # This works by reference, and stops working if write support is added
                    column.append(tile)
            tm.add_column(column)
        return tm

    @classmethod
    def create_from_file(cls, filename: str):
        """Create a World object from a .wld file.

        Warning:
            Parsing an entire world may take up to a few minutes and quite a bit of memory!

        Arguments:
            filename: The name of the file that should be parsed."""
        # This code is a mess.

        with open(filename, "rb") as file:
            data = bytearray(file.read())
        f = FilePacker(data)

        # File header
        version = Version(f.read_int4())

        relogic = f.read_string_fixed(7)  # TODO: this can appearently be "xindong"?
        if relogic != "relogic":
            raise ValueError("World file is missing the 'relogic' magic string", relogic)

        savefile_type = f.read_uint1()
        if savefile_type != 2:
            raise NotImplementedError("World file uses an unknown savefile type", savefile_type)

        supported_versions = (Version("1.4.4.9"),)
        if version not in supported_versions:
            raise NotImplementedError("World file has been created with a unsupported version of Terraria", version)

        revision = f.read_uint4()
        is_favorite = f.read_uint8() != 0

        # Pointers and tileframeimportant
        pointers = Pointers(*[f.read_int4() for _ in range(f.read_int2())])
        tileframeimportant_size = math.ceil(f.read_int2() / 8)
        tileframeimportant = []
        for _ in range(tileframeimportant_size):
            current_bits = f.read_bits()
            tileframeimportant = [*tileframeimportant, *current_bits]

        unknown_file_format_data = f.read_bytearray_to_address(pointers.world_header)

        name = f.read_string_variable()
        generator = GeneratorInfo(f.read_string_variable(), f.read_uint8())

        uuid_ = f.read_uuid()
        id_ = f.read_int4()
        bounds = f.read_rect()
        world_size = Coordinates(y=f.read_int4(), x=f.read_int4())
        difficulty = Difficulty(f.read_int4())
        is_drunk_world = f.read_boolean()
        is_for_the_worthy = f.read_boolean()
        is_tenth_anniversary = f.read_boolean()
        is_the_constant = f.read_boolean()
        is_bee_world = f.read_boolean()
        is_upside_down = f.read_boolean()
        is_trap_world = f.read_boolean()
        is_zenith_world = f.read_boolean()

        created_on = f.read_datetime()

        world_styles = Styles(
            moon=MoonStyle(f.read_uint1()),
            trees=FourPartSplit(
                separators=[f.read_int4(), f.read_int4(), f.read_int4()], properties=[f.read_int4(), f.read_int4(), f.read_int4(), f.read_int4()]
            ),
            moss=FourPartSplit(
                separators=[f.read_int4(), f.read_int4(), f.read_int4()], properties=[f.read_int4(), f.read_int4(), f.read_int4(), f.read_int4()]
            ),
        )

        bg_underground_snow = f.read_int4()
        bg_underground_jungle = f.read_int4()
        bg_hell = f.read_int4()

        spawn_point = Coordinates(f.read_int4(), f.read_int4())
        underground_level = f.read_fdouble()
        cavern_level = f.read_fdouble()

        current_time = f.read_fdouble()
        is_daytime = f.read_boolean()
        moon_phase = MoonPhase(f.read_uint4())

        blood_moon = f.read_boolean()
        eclipse = f.read_boolean()

        dungeon_point = Coordinates(f.read_int4(), f.read_int4())
        world_evil = WorldEvilType(f.read_boolean())

        defeated_eye_of_cthulhu = f.read_boolean()  # Possibly. I'm not sure.
        defeated_eater_of_worlds = f.read_boolean()  # Possibly. I'm not sure.
        defeated_skeletron = f.read_boolean()  # Possibly. I'm not sure.
        defeated_queen_bee = f.read_boolean()
        defeated_the_twins = f.read_boolean()
        defeated_the_destroyer = f.read_boolean()
        defeated_skeletron_prime = f.read_boolean()
        defeated_any_mechnical_boss = f.read_boolean()
        defeated_plantera = f.read_boolean()
        defeated_golem = f.read_boolean()
        defeated_king_slime = f.read_boolean()

        saved_goblin_tinkerer = f.read_boolean()
        saved_wizard = f.read_boolean()
        saved_mechanic = f.read_boolean()

        defeated_goblin_army = f.read_boolean()
        defeated_clown = f.read_boolean()
        defeated_frost_moon = f.read_boolean()
        defeated_pirates = f.read_boolean()

        shadow_orbs = ShadowOrbs(
            smashed_at_least_once=f.read_boolean(), spawn_meteorite=f.read_boolean(), evil_boss_counter=f.read_uint1()
        )  # was int4()

        altars_smashed = f.read_int4()

        is_hardmode = f.read_boolean()

        party_is_doomed = not f.read_boolean()

        invasion_delay = f.read_int4()
        invasion_size = f.read_int4()
        invasion_type = InvasionType(f.read_int4())
        invasion_position = f.read_fdouble()

        time_left_slime_rain = f.read_fdouble()

        sundial_cooldown = f.read_uint1()

        rain = Rain(is_active=f.read_boolean(), time_left=f.read_int4(), max_rain=f.read_fsingle())

        try:
            hardmode_ore_1 = BlockType(f.read_int4())
        except ValueError:
            hardmode_ore_1 = None
        try:
            hardmode_ore_2 = BlockType(f.read_int4())
        except ValueError:
            hardmode_ore_2 = None
        try:
            hardmode_ore_3 = BlockType(f.read_int4())
        except ValueError:
            hardmode_ore_3 = None

        bg_forest = f.read_uint1()
        bg_corruption = f.read_uint1()
        bg_jungle = f.read_uint1()
        bg_snow = f.read_uint1()
        bg_hallow = f.read_uint1()
        bg_crimson = f.read_uint1()
        bg_desert = f.read_uint1()
        bg_ocean = f.read_uint1()

        clouds = Clouds(bg_cloud=f.read_int4(), cloud_number=f.read_int2(), wind_speed=f.read_fsingle())

        angler_today_quest_completed_by_count = f.read_int4()  # was uint1()
        angler_today_quest_completed_by = []
        for _ in range(angler_today_quest_completed_by_count):
            angler_today_quest_completed_by.append(f.read_string_variable())

        saved_angler = f.read_boolean()

        angler_today_quest_target = AnglerQuestFish(f.read_int4())
        anglers_quest = AnglerQuest(
            current_goal=angler_today_quest_target, completed_by=angler_today_quest_completed_by
        )

        saved_stylist = f.read_boolean()
        saved_tax_collector = f.read_boolean()
        saved_golfer = f.read_boolean()

        invasion_size_start = f.read_int4()  # ???
        invasion = Invasion(
            delay=invasion_delay,
            size=invasion_size,
            type_=invasion_type,
            position=invasion_position,
            size_start=invasion_size_start,
        )

        cultist_delay = f.read_int4()  # ???
        mob_types_count = f.read_int2()
        mob_kills = {}
        for mob_id in range(mob_types_count):
            mob_kills[mob_id] = f.read_int4()

        sundial_is_running = f.read_boolean()

        defeated_duke_fishron = f.read_boolean()
        defeated_martian_madness = f.read_boolean()
        defeated_lunatic_cultist = f.read_boolean()
        defeated_moon_lord = f.read_boolean()
        defeated_pumpking = f.read_boolean()
        defeated_mourning_wood = f.read_boolean()
        defeated_ice_queen = f.read_boolean()
        defeated_santa_nk1 = f.read_boolean()
        defeated_everscream = f.read_boolean()
        defeated_pillars = PillarsInfo(solar=f.read_boolean(), vortex=f.read_boolean(), nebula=f.read_boolean(), stardust=f.read_boolean())

        lunar_events = LunarEvents(
            pillars_present=PillarsInfo(solar=f.read_boolean(), vortex=f.read_boolean(), nebula=f.read_boolean(), stardust=f.read_boolean()),
            are_active=f.read_boolean(),
        )

        party_center_active = f.read_boolean()
        party_natural_active = f.read_boolean()
        party_cooldown = f.read_int4()
        partying_npcs_count = f.read_int4()
        partying_npcs = []
        for _ in range(partying_npcs_count):
            partying_npcs.append(f.read_int4())
        party = Party(
            is_doomed=party_is_doomed,
            thrown_by_party_center=party_center_active,
            thrown_by_npcs=party_natural_active,
            cooldown=party_cooldown,
            partying_npcs=partying_npcs,
        )

        sandstorm = Sandstorm(is_active=f.read_boolean(), time_left=f.read_int4(), severity=f.read_fsingle(), intended_severity=f.read_fsingle())

        saved_bartender = f.read_boolean()

        old_ones_army = OldOnesArmyTiers(f.read_boolean(), f.read_boolean(), f.read_boolean())

        # ToDo: Figure out which biomes got new BGs.
        # Oasis and Graveyard probably got new backgrounds.
        bg_mushroom = f.read_uint1()
        bg_underworld = f.read_uint1()
        bg_forest_2 = f.read_uint1()  # Maybe oasis.
        bg_forest_3 = f.read_uint1()
        bg_forest_4 = f.read_uint1()

        backgrounds = Backgrounds(
            underground_snow=bg_underground_snow,
            underground_jungle=bg_underground_jungle,
            hell=bg_hell,
            forest=FourPartSplit(world_styles.trees.separators, [bg_forest, bg_forest_2, bg_forest_3, bg_forest_4]),
            corruption=bg_corruption,
            jungle=bg_jungle,
            snow=bg_snow,
            hallow=bg_hallow,
            crimson=bg_crimson,
            desert=bg_desert,
            ocean=bg_ocean,
            mushroom=bg_mushroom,
            underworld=bg_underworld,
        )

        combat_book_used = f.read_boolean()

        lantern_night = LanternNight(
            nights_on_cooldown=f.read_int4(),
            genuine=f.read_boolean(),
            manual=f.read_boolean(),
            next_night_is_lantern_night=f.read_boolean()
        )

        events = Events(
            blood_moon=blood_moon,
            solar_eclipse=eclipse,
            invasion=invasion,
            slime_rain=time_left_slime_rain,
            rain=rain,
            party=party,
            sandstorm=sandstorm,
            lunar_events=lunar_events,
            lantern_night=lantern_night,
        )

        treetop_variant_count = f.read_int4()
        treetop_variants = TreetopVariants([f.read_int4() for _ in range(treetop_variant_count)])

        halloween_today = f.read_boolean()
        xmas_today = f.read_boolean()

        ore_1 = BlockType(f.read_int4())
        ore_2 = BlockType(f.read_int4())
        ore_3 = BlockType(f.read_int4())
        ore_4 = BlockType(f.read_int4())
        saved_ore_tiers = SavedOreTiers(ore_1, ore_2, ore_3, ore_4, hardmode_ore_1, hardmode_ore_2, hardmode_ore_3)

        pets = Pets(cat=f.read_boolean(), dog=f.read_boolean(), bunny=f.read_boolean())

        defeated_empress_of_light = f.read_boolean()
        defeated_queen_slime = f.read_boolean()
        defeated_deerclops = f.read_boolean()

        bosses_defeated = BossesDefeated(
            eye_of_cthulhu=defeated_eye_of_cthulhu,
            eater_of_worlds=defeated_eater_of_worlds,
            skeletron=defeated_skeletron,
            queen_bee=defeated_queen_bee,
            the_twins=defeated_the_twins,
            the_destroyer=defeated_the_destroyer,
            skeletron_prime=defeated_skeletron_prime,
            any_mechnical_boss=defeated_any_mechnical_boss,
            plantera=defeated_plantera,
            golem=defeated_golem,
            king_slime=defeated_king_slime,
            goblin_army=defeated_goblin_army,
            clown=defeated_clown,
            frost_moon=defeated_frost_moon,
            pirates=defeated_pirates,
            duke_fishron=defeated_duke_fishron,
            moon_lord=defeated_moon_lord,
            pumpking=defeated_pumpking,
            mourning_wood=defeated_mourning_wood,
            ice_queen=defeated_ice_queen,
            santa_nk1=defeated_santa_nk1,
            everscream=defeated_everscream,
            lunar_pillars=defeated_pillars,
            old_ones_army=old_ones_army,
            martian_madness=defeated_martian_madness,
            lunatic_cultist=defeated_lunatic_cultist,
            empress_of_light=defeated_empress_of_light,
            queen_slime=defeated_queen_slime,
            deerclops=defeated_deerclops,
        )

        saved_slime_nerdy = f.read_boolean()
        saved_merchant = f.read_boolean()
        saved_demolitionist = f.read_boolean()
        saved_party_girl = f.read_boolean()
        saved_dye_trader = f.read_boolean()
        saved_truffle = f.read_boolean()
        saved_arms_dealer = f.read_boolean()
        saved_nurse = f.read_boolean()
        saved_princess = f.read_boolean()
        combat_book_2_used = f.read_boolean()
        peddler_satchel_used = f.read_boolean()
        saved_slime_cool = f.read_boolean()
        saved_slime_elder = f.read_boolean()
        saved_slime_clumsy = f.read_boolean()
        saved_slime_diva = f.read_boolean()
        saved_slime_surly = f.read_boolean()
        saved_slime_mystic = f.read_boolean()
        saved_slime_squire = f.read_boolean()

        saved_npcs = SavedNPCs(
            goblin_tinkerer=saved_goblin_tinkerer,
            wizard=saved_wizard,
            mechanic=saved_mechanic,
            angler=saved_angler,
            stylist=saved_stylist,
            tax_collector=saved_tax_collector,
            bartender=saved_bartender,
            golfer=saved_golfer,
            advanced_combat=combat_book_used,
            slime_nerdy=saved_slime_nerdy,
            merchant=saved_merchant,
            demolitionist=saved_demolitionist,
            party_girl=saved_party_girl,
            dye_trader=saved_dye_trader,
            truffle=saved_truffle,
            arms_dealer=saved_arms_dealer,
            nurse=saved_nurse,
            princess=saved_princess,
            advanced_combat_2=combat_book_2_used,
            peddlers_satchel=peddler_satchel_used,
            slime_cool=saved_slime_cool,
            slime_elder=saved_slime_elder,
            slime_clumsy=saved_slime_clumsy,
            slime_diva=saved_slime_diva,
            slime_surly=saved_slime_surly,
            slime_mystic=saved_slime_mystic,
            slime_squire=saved_slime_squire,
        )

        moondial_is_running = f.read_boolean()
        moondial_cooldown = f.read_uint1()

        time = Time(
            current=current_time,
            is_daytime=is_daytime,
            moon_phase=moon_phase,
            sundial_cooldown=sundial_cooldown,
            sundial_is_running=sundial_is_running,
            moondial_cooldown=moondial_cooldown,
            moondial_is_running=moondial_is_running,
        )

        unknown_world_header_data = f.read_bytearray_to_address(pointers.world_tiles)

        # Tiles
        tm = cls._create_tilematrix(f, world_size, tileframeimportant)

        unknown_world_tiles_data = f.read_bytearray_to_address(pointers.chests)

        # Chests
        chests = []

        chests_count = f.read_int2()
        chests_max_items = f.read_int2()

        for _ in range(chests_count):
            chest_position = Coordinates(x=f.read_int4(), y=f.read_int4())
            chest_name = f.read_string_variable()
            chest_contents = []

            for _ in range(chests_max_items):
                item_quantity = f.read_int2()
                if item_quantity > 0:
                    item_type = ItemType(f.read_int4())
                    item_modifier = PrefixType.get(f.read_uint1())
                    item = ItemStack(quantity=item_quantity, type_=item_type, prefix=item_modifier)
                else:
                    item = None
                chest_contents.append(item)
            chest = Chest(position=chest_position, name=chest_name, contents=chest_contents)
            chests.append(chest)
            tm[chest.position].extra = chest

        unknown_chests_data = f.read_bytearray_to_address(pointers.signs)

        # Signs
        signs = []

        signs_count = f.read_int2()

        for _ in range(signs_count):
            sign = Sign(text=f.read_string_variable(), position=Coordinates(f.read_int4(), f.read_int4()))
            signs.append(sign)
            tm[sign.position].extra = sign

        unknown_signs_data = f.read_bytearray_to_address(pointers.npcs)

        # Entities
        npcs = []
        mobs = []

        shimmered_npcs_count = f.read_int4()
        shimmered_npcs = []
        for _ in range(shimmered_npcs_count):
            shimmered_npcs.append(f.read_int4())

        while f.read_boolean():
            npc_type = EntityType(f.read_int4())
            npc_name = f.read_string_variable()
            npc_position = Coordinates(f.read_fsingle(), f.read_fsingle())
            is_homeless = f.read_boolean()
            npc_home = Coordinates(f.read_int4(), f.read_int4())
            if is_homeless:
                npc_home = None

            npc_flags = f.read_bits()
            npc_variation_index = f.read_int4() if npc_flags[0] else 0

            npc = NPC(
                type_=npc_type, name=npc_name, position=npc_position, home=npc_home, variation_index=npc_variation_index
            )
            npcs.append(npc)

        while f.read_boolean():
            mob_type = EntityType(f.read_int4())
            mob_position = Coordinates(f.read_fsingle(), f.read_fsingle())

            mob = Mob(type_=mob_type, position=mob_position)
            mobs.append(mob)

        unknown_npcs_data = f.read_bytearray_to_address(pointers.tile_entities)

        # Tile entities
        tile_entities_count = f.read_int4()
        tile_entities = []

        for _ in range(tile_entities_count):
            te_type = f.read_uint1()
            te_id = f.read_int4()
            te_position = Coordinates(f.read_int2(), f.read_int2())
            # Target Dummy
            if te_type == 0:
                te_extra = TargetDummy(npc=f.read_int2())
            # Item Frame
            elif te_type == 1:
                te_extra = ItemFrame(
                    item=ItemStack(type_=ItemType(f.read_int2()), prefix=PrefixType.get(f.read_uint1()), quantity=f.read_int2())
                )
            # Logic Sensor
            elif te_type == 2:
                te_extra = LogicSensor(logic_check=f.read_uint1(), enabled=f.read_boolean())
            # Mannequin
            elif te_type == 3:
                item_flags = f.read_bits()
                dye_flags = f.read_bits()
                mannequin_items: list[ItemStack | None] = [None for _ in range(8)]
                mannequin_dyes: list[ItemStack | None] = [None for _ in range(8)]
                for index, flag in enumerate(item_flags):
                    if not flag:
                        continue
                    mannequin_items[index] = ItemStack(
                        type_=ItemType(f.read_int2()), prefix=PrefixType.get(f.read_uint1()), quantity=f.read_int2()
                    )
                for index, flag in enumerate(dye_flags):
                    if not flag:
                        continue
                    mannequin_dyes[index] = ItemStack(
                        type_=ItemType(f.read_int2()), prefix=PrefixType.get(f.read_uint1()), quantity=f.read_int2()
                    )
                te_extra = Mannequin(mannequin_items, mannequin_dyes)
            # Weapon Rack
            elif te_type == 4:
                rack_item = ItemStack(type_=ItemType(f.read_int2()), prefix=PrefixType.get(f.read_uint1()), quantity=f.read_int2())
                te_extra = WeaponRack(rack_item)
            # Hat Rack
            elif te_type == 5:
                # This isn't 100% tested, but the first two flags should be items, and the second two should be dyes.
                item_flags = f.read_bits()
                # Maximum of two items slots and two dye slots.
                rack_items: list[ItemStack | None] = [None for _ in range(2)]
                rack_dyes: list[ItemStack | None] = [None for _ in range(2)]
                for index, flag in enumerate(item_flags[0:2]):
                    if not flag:
                        continue
                    rack_items[index] = ItemStack(
                        type_=ItemType(f.read_int2()), prefix=PrefixType.get(f.read_uint1()), quantity=f.read_int2()
                    )
                for index, flag in enumerate(item_flags[2:4]):
                    if not flag:
                        continue
                    rack_dyes[index] = ItemStack(
                        type_=ItemType(f.read_int2()), prefix=PrefixType.get(f.read_uint1()), quantity=f.read_int2()
                    )
                te_extra = HatRack(rack_items, rack_dyes)
            # Food Plate
            elif te_type == 6:
                plate_item = ItemStack(type_=ItemType(f.read_int2()), prefix=PrefixType.get(f.read_uint1()), quantity=f.read_int2())
                te_extra = Plate(plate_item)
            # Teleport Pylon
            elif te_type == 7:
                te_extra = Pylon()
            else:
                print(f"te_type:", te_type)
                te_extra = None

            tile_entity = TileEntity(id_=te_id, position=te_position, extra=te_extra)
            tile_entities.append(tile_entity)
            tm[tile_entity.position].extra = tile_entity

        unknown_tile_entities_data = f.read_bytearray_to_address(pointers.pressure_plates)

        # Weighed Pressure Plates
        weighed_pressure_plates_count = f.read_int4()
        weighed_pressure_plates = []

        for _ in range(weighed_pressure_plates_count):
            wpp = WeighedPressurePlate(position=Coordinates(f.read_int4(), f.read_int4()))
            weighed_pressure_plates.append(wpp)
            tm[wpp.position].extra = wpp

        unknown_pressure_plates_data = f.read_bytearray_to_address(pointers.town_manager)

        # Town Manager
        rooms_count = f.read_int4()
        rooms = []

        for _ in range(rooms_count):
            room = Room(npc=EntityType(f.read_int4()), position=Coordinates(f.read_int4(), f.read_int4()))
            rooms.append(room)

        unknown_town_manager_data = f.read_bytearray_to_address(pointers.bestiary)

        bestiary_kills = {}
        for _ in range(f.read_int4()):
            entity = EntityType[f.read_string_variable()]
            kills = f.read_int4()
            bestiary_kills[entity] = kills

        bestiary_sightings = [EntityType[f.read_string_variable()] for _ in range(f.read_int4())]
        bestiary_chats = [EntityType[f.read_string_variable()] for _ in range(f.read_int4())]

        bestiary = Bestiary(chats=bestiary_chats, kills=bestiary_kills, sightings=bestiary_sightings)

        unknown_bestiary_data = f.read_bytearray_to_address(pointers.journey_powers)

        journey_powers = JourneyPowers()
        while f.read_boolean():
            power_id = f.read_int2()
            if power_id == 0:
                journey_powers.freeze_time = f.read_boolean()
            elif power_id == 8:
                journey_powers.time_rate = f.read_fsingle()
            elif power_id == 9:
                journey_powers.freeze_rain = f.read_boolean()
            elif power_id == 10:
                journey_powers.freeze_wind = f.read_boolean()
            elif power_id == 12:
                journey_powers.difficulty = f.read_fsingle()
            elif power_id == 13:
                journey_powers.freeze_biome_spread = f.read_boolean()

        unknown_journey_powers_data = f.read_bytearray_to_address(pointers.footer)

        # Object creation
        result = cls(
            version=version,
            savefile_type=savefile_type,
            revision=revision,
            is_favorite=is_favorite,
            name=name,
            generator=generator,
            uuid_=uuid_,
            id_=id_,
            bounds=bounds,
            size=world_size,
            difficulty=difficulty,
            is_drunk_world=is_drunk_world,
            is_for_the_worthy=is_for_the_worthy,
            is_tenth_anniversary=is_tenth_anniversary,
            is_the_constant=is_the_constant,
            is_bee_world=is_bee_world,
            is_upside_down=is_upside_down,
            is_trap_world=is_trap_world,
            is_zenith_world=is_zenith_world,
            created_on=created_on,
            styles=world_styles,
            backgrounds=backgrounds,
            spawn_point=spawn_point,
            underground_level=underground_level,
            cavern_level=cavern_level,
            time=time,
            events=events,
            dungeon_point=dungeon_point,
            world_evil=world_evil,
            saved_npcs=saved_npcs,
            altars_smashed=altars_smashed,
            is_hardmode=is_hardmode,
            shadow_orbs=shadow_orbs,
            bosses_defeated=bosses_defeated,
            anglers_quest=anglers_quest,
            clouds=clouds,
            cultist_delay=cultist_delay,
            tiles=tm,
            chests=chests,
            signs=signs,
            shimmered_npcs=shimmered_npcs,
            npcs=npcs,
            mobs=mobs,
            tile_entities=tile_entities,
            weighed_pressure_plates=weighed_pressure_plates,
            rooms=rooms,
            halloween_today=halloween_today,
            xmas_today=xmas_today,
            treetop_variants=treetop_variants,
            saved_ore_tiers=saved_ore_tiers,
            pets=pets,
            bestiary=bestiary,
            journey_powers=journey_powers,
            unknown_file_format_data=unknown_file_format_data,
            unknown_world_header_data=unknown_world_header_data,
            unknown_world_tiles_data=unknown_world_tiles_data,
            unknown_chests_data=unknown_chests_data,
            unknown_signs_data=unknown_signs_data,
            unknown_npcs_data=unknown_npcs_data,
            unknown_tile_entities_data=unknown_tile_entities_data,
            unknown_pressure_plates_data=unknown_pressure_plates_data,
            unknown_town_manager_data=unknown_town_manager_data,
            unknown_bestiary_data=unknown_bestiary_data,
            unknown_journey_powers_data=unknown_journey_powers_data,
        )

        # Footer
        if not f.read_boolean():
            raise InvalidFooterError("Invalid footer")
        if not f.read_string_variable() == result.name:
            raise InvalidFooterError("Invalid footer")
        if not f.read_int4() == result.id:
            raise InvalidFooterError("Invalid footer")

        return result


__all__ = (
    "World",
)

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    world = World.create_from_file(sys.argv[1])
    breakpoint()
