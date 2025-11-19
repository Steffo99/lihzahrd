import uuid
import math
import sys
from typing import *
from .fileutils import *
from .enums import *
from .items import *
from .header import *
from .tiles import *
from .bestiary import *
from .journeypowers import *
from .chests import *
from .signs import *
from .npcs import *
from .tileentities import *
from .pressureplates import *
from .townmanager import *
from .errors import InvalidFooterError


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
        chests: List[Chest],
        signs: List[Sign],
        shimmered_npcs: List[int],
        npcs: List[NPC],
        mobs: List[Mob],
        tile_entities: List[TileEntity],
        weighed_pressure_plates: List[WeighedPressurePlate],
        rooms: List[Room],
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

        self.chests: List[Chest] = chests
        """A list of all the containers (chests, barrels) in the world."""

        self.signs: List[Sign] = signs
        """A list of all non-empty signs in the world."""

        self.shimmered_npcs: List[int] = shimmered_npcs
        """A list of the ids of the NPCs that have been shimmered."""

        self.npcs: List[NPC] = npcs
        """A list of all the NPCs currently living in the world, including the Old Man."""

        self.mobs: List[Mob] = mobs
        """(Unknown, possibly a list of mobs in the world?)"""

        self.tile_entities: List[TileEntity] = tile_entities
        """A list of tile entities in the world, such as Training Dummies, Item Frames and Logic Sensors."""

        self.weighed_pressure_plates: List[WeighedPressurePlate] = weighed_pressure_plates
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

        self.rooms: List[Room] = rooms
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
    def _read_tile_block(fr: FileReader, tileframeimportant) -> Tuple[Tile, int]:
        flags1 = fr.bits()
        has_flags2 = flags1[0]
        flags2 = fr.bits() if has_flags2 else INT_TO_BITS_CACHE[0]
        has_flags3 = flags2[0]
        flags3 = fr.bits() if has_flags3 else INT_TO_BITS_CACHE[0]
        has_flags4 = flags3[0]
        flags4 = fr.bits() if has_flags4 else INT_TO_BITS_CACHE[0]
            
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
                block_type = BlockType(fr.uint2())
            else:
                block_type = BlockType(fr.uint1())
            if tileframeimportant[block_type]:
                frame = FrameImportantData(fr.uint2(), fr.uint2())
            else:
                frame = None
            if is_block_painted:
                block_paint = fr.uint1()
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
            wall_type_l = fr.uint1()
            if is_wall_painted:
                wall_paint = fr.uint1()
            else:
                wall_paint = None
        else:
            wall_type_l = 0
            wall_paint = None

        # Parse liquid
        if liquid_type != LiquidType.NO_LIQUID:
            liquid = Liquid(type_=liquid_type, volume=fr.uint1())
        else:
            liquid = None

        # Parse wall, again
        if has_extended_wall_id:
            wall_type_g = fr.uint1()
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
            multiply_by = fr.uint2() + 1
        elif rle_compression == RLEEncoding.SINGLE_BYTE:
            multiply_by = fr.uint1() + 1
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
    def _create_tilematrix(cls, f, world_size: Coordinates, tileframeimportant: List[bool]):
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

        file = open(filename, "rb")
        f = FileReader(file)

        # File header
        version = Version(f.int4())

        relogic = f.string(7)  # TODO: this can appearently be "xindong"?
        if relogic != "relogic":
            raise ValueError("World file is missing the 'relogic' magic string", relogic)

        savefile_type = f.uint1()
        if savefile_type != 2:
            raise NotImplementedError("World file uses an unknown savefile type", savefile_type)

        supported_versions = (Version("1.4.4.9"),)
        if version not in supported_versions:
            raise NotImplementedError("World file has been created with a unsupported version of Terraria", version)

        revision = f.uint4()
        is_favorite = f.uint8() != 0

        # Pointers and tileframeimportant
        pointers = Pointers(*[f.int4() for _ in range(f.int2())])
        tileframeimportant_size = math.ceil(f.int2() / 8)
        tileframeimportant = []
        for _ in range(tileframeimportant_size):
            current_bit = f.bits()
            tileframeimportant = [*tileframeimportant, *current_bit]

        unknown_file_format_data = f.read_until(pointers.world_header)

        name = f.string()
        generator = GeneratorInfo(f.string(), f.uint8())

        uuid_ = f.uuid()
        id_ = f.int4()
        bounds = f.rect()
        world_size = Coordinates(y=f.int4(), x=f.int4())
        difficulty = Difficulty(f.int4())
        is_drunk_world = f.bool()
        is_for_the_worthy = f.bool()
        is_tenth_anniversary = f.bool()
        is_the_constant = f.bool()
        is_bee_world = f.bool()
        is_upside_down = f.bool()
        is_trap_world = f.bool()
        is_zenith_world = f.bool()

        created_on = f.datetime()

        world_styles = Styles(
            moon=MoonStyle(f.uint1()),
            trees=FourPartSplit(
                separators=[f.int4(), f.int4(), f.int4()], properties=[f.int4(), f.int4(), f.int4(), f.int4()]
            ),
            moss=FourPartSplit(
                separators=[f.int4(), f.int4(), f.int4()], properties=[f.int4(), f.int4(), f.int4(), f.int4()]
            ),
        )

        bg_underground_snow = f.int4()
        bg_underground_jungle = f.int4()
        bg_hell = f.int4()

        spawn_point = Coordinates(f.int4(), f.int4())
        underground_level = f.double()
        cavern_level = f.double()

        current_time = f.double()
        is_daytime = f.bool()
        moon_phase = MoonPhase(f.uint4())

        blood_moon = f.bool()
        eclipse = f.bool()

        dungeon_point = Coordinates(f.int4(), f.int4())
        world_evil = WorldEvilType(f.bool())

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

        shadow_orbs = ShadowOrbs(
            smashed_at_least_once=f.bool(), spawn_meteorite=f.bool(), evil_boss_counter=f.uint1()
        )  # was int4()

        altars_smashed = f.int4()

        is_hardmode = f.bool()

        party_is_doomed = not f.bool()

        invasion_delay = f.int4()
        invasion_size = f.int4()
        invasion_type = InvasionType(f.int4())
        invasion_position = f.double()

        time_left_slime_rain = f.double()

        sundial_cooldown = f.uint1()

        rain = Rain(is_active=f.bool(), time_left=f.int4(), max_rain=f.single())

        try:
            hardmode_ore_1 = BlockType(f.int4())
        except ValueError:
            hardmode_ore_1 = None
        try:
            hardmode_ore_2 = BlockType(f.int4())
        except ValueError:
            hardmode_ore_2 = None
        try:
            hardmode_ore_3 = BlockType(f.int4())
        except ValueError:
            hardmode_ore_3 = None

        bg_forest = f.int1()
        bg_corruption = f.int1()
        bg_jungle = f.int1()
        bg_snow = f.int1()
        bg_hallow = f.int1()
        bg_crimson = f.int1()
        bg_desert = f.int1()
        bg_ocean = f.int1()

        clouds = Clouds(bg_cloud=f.int4(), cloud_number=f.int2(), wind_speed=f.single())

        angler_today_quest_completed_by_count = f.int4()  # was uint1()
        angler_today_quest_completed_by = []
        for _ in range(angler_today_quest_completed_by_count):
            angler_today_quest_completed_by.append(f.string())

        saved_angler = f.bool()

        angler_today_quest_target = AnglerQuestFish(f.int4())
        anglers_quest = AnglerQuest(
            current_goal=angler_today_quest_target, completed_by=angler_today_quest_completed_by
        )

        saved_stylist = f.bool()
        saved_tax_collector = f.bool()
        saved_golfer = f.bool()

        invasion_size_start = f.int4()  # ???
        invasion = Invasion(
            delay=invasion_delay,
            size=invasion_size,
            type_=invasion_type,
            position=invasion_position,
            size_start=invasion_size_start,
        )

        cultist_delay = f.int4()  # ???
        mob_types_count = f.int2()
        mob_kills = {}
        for mob_id in range(mob_types_count):
            mob_kills[mob_id] = f.int4()

        sundial_is_running = f.bool()

        defeated_duke_fishron = f.bool()
        defeated_martian_madness = f.bool()
        defeated_lunatic_cultist = f.bool()
        defeated_moon_lord = f.bool()
        defeated_pumpking = f.bool()
        defeated_mourning_wood = f.bool()
        defeated_ice_queen = f.bool()
        defeated_santa_nk1 = f.bool()
        defeated_everscream = f.bool()
        defeated_pillars = PillarsInfo(solar=f.bool(), vortex=f.bool(), nebula=f.bool(), stardust=f.bool())

        lunar_events = LunarEvents(
            pillars_present=PillarsInfo(solar=f.bool(), vortex=f.bool(), nebula=f.bool(), stardust=f.bool()),
            are_active=f.bool(),
        )

        party_center_active = f.bool()
        party_natural_active = f.bool()
        party_cooldown = f.int4()
        partying_npcs_count = f.int4()
        partying_npcs = []
        for _ in range(partying_npcs_count):
            partying_npcs.append(f.int4())
        party = Party(
            is_doomed=party_is_doomed,
            thrown_by_party_center=party_center_active,
            thrown_by_npcs=party_natural_active,
            cooldown=party_cooldown,
            partying_npcs=partying_npcs,
        )

        sandstorm = Sandstorm(is_active=f.bool(), time_left=f.int4(), severity=f.single(), intended_severity=f.single())

        saved_bartender = f.bool()

        old_ones_army = OldOnesArmyTiers(f.bool(), f.bool(), f.bool())

        # ToDo: Figure out which biomes got new BGs.
        # Oasis and Graveyard probably got new backgrounds.
        bg_mushroom = f.int1()
        bg_underworld = f.int1()
        bg_forest_2 = f.int1()  # Maybe oasis.
        bg_forest_3 = f.int1()
        bg_forest_4 = f.int1()

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

        combat_book_used = f.bool()

        lantern_night = LanternNight(
            nights_on_cooldown=f.int4(),
            genuine=f.bool(),
            manual=f.bool(),
            next_night_is_lantern_night=f.bool()
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

        treetop_variant_count = f.int4()
        treetop_variants = TreetopVariants([f.int4() for _ in range(treetop_variant_count)])

        halloween_today = f.bool()
        xmas_today = f.bool()

        ore_1 = BlockType(f.int4())
        ore_2 = BlockType(f.int4())
        ore_3 = BlockType(f.int4())
        ore_4 = BlockType(f.int4())
        saved_ore_tiers = SavedOreTiers(ore_1, ore_2, ore_3, ore_4, hardmode_ore_1, hardmode_ore_2, hardmode_ore_3)

        pets = Pets(cat=f.bool(), dog=f.bool(), bunny=f.bool())

        defeated_empress_of_light = f.bool()
        defeated_queen_slime = f.bool()
        defeated_deerclops = f.bool()

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

        saved_slime_nerdy = f.bool()
        saved_merchant = f.bool()
        saved_demolitionist = f.bool()
        saved_party_girl = f.bool()
        saved_dye_trader = f.bool()
        saved_truffle = f.bool()
        saved_arms_dealer = f.bool()
        saved_nurse = f.bool()
        saved_princess = f.bool()
        combat_book_2_used = f.bool()
        peddler_satchel_used = f.bool()
        saved_slime_cool = f.bool()
        saved_slime_elder = f.bool()
        saved_slime_clumsy = f.bool()
        saved_slime_diva = f.bool()
        saved_slime_surly = f.bool()
        saved_slime_mystic = f.bool()
        saved_slime_squire = f.bool()

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

        moondial_is_running = f.bool()
        moondial_cooldown = f.uint1()

        time = Time(
            current=current_time,
            is_daytime=is_daytime,
            moon_phase=moon_phase,
            sundial_cooldown=sundial_cooldown,
            sundial_is_running=sundial_is_running,
            moondial_cooldown=moondial_cooldown,
            moondial_is_running=moondial_is_running,
        )

        unknown_world_header_data = f.read_until(pointers.world_tiles)

        # Tiles
        tm = cls._create_tilematrix(f, world_size, tileframeimportant)

        unknown_world_tiles_data = f.read_until(pointers.chests)

        # Chests
        chests = []

        chests_count = f.int2()
        chests_max_items = f.int2()

        for _ in range(chests_count):
            chest_position = Coordinates(x=f.int4(), y=f.int4())
            chest_name = f.string()
            chest_contents = []

            for _ in range(chests_max_items):
                item_quantity = f.int2()
                if item_quantity > 0:
                    item_type = ItemType(f.int4())
                    item_modifier = PrefixType.get(f.uint1())
                    item = ItemStack(quantity=item_quantity, type_=item_type, prefix=item_modifier)
                else:
                    item = None
                chest_contents.append(item)
            chest = Chest(position=chest_position, name=chest_name, contents=chest_contents)
            chests.append(chest)
            tm[chest.position].extra = chest

        unknown_chests_data = f.read_until(pointers.signs)

        # Signs
        signs = []

        signs_count = f.int2()

        for _ in range(signs_count):
            sign = Sign(text=f.string(), position=Coordinates(f.int4(), f.int4()))
            signs.append(sign)
            tm[sign.position].extra = sign

        unknown_signs_data = f.read_until(pointers.npcs)

        # Entities
        npcs = []
        mobs = []

        shimmered_npcs_count = f.int4()
        shimmered_npcs = []
        for _ in range(shimmered_npcs_count):
            shimmered_npcs.append(f.int4())

        while f.bool():
            npc_type = EntityType(f.int4())
            npc_name = f.string()
            npc_position = Coordinates(f.single(), f.single())
            is_homeless = f.bool()
            npc_home = Coordinates(f.int4(), f.int4())
            if is_homeless:
                npc_home = None

            npc_flags = f.bits()
            npc_variation_index = f.int4() if npc_flags[0] else 0

            npc = NPC(
                type_=npc_type, name=npc_name, position=npc_position, home=npc_home, variation_index=npc_variation_index
            )
            npcs.append(npc)

        while f.bool():
            mob_type = EntityType(f.int4())
            mob_position = Coordinates(f.single(), f.single())

            mob = Mob(type_=mob_type, position=mob_position)
            mobs.append(mob)

        unknown_npcs_data = f.read_until(pointers.tile_entities)

        # Tile entities
        tile_entities_count = f.int4()
        tile_entities = []

        for _ in range(tile_entities_count):
            te_type = f.uint1()
            te_id = f.int4()
            te_position = Coordinates(f.int2(), f.int2())
            # Target Dummy
            if te_type == 0:
                te_extra = TargetDummy(npc=f.int2())
            # Item Frame
            elif te_type == 1:
                te_extra = ItemFrame(
                    item=ItemStack(type_=ItemType(f.int2()), prefix=PrefixType.get(f.uint1()), quantity=f.int2())
                )
            # Logic Sensor
            elif te_type == 2:
                te_extra = LogicSensor(logic_check=f.uint1(), enabled=f.bool())
            # Mannequin
            elif te_type == 3:
                item_flags = f.bits()
                dye_flags = f.bits()
                mannequin_items: List[Optional[ItemStack]] = [None for _ in range(len(item_flags))]
                mannequin_dyes: List[Optional[ItemStack]] = [None for _ in range(len(dye_flags))]
                for index, flag in enumerate(item_flags):
                    if not flag:
                        continue
                    mannequin_items[index] = ItemStack(
                        type_=ItemType(f.int2()), prefix=PrefixType.get(f.int1()), quantity=f.int2()
                    )
                for index, flag in enumerate(dye_flags):
                    if not flag:
                        continue
                    mannequin_dyes[index] = ItemStack(
                        type_=ItemType(f.int2()), prefix=PrefixType.get(f.int1()), quantity=f.int2()
                    )
                te_extra = Mannequin(mannequin_items, mannequin_dyes)
            # Weapon Rack
            elif te_type == 4:
                rack_item = ItemStack(type_=ItemType(f.int2()), prefix=PrefixType.get(f.int1()), quantity=f.int2())
                te_extra = WeaponRack(rack_item)
            # Hat Rack
            elif te_type == 5:
                # This isn't 100% tested, but the first two flags should be items, and the second two should be dyes.
                item_flags = f.bits()
                # Maximum of two items slots and two dye slots.
                rack_items: List[Optional[ItemStack]] = [None for _ in range(2)]
                rack_dyes: List[Optional[ItemStack]] = [None for _ in range(2)]
                for index, flag in enumerate(item_flags[0:2]):
                    if not flag:
                        continue
                    rack_items[index] = ItemStack(
                        type_=ItemType(f.int2()), prefix=PrefixType.get(f.int1()), quantity=f.int2()
                    )
                for index, flag in enumerate(item_flags[2:4]):
                    if not flag:
                        continue
                    rack_dyes[index] = ItemStack(
                        type_=ItemType(f.int2()), prefix=PrefixType.get(f.int1()), quantity=f.int2()
                    )
                te_extra = HatRack(rack_items, rack_dyes)
            # Food Plate
            elif te_type == 6:
                plate_item = ItemStack(type_=ItemType(f.int2()), prefix=PrefixType.get(f.int1()), quantity=f.int2())
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

        unknown_tile_entities_data = f.read_until(pointers.pressure_plates)

        # Weighed Pressure Plates
        weighed_pressure_plates_count = f.int4()
        weighed_pressure_plates = []

        for _ in range(weighed_pressure_plates_count):
            wpp = WeighedPressurePlate(position=Coordinates(f.int4(), f.int4()))
            weighed_pressure_plates.append(wpp)
            tm[wpp.position].extra = wpp

        unknown_pressure_plates_data = f.read_until(pointers.town_manager)

        # Town Manager
        rooms_count = f.int4()
        rooms = []

        for _ in range(rooms_count):
            room = Room(npc=EntityType(f.int4()), position=Coordinates(f.int4(), f.int4()))
            rooms.append(room)

        unknown_town_manager_data = f.read_until(pointers.bestiary)

        bestiary_kills = {}
        for _ in range(f.int4()):
            entity = EntityType[f.string()]
            kills = f.int4()
            bestiary_kills[entity] = kills

        bestiary_sightings = [EntityType[f.string()] for _ in range(f.int4())]
        bestiary_chats = [EntityType[f.string()] for _ in range(f.int4())]

        bestiary = Bestiary(chats=bestiary_chats, kills=bestiary_kills, sightings=bestiary_sightings)

        unknown_bestiary_data = f.read_until(pointers.journey_powers)

        journey_powers = JourneyPowers()
        while f.bool():
            power_id = f.int2()
            if power_id == 0:
                journey_powers.freeze_time = f.bool()
            elif power_id == 8:
                journey_powers.time_rate = f.single()
            elif power_id == 9:
                journey_powers.freeze_rain = f.bool()
            elif power_id == 10:
                journey_powers.freeze_wind = f.bool()
            elif power_id == 12:
                journey_powers.difficulty = f.single()
            elif power_id == 13:
                journey_powers.freeze_biome_spread = f.bool()

        unknown_journey_powers_data = f.read_until(pointers.footer)

        # Object creation
        world = cls(
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
        if not f.bool():
            raise InvalidFooterError("Invalid footer")
        if not f.string() == world.name:
            raise InvalidFooterError("Invalid footer")
        if not f.int4() == world.id:
            raise InvalidFooterError("Invalid footer")

        f.file.close()

        return world


__all__ = (
    "World",
)


if __name__ == "__main__":
    world = World.create_from_file(sys.argv[1])
    breakpoint()
