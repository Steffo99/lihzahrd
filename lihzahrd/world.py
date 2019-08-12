import uuid
import math
import typing
from .fileutils import *
from .header import *
from .tiles import *
from .chests import *
from .signs import *
from .npcs import *
from .timer import Timer


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
                 altars_smashed: AltarsSmashed,
                 is_hardmode: bool,
                 shadow_orbs: ShadowOrbs,
                 bosses_defeated: BossesDefeated,
                 anglers_quest: AnglerQuest,
                 clouds: Clouds,
                 cultist_delay: int,
                 tiles: typing.List[typing.List[Tile]],
                 chests: typing.List[Chest],
                 unknown_file_format_data: bytearray,
                 unknown_world_header_data: bytearray,
                 unknown_world_tiles_data: bytearray,
                 unknown_chests_data: bytearray):

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

        self.altars_smashed: AltarsSmashed = altars_smashed
        """Information related to the destruction of Demon Altars with a Pwnhammer."""

        self.is_hardmode: bool = is_hardmode
        """Whether or not the world is in hardmode."""

        self.shadow_orbs: ShadowOrbs = shadow_orbs
        """Information related to the Shadow Orbs or Crimson Hearts in the world."""

        self.bosses_defeated: BossesDefeated = bosses_defeated
        """Which bosses have been defeated in the world."""

        self.anglers_quest: AnglerQuest = anglers_quest
        """Information about today's Angler's Quest."""

        self.chests: typing.List[Chest] = chests

        self.tiles: typing.List[typing.List[Tile]] = tiles

        self.clouds: Clouds = clouds
        self.cultist_delay: int = cultist_delay
        self.unknown_file_format_data: bytearray = unknown_file_format_data
        self.unknown_world_header_data: bytearray = unknown_world_header_data
        self.unknown_world_tiles_data: bytearray = unknown_world_tiles_data
        self.unknown_chests_data: bytearray = unknown_chests_data

    def __repr__(self):
        return f'<World "{self.name}">'

    @property
    def crimson_hearts(self) -> ShadowOrbs:
        return self.shadow_orbs

    @crimson_hearts.setter
    def crimson_hearts(self, value):
        self.shadow_orbs = value

    @staticmethod
    def _read_tile_block(fr: FileReader, tileframeimportant) -> typing.List:
        # Once again, this code is a mess
        flags1 = fr.bits()
        has_block = flags1[1]
        has_wall = flags1[2]
        liquid_type = LiquidType.from_flags(flags1)
        has_extended_block_id = flags1[5]
        rle_compression = RLEEncoding.from_flags(flags1)
        if flags1[0]:
            flags2 = fr.bits()
            block_shape = Shape.from_flags(flags2)
            if flags2[0]:
                flags3 = fr.bits()
                is_block_active = not flags3[2]
                wiring = Wiring.from_flags(flags2, flags3)
                is_block_painted = flags3[3]
                is_wall_painted = flags3[4]
            else:
                is_block_active = True
                wiring = Wiring.from_flags(flags2)
                is_block_painted = False
                is_wall_painted = False
        else:
            block_shape = Shape.NORMAL
            is_block_active = True
            wiring = None
            is_block_painted = False
            is_wall_painted = False
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
            block = Block(type_=block_type,
                          frame=frame,
                          paint=block_paint,
                          is_active=is_block_active,
                          shape=block_shape)
        else:
            block = None
        if has_wall:
            wall_id = WallType(fr.uint1())
            if is_wall_painted:
                wall_paint = fr.uint1()
            else:
                wall_paint = None
            wall = Wall(type_=wall_id, paint=wall_paint)
        else:
            wall = None
        if liquid_type != LiquidType.NO_LIQUID:
            liquid = Liquid(type_=liquid_type, volume=fr.uint1())
        else:
            liquid = None
        if rle_compression == RLEEncoding.DOUBLE_BYTE:
            multiply_by = fr.uint2() + 1
        elif rle_compression == RLEEncoding.SINGLE_BYTE:
            multiply_by = fr.uint1() + 1
        else:
            multiply_by = 1
        tile = Tile(block=block, wall=wall, liquid=liquid, wiring=wiring)
        return [tile] * multiply_by

    @classmethod
    def create_from_file(cls, file):
        """Create a World object from a .wld file."""
        # This code is a mess.

        f = FileReader(file)

        with Timer("File Format", display=True):
            version = Version(f.int4())
            relogic = f.string(7)
            savefile_type = f.uint1()
            if version != Version("1.3.5.3") or relogic != "relogic" or savefile_type != 2:
                raise NotImplementedError("This parser can only read Terraria 1.3.5.3 save files.")

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

        with Timer("World Header", display=True):
            name = f.string()

            generator = GeneratorInfo(f.string(), f.int4())

            uuid_ = f.uuid()
            id_ = f.int8()
            bounds = f.rect()
            world_size = Coordinates(y=f.int4(), x=f.int4())
            is_expert = f.bool()
            created_on = f.datetime()

            world_styles = Styles(moon=MoonStyle(f.uint1()),
                                  trees=FourPartSplit(separators=[f.int4(), f.int4(), f.int4()],
                                                      properties=[f.int4(),
                                                                  f.int4(),
                                                                  f.int4(),
                                                                  f.int4()]),
                                  moss=FourPartSplit(separators=[f.int4(), f.int4(), f.int4()],
                                                     properties=[f.int4(),
                                                                 f.int4(),
                                                                 f.int4(),
                                                                 f.int4()]))

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

            shadow_orbs = ShadowOrbs(smashed_at_least_once=f.bool(),
                                     spawn_meteorite=f.bool(),
                                     evil_boss_counter=f.int4())

            smashed_altars_count = f.int4()

            is_hardmode = f.bool()

            invasion_delay = f.int4()
            invasion_size = f.int4()
            invasion_type = InvasionType(f.int4())
            invasion_position = f.double()

            time_left_slime_rain = f.double()

            sundial_cooldown = f.uint1()

            rain = Rain(is_active=f.bool(), time_left=f.int4(), max_rain=f.single())

            hardmode_ore_1 = HardmodeTier1Ore(f.int4())
            hardmode_ore_2 = HardmodeTier2Ore(f.int4())
            hardmode_ore_3 = HardmodeTier3Ore(f.int4())
            altars_smashed = AltarsSmashed(count=smashed_altars_count,
                                           ore_tier1=hardmode_ore_1,
                                           ore_tier2=hardmode_ore_2,
                                           ore_tier3=hardmode_ore_3)

            bg_forest = f.int1()
            bg_corruption = f.int1()
            bg_jungle = f.int1()
            bg_snow = f.int1()
            bg_hallow = f.int1()
            bg_crimson = f.int1()
            bg_desert = f.int1()
            bg_ocean = f.int1()

            backgrounds = Backgrounds(bg_underground_snow=bg_underground_snow,
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

            clouds = Clouds(bg_cloud=f.int4(), cloud_number=f.int2(), wind_speed=f.single())

            angler_today_quest_completed_by_count = f.uint1()
            angler_today_quest_completed_by = []
            for _ in range(angler_today_quest_completed_by_count):
                angler_today_quest_completed_by.append(f.string())

            saved_angler = f.bool()

            angler_today_quest_target = AnglerQuestFish(f.int4())
            anglers_quest = AnglerQuest(current_goal=angler_today_quest_target,
                                        completed_by=angler_today_quest_completed_by)

            saved_stylist = f.bool()
            saved_tax_collector = f.bool()

            invasion_size_start = f.int4()  # ???
            invasion = Invasion(delay=invasion_delay,
                                size=invasion_size,
                                type_=invasion_type,
                                position=invasion_position,
                                size_start=invasion_size_start)

            cultist_delay = f.int4()  # ???
            mob_types_count = f.int2()
            mob_kills = {}
            for mob_id in range(mob_types_count):
                mob_kills[mob_id] = f.int4()

            fast_forward_time = f.bool()
            time = Time(current=current_time,
                        is_daytime=is_daytime,
                        moon_phase=moon_phase,
                        sundial_cooldown=sundial_cooldown,
                        fast_forward_time=fast_forward_time)

            defeated_duke_fishron = f.bool()
            defeated_moon_lord = f.bool()
            defeated_pumpking = f.bool()
            defeated_mourning_wood = f.bool()
            defeated_ice_queen = f.bool()
            defeated_santa_nk1 = f.bool()
            defeated_everscream = f.bool()
            defeated_pillars = PillarsInfo(solar=f.bool(), vortex=f.bool(), nebula=f.bool(), stardust=f.bool())

            lunar_events = LunarEvents(pillars_present=PillarsInfo(solar=f.bool(),
                                                                   vortex=f.bool(),
                                                                   nebula=f.bool(),
                                                                   stardust=f.bool()),
                                       are_active=f.bool())

            party_center_active = f.bool()
            party_natural_active = f.bool()
            party_cooldown = f.int4()
            partying_npcs_count = f.int4()
            partying_npcs = []
            for _ in range(partying_npcs_count):
                partying_npcs.append(f.int4())
            party = Party(thrown_by_party_center=party_center_active,
                          thrown_by_npcs=party_natural_active,
                          cooldown=party_cooldown,
                          partying_npcs=partying_npcs)

            sandstorm = Sandstorm(is_active=f.bool(),
                                  time_left=f.int4(),
                                  severity=f.single(),
                                  intended_severity=f.single())

            events = Events(blood_moon=blood_moon,
                            solar_eclipse=eclipse,
                            invasion=invasion,
                            slime_rain=time_left_slime_rain,
                            rain=rain,
                            party=party,
                            sandstorm=sandstorm,
                            lunar_events=lunar_events)

            saved_bartender = f.bool()
            saved_npcs = SavedNPCs(goblin_tinkerer=saved_goblin_tinkerer,
                                   wizard=saved_wizard,
                                   mechanic=saved_mechanic,
                                   angler=saved_angler,
                                   stylist=saved_stylist,
                                   tax_collector=saved_tax_collector,
                                   bartender=saved_bartender)

            old_ones_army = OldOnesArmyTiers(f.bool(), f.bool(), f.bool())

            bosses_defeated = BossesDefeated(eye_of_cthulhu=defeated_eye_of_cthulhu,
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
                                             old_ones_army=old_ones_army)

            unknown_world_header_data = f.read_until(pointers.world_tiles)

        with Timer("World Tiles", display=True):
            tiles = []
            while len(tiles) < world_size.x:
                column = []
                while len(column) < world_size.y:
                    readtiles = cls._read_tile_block(f, tileframeimportant)
                    column = [*column, *readtiles]
                tiles.append(column)

            unknown_world_tiles_data = f.read_until(pointers.chests)

        with Timer("Chests", display=True):
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
                        item_modifier = f.uint1()
                        item = ItemStack(quantity=item_quantity,
                                         type_=item_type,
                                         modifier=item_modifier)
                    else:
                        item = None
                    chest_contents.append(item)
                chest = Chest(position=chest_position,
                              name=chest_name,
                              contents=chest_contents)
                chests.append(chest)

            unknown_chests_data = f.read_until(pointers.signs)

        with Timer("Signs", display=True):
            signs = []

            signs_count = f.int2()

            for _ in range(signs_count):
                sign = Sign(text=f.string(),
                            position=Coordinates(f.int4(), f.int4()))

            unknown_signs_data = f.read_until(pointers.npcs)

        with Timer("NPCs", display=True):
            npcs = []

            while f.bool():
                npc_sprite_id = f.int4()
                npc_name = f.string()
                npc_position = Coordinates(f.single(), f.single())
                is_homeless = f.bool()
                npc_home = Coordinates(f.int4(), f.int4())
                if is_homeless:
                    npc_home = None

                npc = NPC(sprite_id=npc_sprite_id,
                          name=npc_name,
                          position=npc_position,
                          home=npc_home)
                npcs.append(npc)

        world = World(version=version, savefile_type=savefile_type, revision=revision, is_favorite=is_favorite,
                      name=name, generator=generator, uuid_=uuid_, id_=id_, bounds=bounds, size=world_size,
                      is_expert=is_expert, created_on=created_on, styles=world_styles, backgrounds=backgrounds,
                      spawn_point=spawn_point, underground_level=underground_level, cavern_level=cavern_level,
                      time=time, events=events, dungeon_point=dungeon_point, world_evil=world_evil,
                      saved_npcs=saved_npcs, altars_smashed=altars_smashed, is_hardmode=is_hardmode,
                      shadow_orbs=shadow_orbs, bosses_defeated=bosses_defeated, anglers_quest=anglers_quest,
                      clouds=clouds, cultist_delay=cultist_delay, tiles=tiles, chests=chests,
                      unknown_file_format_data=unknown_file_format_data,
                      unknown_world_header_data=unknown_world_header_data,
                      unknown_world_tiles_data=unknown_world_tiles_data,
                      unknown_chests_data=unknown_chests_data)
        return world
