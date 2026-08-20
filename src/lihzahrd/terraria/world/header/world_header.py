# language=rst
"""
Submodule containing :class:`.WorldHeader`.
"""

from logging import getLogger
from typing import Self, override

from lihzahrd.terraria.common.file_version import FileVersion
from lihzahrd.terraria.utils.pack.composite.composite import PackComposite as PaCo
from lihzahrd.terraria.utils.pack.pack import Pack
from lihzahrd.terraria.utils.pack.primitive.coordinates import PackCoordinatesInt
from lihzahrd.terraria.utils.pack.primitive.date import PackDatetime
from lihzahrd.terraria.utils.pack.primitive.uuid_ import PackUUID
from lihzahrd.terraria.world.header.altar_count import AltarCount
from lihzahrd.terraria.world.header.banner_claimable_counts import BannerClaimableCounts
from lihzahrd.terraria.world.header.banner_kill_counts import BannerKillCounts
from lihzahrd.terraria.world.header.enemy_defeated import EnemyDefeated
from lihzahrd.terraria.world.header.cavern_background import CavernBackground
from lihzahrd.terraria.world.header.clock import Clock
from lihzahrd.terraria.world.header.cloud_background_active import CloudBackgroundActive
from lihzahrd.terraria.world.header.cloud_count import CloudCount
from lihzahrd.terraria.world.header.coinrain_remaining import CoinRainRemaining
from lihzahrd.terraria.world.header.corruption_background import CorruptionBackground
from lihzahrd.terraria.world.header.crimson_background import CrimsonBackground
from lihzahrd.terraria.world.header.cultists_cooldown import CultistsCooldown
from lihzahrd.terraria.world.header.daytime import Daytime
from lihzahrd.terraria.world.header.desert_background import DesertBackground
from lihzahrd.terraria.world.header.event_ongoing import EventOngoing
from lihzahrd.terraria.world.header.fishingquest_completedby import FishingQuestCompletedBy
from lihzahrd.terraria.world.header.fishingquest_goal import FishingQuestGoal
from lihzahrd.terraria.world.header.forest_background import ForestBackground
from lihzahrd.terraria.world.header.forest_treetop import ForestTreetop
from lihzahrd.terraria.world.header.hallow_background import HallowBackground
from lihzahrd.terraria.world.header.hell_background import HellBackground
from lihzahrd.terraria.world.header.ice_background import IceBackground
from lihzahrd.terraria.world.header.invasion_delay import InvasionDelay
from lihzahrd.terraria.world.header.invasion_position import InvasionPosition
from lihzahrd.terraria.world.header.invasion_power import InvasionPower
from lihzahrd.terraria.world.header.invasion_kind import InvasionKind
from lihzahrd.terraria.world.header.jungle_surface_background import JungleSurfaceBackground
from lihzahrd.terraria.world.header.jungle_underground_background import JungleUndergroundBackground
from lihzahrd.terraria.world.header.lanternnight_celebration_active import LanternNightCelebrationActive
from lihzahrd.terraria.world.header.lanternnight_celebration_scheduled import LanternNightCelebrationScheduled
from lihzahrd.terraria.world.header.lanternnight_spontaneous_active import LanternNightSpontaneousActive
from lihzahrd.terraria.world.header.lanternnight_spontaneous_cooldown import LanternNightSpontaneousCooldown
from lihzahrd.terraria.world.header.meteorite_scheduled import MeteoriteScheduled
from lihzahrd.terraria.world.header.meteorshower_remaining import MeteorShowerRemaining
from lihzahrd.terraria.world.header.milestone import Milestone
from lihzahrd.terraria.world.header.moon_phase import MoonPhase
from lihzahrd.terraria.world.header.moon_style import MoonStyle
from lihzahrd.terraria.world.header.mushroom_background import MushroomBackground
from lihzahrd.terraria.world.header.npc_rescued import NPCRescued
from lihzahrd.terraria.world.header.ocean_background import OceanBackground
from lihzahrd.terraria.world.header.ore_available import OreAvailable
from lihzahrd.terraria.world.header.treetops import Treetops
from lihzahrd.terraria.world.header.party_center_active import PartyCenterActive
from lihzahrd.terraria.world.header.party_partecipants import PartyPartecipants
from lihzahrd.terraria.world.header.party_spontaneous_active import PartySpontaneousActive
from lihzahrd.terraria.world.header.party_spontaneous_cooldown import PartySpontaneousCooldown
from lihzahrd.terraria.world.header.rain_duration import RainDuration
from lihzahrd.terraria.world.header.rain_strength import RainStrength
from lihzahrd.terraria.world.header.sandstorm_duration import SandstormDuration
from lihzahrd.terraria.world.header.sandstorm_severity import SandstormSeverity
from lihzahrd.terraria.world.header.secret_seed_active import SecretSeedActive
from lihzahrd.terraria.world.header.secret_teams_spawns import SecretTeamsSpawns
from lihzahrd.terraria.world.header.shadow_orb_count import ShadowOrbCount
from lihzahrd.terraria.world.header.slimerain_duration import SlimeRainDuration
from lihzahrd.terraria.world.header.snow_background import SnowBackground
from lihzahrd.terraria.world.header.special_seed_active import SpecialSeedActive
from lihzahrd.terraria.world.header.timedial_cooldown import TimedialCooldown
from lihzahrd.terraria.world.header.timedial_running import TimedialRunning
from lihzahrd.terraria.world.header.underworld_background import UnderworldBackground
from lihzahrd.terraria.world.header.wind_speed import WindSpeed
from lihzahrd.terraria.world.header.world_bounds import WorldBounds
from lihzahrd.terraria.world.header.world_difficulty import PackWorldDifficulty
from lihzahrd.terraria.world.header.world_evil import WorldEvil
from lihzahrd.terraria.world.header.world_generator_seed import WorldGeneratorSeed
from lihzahrd.terraria.world.header.world_generator_version import WorldGeneratorVersion
from lihzahrd.terraria.world.header.world_id import WorldID
from lihzahrd.terraria.world.header.world_layer_boundary import WorldLayerBoundary
from lihzahrd.terraria.world.header.world_manifest import WorldManifest
from lihzahrd.terraria.world.header.world_mode import WorldMode
from lihzahrd.terraria.world.header.world_name import WorldName
from lihzahrd.terraria.world.header.world_size import WorldSize
from lihzahrd.terraria.world.header.world_style_boundary import WorldStyleBoundary


class WorldHeader(PaCo):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.composite.PackComposite` to process all metadata contained inside a Terraria world's header.
    """

    _LOG = getLogger(__name__)

    # For easier future updates, do not nest other PackableComposite inside this one.

    name: PaCo.Field[Self, WorldName] = PaCo.Field(WorldName)
    "The name of the world."

    generator_seed: PaCo.Field[Self, WorldGeneratorSeed] = PaCo.Field(WorldGeneratorSeed)
    "The seed used to generate the world."

    generator_version: PaCo.Field[Self, WorldGeneratorVersion] = PaCo.Field(WorldGeneratorVersion)
    "The version of the used world generator."

    uuid: PaCo.Field[Self, PackUUID] = PaCo.Field(PackUUID)
    "The UUID of the world."

    id: PaCo.Field[Self, WorldID] = PaCo.Field(WorldID)
    "The ID of the world."

    bounds: PaCo.Field[Self, WorldBounds] = PaCo.Field(WorldBounds)
    "The camera bounds of the world."

    size: PaCo.Field[Self, WorldSize] = PaCo.Field(WorldSize)
    "The size in tiles of the world."

    difficulty: PaCo.Field[Self, PackWorldDifficulty] = PaCo.Field(PackWorldDifficulty)
    "The difficulty of the world."

    special_drunk: PaCo.Field[Self, SpecialSeedActive] = PaCo.Field(SpecialSeedActive)
    "If the world uses the special seed *Drunk world*."

    special_fortheworthy: PaCo.Field[Self, SpecialSeedActive] = PaCo.Field(SpecialSeedActive)
    "If the world uses the special seed *For the Worthy*."

    special_anniversary: PaCo.Field[Self, SpecialSeedActive] = PaCo.Field(SpecialSeedActive)
    "If the world uses the special seed *10th Anniversary*."

    special_dontstarve: PaCo.Field[Self, SpecialSeedActive] = PaCo.Field(SpecialSeedActive)
    "If the world uses the special seed *Don't Starve*."

    special_notthebees: PaCo.Field[Self, SpecialSeedActive] = PaCo.Field(SpecialSeedActive)
    "If the world uses the special seed *Not the bees*."

    special_remix: PaCo.Field[Self, SpecialSeedActive] = PaCo.Field(SpecialSeedActive)
    "If the world uses the special seed *Remix*."

    special_notraps: PaCo.Field[Self, SpecialSeedActive] = PaCo.Field(SpecialSeedActive)
    "If the world uses the special seed *No traps*."

    special_zenith: PaCo.Field[Self, SpecialSeedActive] = PaCo.Field(SpecialSeedActive)
    "If the world uses the special seed *Zenith*."

    special_skyblock: PaCo.Field[Self, SpecialSeedActive] = PaCo.Field(SpecialSeedActive)
    "If the world uses the special seed *Skyblock*."

    created_on: PaCo.Field[Self, PackDatetime] = PaCo.Field(PackDatetime)
    "The timestamp of when the world was generated."

    last_saved_on: PaCo.Field[Self, PackDatetime] = PaCo.Field(PackDatetime)
    "The timestamp of when the world was last saved."

    moon_style: PaCo.Field[Self, MoonStyle] = PaCo.Field(MoonStyle)
    "The style of the moon in the world."

    forest_boundary_a_b: PaCo.Field[Self, WorldStyleBoundary] = PaCo.Field(WorldStyleBoundary)
    "The vertical boundary separating the forest styles A and B."

    forest_boundary_b_c: PaCo.Field[Self, WorldStyleBoundary] = PaCo.Field(WorldStyleBoundary)
    "The vertical boundary separating the forest styles B and C."

    forest_boundary_c_d: PaCo.Field[Self, WorldStyleBoundary] = PaCo.Field(WorldStyleBoundary)
    "The vertical boundary separating the forest styles C and D."

    forest_treetop_a: PaCo.Field[Self, ForestTreetop] = PaCo.Field(ForestTreetop)
    "The treetop style that the trees in the forest area A have."

    forest_treetop_b: PaCo.Field[Self, ForestTreetop] = PaCo.Field(ForestTreetop)
    "The treetop style that the trees in the forest area B have."

    forest_treetop_c: PaCo.Field[Self, ForestTreetop] = PaCo.Field(ForestTreetop)
    "The treetop style that the trees in the forest area C have."

    forest_treetop_d: PaCo.Field[Self, ForestTreetop] = PaCo.Field(ForestTreetop)
    "The treetop style that the trees in the forest area D have."

    cavern_boundary_a_b: PaCo.Field[Self, WorldStyleBoundary] = PaCo.Field(WorldStyleBoundary)
    "The vertical boundary separating the cavern styles A and B."

    cavern_boundary_b_c: PaCo.Field[Self, WorldStyleBoundary] = PaCo.Field(WorldStyleBoundary)
    "The vertical boundary separating the cavern styles B and C."

    cavern_boundary_c_d: PaCo.Field[Self, WorldStyleBoundary] = PaCo.Field(WorldStyleBoundary)
    "The vertical boundary separating the cavern styles C and D."

    cavern_background_a: PaCo.Field[Self, CavernBackground] = PaCo.Field(CavernBackground)
    "The treetop style that the trees in the cavern area A have."

    cavern_background_b: PaCo.Field[Self, CavernBackground] = PaCo.Field(CavernBackground)
    "The treetop style that the trees in the cavern area B have."

    cavern_background_c: PaCo.Field[Self, CavernBackground] = PaCo.Field(CavernBackground)
    "The treetop style that the trees in the cavern area C have."

    cavern_background_d: PaCo.Field[Self, CavernBackground] = PaCo.Field(CavernBackground)
    "The treetop style that the trees in the cavern area D have."

    ice_background: PaCo.Field[Self, IceBackground] = PaCo.Field(IceBackground)
    "The background of the underground ice biome."

    jungle_underground_background: PaCo.Field[Self, JungleUndergroundBackground] = PaCo.Field(
        JungleUndergroundBackground
    )
    "The background of the underground jungle biome."

    hell_background: PaCo.Field[Self, HellBackground] = PaCo.Field(HellBackground)
    "The background of the hell biome."

    point_spawn: PaCo.Field[Self, PackCoordinatesInt] = PaCo.Field(PackCoordinatesInt)
    "The spawn point of the world."

    underground_surface_boundary: PaCo.Field[Self, WorldLayerBoundary] = PaCo.Field(WorldLayerBoundary)
    "The horizontal boundary separating surface from underground."

    cavern_underground_boundary: PaCo.Field[Self, WorldLayerBoundary] = PaCo.Field(WorldLayerBoundary)
    "The horizontal boundary separating underground from cavern."

    clock_time: PaCo.Field[Self, Clock] = PaCo.Field(Clock)
    "The current clock time of the world."

    day_time: PaCo.Field[Self, Daytime] = PaCo.Field(Daytime)
    "Whether it's day or night in the world."

    moon_phase: PaCo.Field[Self, MoonPhase] = PaCo.Field(MoonPhase)
    "The current moon phase of the world."

    bloodmoon_ongoing: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether a blood moon is currently ongoing in the world."

    eclipse_ongoing: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether a solar eclipse is currently ongoing in the world."

    point_dungeon: PaCo.Field[Self, PackCoordinatesInt] = PaCo.Field(PackCoordinatesInt)
    "The spawn point of the Old Man."

    evil: PaCo.Field[Self, WorldEvil] = PaCo.Field(WorldEvil)
    "The main evil of the world: Corruption or Crimson."

    defeated_eyeofcthulhu: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Eye of Cthulhu* was defeated at least once in the world."

    defeated_eaterofworlds: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Eater of Worlds* was defeated at least once in the world."

    defeated_skeletron: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Skeletron* was defeated at least once in the world."

    defeated_queenbee: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Queen Bee* was defeated at least once in the world."

    defeated_thetwins: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *The Twins* were defeated at least once in the world."

    defeated_thedestroyer: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *The Destroyer* was defeated at least once in the world."

    defeated_skeletronprime: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Skeletron Prime* was defeated at least once in the world."

    defeated_anymechanicalboss: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether any mechanical boss was defeated at least once in the world."

    defeated_plantera: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Plantera* was defeated at least once in the world."

    defeated_golem: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Golem* was defeated at least once in the world."

    defeated_kingslime: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *King Slime* was defeated at least once in the world."

    rescued_goblin: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Goblin Tinkerer* NPC was rescued and can now arrive automatically."

    rescued_wizard: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Wizard* NPC was rescued and can now arrive automatically."

    rescued_mechanic: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Mechanic* NPC was rescued and can now arrive automatically."

    defeated_goblinarmy: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Goblin Army* was repelled at least once in the world."

    defeated_clown: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether a *Clown* was defeated at least once in the world."

    defeated_frostlegion: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Frost Legion* was repelled at least once in the world."

    defeated_pirateinvasion: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Pirate Invasion* was repelled at least once in the world."

    shadoworb_smashed: PaCo.Field[Self, Milestone] = PaCo.Field(Milestone)
    "Whether a *Shadow Orb* was smashed at least once in the world."

    meteorite_scheduled: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether a meteorite is schedule to land as soon as possible."

    shadoworb_count: PaCo.Field[Self, ShadowOrbCount] = PaCo.Field(ShadowOrbCount)
    "How many shadow orbs or crimson hearts were broken in the world, and how many are left to summon the World Evil boss."

    altar_count: PaCo.Field[Self, AltarCount] = PaCo.Field(AltarCount)
    "How many demon or crimson altars were smashed in the world."

    mode: PaCo.Field[Self, WorldMode] = PaCo.Field(WorldMode)
    "The current world mode, either pre-hardmode or hardmode."

    party_doomed: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether all NPCs should die and be un-rescued when the current party ends."

    invasion_delay: PaCo.Field[Self, InvasionDelay] = PaCo.Field(InvasionDelay)
    "Unknown."

    invasion_power_left: PaCo.Field[Self, InvasionPower] = PaCo.Field(InvasionPower)
    "How many enemies still need to be defeated to repel the current invasion."

    invasion_kind: PaCo.Field[Self, InvasionKind] = PaCo.Field(InvasionKind)
    "The kind of the current invasion."

    invasion_position: PaCo.Field[Self, InvasionPosition] = PaCo.Field(InvasionPosition)
    "The position of the current invasion."

    slimerain_duration: PaCo.Field[Self, SlimeRainDuration] = PaCo.Field(SlimeRainDuration)
    "How long the current *Slime Rain* will last for."

    sundial_cooldown: PaCo.Field[Self, TimedialCooldown] = PaCo.Field(TimedialCooldown)
    "How much the *Sundial* is on cooldown for."

    rain_ongoing: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether it is raining or not."

    rain_duration: PaCo.Field[Self, RainDuration] = PaCo.Field(RainDuration)
    "How much it will still rain for."

    rain_strength: PaCo.Field[Self, RainStrength] = PaCo.Field(RainStrength)
    "How strong is the current rain."

    ore_cobalt_tier: PaCo.Field[Self, OreAvailable] = PaCo.Field(OreAvailable)
    "The first tier of hardmode ore selected to spawn in the world: either Cobalt or Palladium."

    ore_mythril_tier: PaCo.Field[Self, OreAvailable] = PaCo.Field(OreAvailable)
    "The second tier of hardmode ore selected to spawn in the world: either Mythril or Orichalcum."

    ore_adamantite_tier: PaCo.Field[Self, OreAvailable] = PaCo.Field(OreAvailable)
    "The third tier of hardmode ore selected to spawn in the world: either Adamantite or Titanium."

    forest_background_a: PaCo.Field[Self, ForestBackground] = PaCo.Field(ForestBackground)
    "The background of the forest biome in the forest area A."

    corruption_background: PaCo.Field[Self, CorruptionBackground] = PaCo.Field(CorruptionBackground)
    "The background of the corruption biome."

    jungle_surface_background: PaCo.Field[Self, JungleSurfaceBackground] = PaCo.Field(JungleSurfaceBackground)
    "The background of the surface jungle biome."

    snow_background: PaCo.Field[Self, SnowBackground] = PaCo.Field(SnowBackground)
    "The background of the surface snow biome."

    hallow_background: PaCo.Field[Self, HallowBackground] = PaCo.Field(HallowBackground)
    "The background of the hallow biome."

    crimson_background: PaCo.Field[Self, CrimsonBackground] = PaCo.Field(CrimsonBackground)
    "The background of the crimson biome."

    desert_background: PaCo.Field[Self, DesertBackground] = PaCo.Field(DesertBackground)
    "The background of the desert biome."

    ocean_background: PaCo.Field[Self, OceanBackground] = PaCo.Field(OceanBackground)
    "The background of the ocean biome."

    cloud_background_active: PaCo.Field[Self, CloudBackgroundActive] = PaCo.Field(CloudBackgroundActive)
    "Unknown."

    cloud_count: PaCo.Field[Self, CloudCount] = PaCo.Field(CloudCount)
    "Unknown."

    wind_speed: PaCo.Field[Self, WindSpeed] = PaCo.Field(WindSpeed)
    "The current wind speed and direction."

    fishingquest_completed_by: PaCo.Field[Self, FishingQuestCompletedBy] = PaCo.Field(FishingQuestCompletedBy)
    "Which players have completed the current fishing quest."

    rescued_angler: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Angler* NPC was rescued and can now arrive automatically."

    fishingquest_goal: PaCo.Field[Self, FishingQuestGoal] = PaCo.Field(FishingQuestGoal)
    "The current goal of the fishing quest."

    rescued_stylist: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Stylist* NPC was rescued and can now arrive automatically."

    rescued_taxcollector: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Tax Collector* NPC was rescued and can now arrive automatically."

    rescued_golfer: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Golfer* NPC was rescued and can now arrive automatically."

    invasion_power_total: PaCo.Field[Self, InvasionPower] = PaCo.Field(InvasionPower)
    """
    The total amount of enemies to defeat to repel the current invasion.
    
    The value of :attr:`.invasion_power_left` at the start of the current invasion.
    """

    cultists_cooldown: PaCo.Field[Self, CultistsCooldown] = PaCo.Field(CultistsCooldown)
    "Unknown."

    banner_kill_counts: PaCo.Field[Self, BannerKillCounts] = PaCo.Field(BannerKillCounts)
    "How many enemies of each type were killed, for banner drop purposes."

    banner_claimable_counts: PaCo.Field[Self, BannerClaimableCounts] = PaCo.Field(BannerClaimableCounts)
    "How many banners of each enemy type can be claimed at the moment."

    sundial_running: PaCo.Field[Self, TimedialRunning] = PaCo.Field(TimedialRunning)
    "Whether the *Sundial* is currently running."

    defeated_dukefishron: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Duke Fishron* was defeated at least once in the world."

    defeated_martianmadness: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Martian Madness* was repelled at least once in the world."

    defeated_lunaticcultist: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Lunatic Cultist* was defeated at least once in the world."

    defeated_moonlord: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Moon Lord* was defeated at least once in the world."

    defeated_pumpking: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Pumpking* was defeated at least once in the world."

    defeated_mourningwood: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Mourning Wood* was defeated at least once in the world."

    defeated_icequeen: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Ice Queen* was defeated at least once in the world."

    defeated_santank1: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Santa-NK1* was defeated at least once in the world."

    defeated_everscream: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Everscream* was defeated at least once in the world."

    defeated_pillar_solar: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Solar Pillar* was defeated at least once in the world."

    defeated_pillar_vortex: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Vortex Pillar* was defeated at least once in the world."

    defeated_pillar_nebula: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Nebula Pillar* was defeated at least once in the world."

    defeated_pillar_stardust: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Stardust Pillar* was defeated at least once in the world."

    pillar_solar_present: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether the *Solar Pillar* is currently present in the world."

    pillar_vortex_present: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether the *Vortex Pillar* is currently present in the world."

    pillar_nebula_present: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether the *Nebula Pillar* is currently present in the world."

    pillar_stardust_present: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether the *Stardust Pillar* is currently present in the world."

    impendingdoom_approaching: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether *Moon Lord* is about to spawn."

    party_center_active: PaCo.Field[Self, PartyCenterActive] = PaCo.Field(PartyCenterActive)
    "Whether the *Party Center* is active."

    party_spontaneous_active: PaCo.Field[Self, PartySpontaneousActive] = PaCo.Field(PartySpontaneousActive)
    "Whether a naturally-occurring party is ongoing."

    party_spontaneous_cooldown: PaCo.Field[Self, PartySpontaneousCooldown] = PaCo.Field(PartySpontaneousCooldown)
    "How much time has to pass before another naturally-occurring party can occur."

    party_partecipants: PaCo.Field[Self, PartyPartecipants] = PaCo.Field(PartyPartecipants)
    "Which NPCs are partecipating in the party."

    sandstorm_ongoing: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether a sandstorm is currently ongoing."

    sandstorm_duration: PaCo.Field[Self, SandstormDuration] = PaCo.Field(SandstormDuration)
    "How long the currently ongoing sandstorm will last for."

    sandstorm_severity_current: PaCo.Field[Self, SandstormSeverity] = PaCo.Field(SandstormSeverity)
    "Unknown."

    sandstorm_severity_target: PaCo.Field[Self, SandstormSeverity] = PaCo.Field(SandstormSeverity)
    "Unknown."

    rescued_bartender: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Bartender* NPC was rescued and can now arrive automatically."

    defeated_oldonesarmy_a: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the first tier of the *Old One's Army* was repelled at least once in the world."

    defeated_oldonesarmy_b: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the second tier of the *Old One's Army* was repelled at least once in the world."

    defeated_oldonesarmy_c: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the third tier of the *Old One's Army* was repelled at least once in the world."

    mushroom_background: PaCo.Field[Self, MushroomBackground] = PaCo.Field(MushroomBackground)
    "The background of the glowing mushroom biome."

    underworld_background: PaCo.Field[Self, UnderworldBackground] = PaCo.Field(UnderworldBackground)
    "The background of the underworld biome."

    forest_background_b: PaCo.Field[Self, ForestBackground] = PaCo.Field(ForestBackground)
    "The background of the forest biome in the forest area B."

    forest_background_c: PaCo.Field[Self, ForestBackground] = PaCo.Field(ForestBackground)
    "The background of the forest biome in the forest area C."

    forest_background_d: PaCo.Field[Self, ForestBackground] = PaCo.Field(ForestBackground)
    "The background of the forest biome in the forest area D."

    used_advancedcombattechniques_1: PaCo.Field[Self, Milestone] = PaCo.Field(Milestone)
    "Whether *Advanced Combat Techniques* was used in the world."

    lanternnight_spontaneous_cooldown: PaCo.Field[Self, LanternNightSpontaneousCooldown] = PaCo.Field(
        LanternNightSpontaneousCooldown
    )
    "How much time must pass before a new *Lantern Night* can spontaneously start again (if Moon Lord is defeated)."

    lanternnight_spontaneous_active: PaCo.Field[Self, LanternNightSpontaneousActive] = PaCo.Field(
        LanternNightSpontaneousActive
    )
    "Whether a (spontaneous) *Lantern Night* is ongoing or not."

    lanternnight_celebration_active: PaCo.Field[Self, LanternNightCelebrationActive] = PaCo.Field(
        LanternNightCelebrationActive
    )
    "Whether a celebratory (boss defeated) *Lantern Night* is ongoing."

    lanternnight_celebration_scheduled: PaCo.Field[Self, LanternNightCelebrationScheduled] = PaCo.Field(
        LanternNightCelebrationScheduled
    )
    "Whether a celebratory (boss defeated) *Lantern Night* will start at the next night."

    treetops: PaCo.Field[Self, Treetops] = PaCo.Field(Treetops)
    "The treetops in the world's various biomes."

    halloween_ongoing: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether it's *Halloween* for the next day."

    christmas_ongoing: PaCo.Field[Self, EventOngoing] = PaCo.Field(EventOngoing)
    "Whether it's *Christmas* for the next day."

    ore_copper_tier: PaCo.Field[Self, OreAvailable] = PaCo.Field(OreAvailable)
    "The first tier of pre-hardmode ore selected to spawn in the world: either Copper or Tin."

    ore_iron_tier: PaCo.Field[Self, OreAvailable] = PaCo.Field(OreAvailable)
    "The first tier of pre-hardmode ore selected to spawn in the world: either Iron or Lead."

    ore_silver_tier: PaCo.Field[Self, OreAvailable] = PaCo.Field(OreAvailable)
    "The first tier of pre-hardmode ore selected to spawn in the world: either Silver or Tungsten."

    ore_gold_tier: PaCo.Field[Self, OreAvailable] = PaCo.Field(OreAvailable)
    "The first tier of pre-hardmode ore selected to spawn in the world: either Gold or Platinum."

    bought_cat: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Cat* NPC was bought and can now arrive automatically."

    bought_dog: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Dog* NPC was bought and can now arrive automatically."

    bought_bunny: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Bunny* NPC was bought and can now arrive automatically."

    defeated_empressoflight: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether the *Empress of Light* was defeated at least once in the world."

    defeated_queenslime: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Queen Slime* was defeated at least once in the world."

    defeated_deerclops: PaCo.Field[Self, EnemyDefeated] = PaCo.Field(EnemyDefeated)
    "Whether *Deerclops* was defeated at least once in the world."

    unlocked_slime_nerdy: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Nerdy Slime* NPC was unlocked and can now arrive automatically."

    unlocked_merchant: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Merchant* NPC was unlocked and can now arrive automatically."

    unlocked_demolitionist: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Demolitionist* NPC was unlocked and can now arrive automatically."

    unlocked_partygirl: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Party Girl* NPC was unlocked and can now arrive automatically."

    unlocked_dyetrader: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Dye Trader* NPC was unlocked and can now arrive automatically."

    unlocked_truffle: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Truffle* NPC was unlocked and can now arrive automatically."

    unlocked_armsdealer: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Arms Dealer* NPC was unlocked and can now arrive automatically."

    unlocked_nurse: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Nurse* NPC was unlocked and can now arrive automatically."

    unlocked_princess: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Princess* NPC was unlocked and can now arrive automatically."

    used_advancedcombattechniques_2: PaCo.Field[Self, Milestone] = PaCo.Field(Milestone)
    "Whether *Advanced Combat Techniques: Volume Two* was used in the world."

    used_peddlerssatchel: PaCo.Field[Self, Milestone] = PaCo.Field(Milestone)
    "Whether the *Peddler's Satchel* was used in the world."

    unlocked_slime_cool: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Cool Slime* NPC was unlocked and can now arrive automatically."

    unlocked_slime_elder: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Elder Slime* NPC was unlocked and can now arrive automatically."

    unlocked_slime_clumsy: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Clumsy Slime* NPC was unlocked and can now arrive automatically."

    unlocked_slime_diva: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Diva Slime* NPC was unlocked and can now arrive automatically."

    unlocked_slime_surly: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Surly Slime* NPC was unlocked and can now arrive automatically."

    unlocked_slime_mystic: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Mystic Slime* NPC was unlocked and can now arrive automatically."

    unlocked_slime_squire: PaCo.Field[Self, NPCRescued] = PaCo.Field(NPCRescued)
    "Whether the *Squire Slime* NPC was unlocked and can now arrive automatically."

    moondial_running: PaCo.Field[Self, TimedialRunning] = PaCo.Field(TimedialRunning)
    "Whether the *Moondial* is currently running."

    moondial_cooldown: PaCo.Field[Self, TimedialCooldown] = PaCo.Field(TimedialCooldown)
    "How much the *Moondial* is on cooldown for."

    secret_halloween: PaCo.Field[Self, SecretSeedActive] = PaCo.Field(SecretSeedActive)
    "If the world uses the secret seed *Hocus Pocus*."

    secret_christmas: PaCo.Field[Self, SecretSeedActive] = PaCo.Field(SecretSeedActive)
    "If the world uses the secret seed *Jingle All The Way*."

    secret_vampirism: PaCo.Field[Self, SecretSeedActive] = PaCo.Field(SecretSeedActive)
    "If the world uses the secret seed *Vampirism*."

    secret_purification: PaCo.Field[Self, SecretSeedActive] = PaCo.Field(SecretSeedActive)
    "If the world uses the secret seed *Purify This*."

    meteorshower_remaining: PaCo.Field[Self, MeteorShowerRemaining] = PaCo.Field(MeteorShowerRemaining)
    "How many meteors are left in the *Meteor Shower*."

    coinrain_remaining: PaCo.Field[Self, CoinRainRemaining] = PaCo.Field(CoinRainRemaining)
    "Total value of the coins that are left in the *Coin Rain*."

    secret_teams: PaCo.Field[Self, SecretSeedActive] = PaCo.Field(SecretSeedActive)
    "If the world uses the secret seed *Royale With Cheese*."

    secret_teams_spawns: PaCo.Field[Self, SecretTeamsSpawns] = PaCo.Field(SecretTeamsSpawns)
    "The spawn points for the secret seed *Royale With Cheese*."

    secret_dualdungeons: PaCo.Field[Self, SecretSeedActive] = PaCo.Field(SecretSeedActive)
    "If the world uses the secret seed *Dual Dungeons*."

    secret_morelightning: PaCo.Field[Self, SecretSeedActive] = PaCo.Field(SecretSeedActive)
    "If the world uses the secret seed *Electric Boogaloo*."

    secret_nolightning: PaCo.Field[Self, SecretSeedActive] = PaCo.Field(SecretSeedActive)
    "If the world uses the secret seed *Calm Before The Storm*."

    manifest: PaCo.Field[Self, WorldManifest] = PaCo.Field(WorldManifest)
    "Unknown."

    # noinspection PyTypeChecker
    @override
    def __init__(self, *args: Pack, **kwargs):
        self.name: WorldName = ...
        self.generator_seed: WorldGeneratorSeed = ...
        self.generator_version: WorldGeneratorVersion = ...
        self.uuid: PackUUID = ...
        self.id: WorldID = ...
        self.bounds: WorldBounds = ...
        self.size: WorldSize = ...
        self.difficulty: PackWorldDifficulty = ...
        self.special_drunk: SpecialSeedActive = ...
        self.special_fortheworthy: SpecialSeedActive = ...
        self.special_anniversary: SpecialSeedActive = ...
        self.special_dontstarve: SpecialSeedActive = ...
        self.special_notthebees: SpecialSeedActive = ...
        self.special_remix: SpecialSeedActive = ...
        self.special_notraps: SpecialSeedActive = ...
        self.special_zenith: SpecialSeedActive = ...
        self.special_skyblock: SpecialSeedActive = ...
        self.created_on: PackDatetime = ...
        self.last_saved_on: PackDatetime = ...
        self.moon_style: MoonStyle = ...
        self.forest_boundary_a_b: WorldStyleBoundary = ...
        self.forest_boundary_b_c: WorldStyleBoundary = ...
        self.forest_boundary_c_d: WorldStyleBoundary = ...
        self.forest_treetop_a: ForestTreetop = ...
        self.forest_treetop_b: ForestTreetop = ...
        self.forest_treetop_c: ForestTreetop = ...
        self.forest_treetop_d: ForestTreetop = ...
        self.cavern_boundary_a_b: WorldStyleBoundary = ...
        self.cavern_boundary_b_c: WorldStyleBoundary = ...
        self.cavern_boundary_c_d: WorldStyleBoundary = ...
        self.cavern_background_a: CavernBackground = ...
        self.cavern_background_b: CavernBackground = ...
        self.cavern_background_c: CavernBackground = ...
        self.cavern_background_d: CavernBackground = ...
        self.ice_background: IceBackground = ...
        self.jungle_underground_background: JungleUndergroundBackground = ...
        self.hell_background: HellBackground = ...
        self.point_spawn: PackCoordinatesInt = ...
        self.underground_surface_boundary: WorldLayerBoundary = ...
        self.cavern_underground_boundary: WorldLayerBoundary = ...
        self.clock_time: Clock = ...
        self.day_time: Daytime = ...
        self.moon_phase: MoonPhase = ...
        self.bloodmoon_ongoing: EventOngoing = ...
        self.eclipse_ongoing: EventOngoing = ...
        self.point_dungeon: PackCoordinatesInt = ...
        self.evil: WorldEvil = ...
        self.defeated_eyeofcthulhu: EnemyDefeated = ...
        self.defeated_eaterofworlds: EnemyDefeated = ...
        self.defeated_skeletron: EnemyDefeated = ...
        self.defeated_queenbee: EnemyDefeated = ...
        self.defeated_thetwins: EnemyDefeated = ...
        self.defeated_thedestroyer: EnemyDefeated = ...
        self.defeated_skeletronprime: EnemyDefeated = ...
        self.defeated_anymechanicalboss: EnemyDefeated = ...
        self.defeated_plantera: EnemyDefeated = ...
        self.defeated_golem: EnemyDefeated = ...
        self.defeated_kingslime: EnemyDefeated = ...
        self.rescued_goblin: NPCRescued = ...
        self.rescued_wizard: NPCRescued = ...
        self.rescued_mechanic: NPCRescued = ...
        self.defeated_goblinarmy: EnemyDefeated = ...
        self.defeated_clown: EnemyDefeated = ...
        self.defeated_frostlegion: EnemyDefeated = ...
        self.defeated_pirateinvasion: EnemyDefeated = ...
        self.shadoworb_smashed: EnemyDefeated = ...
        self.meteorite_scheduled: MeteoriteScheduled = ...
        self.shadoworb_count: ShadowOrbCount = ...
        self.altar_count: AltarCount = ...
        self.mode: WorldMode = ...
        self.party_doomed: EventOngoing = ...
        self.invasion_delay: InvasionDelay = ...
        self.invasion_power_left: InvasionPower = ...
        self.invasion_kind: InvasionKind = ...
        self.invasion_position: InvasionPosition = ...
        self.slimerain_duration: SlimeRainDuration = ...
        self.sundial_cooldown: TimedialCooldown = ...
        self.rain_ongoing: EventOngoing = ...
        self.rain_duration: RainDuration = ...
        self.rain_strength: RainStrength = ...
        self.ore_cobalt_tier: OreAvailable = ...
        self.ore_mythril_tier: OreAvailable = ...
        self.ore_adamantite_tier: OreAvailable = ...
        self.forest_background_a: ForestBackground = ...
        self.corruption_background: CorruptionBackground = ...
        self.jungle_surface_background: JungleSurfaceBackground = ...
        self.snow_background: SnowBackground = ...
        self.hallow_background: HallowBackground = ...
        self.crimson_background: CrimsonBackground = ...
        self.desert_background: DesertBackground = ...
        self.ocean_background: OceanBackground = ...
        self.cloud_background_active: CloudBackgroundActive = ...
        self.cloud_count: CloudCount = ...
        self.wind_speed: WindSpeed = ...
        self.fishingquest_completed_by: FishingQuestCompletedBy = ...
        self.rescued_angler: NPCRescued = ...
        self.fishingquest_goal: FishingQuestGoal = ...
        self.rescued_stylist: NPCRescued = ...
        self.rescued_taxcollector: NPCRescued = ...
        self.rescued_golfer: NPCRescued = ...
        self.invasion_power_total: InvasionPower = ...
        self.cultists_cooldown: CultistsCooldown = ...
        self.banner_kill_counts: BannerKillCounts = ...
        self.banner_claimable_counts: BannerClaimableCounts = ...
        self.sundial_running: TimedialRunning = ...
        self.defeated_dukefishron: EnemyDefeated = ...
        self.defeated_martianmadness: EnemyDefeated = ...
        self.defeated_lunaticcultist: EnemyDefeated = ...
        self.defeated_moonlord: EnemyDefeated = ...
        self.defeated_pumpking: EnemyDefeated = ...
        self.defeated_mourningwood: EnemyDefeated = ...
        self.defeated_icequeen: EnemyDefeated = ...
        self.defeated_santank1: EnemyDefeated = ...
        self.defeated_everscream: EnemyDefeated = ...
        self.defeated_pillar_solar: EnemyDefeated = ...
        self.defeated_pillar_vortex: EnemyDefeated = ...
        self.defeated_pillar_nebula: EnemyDefeated = ...
        self.defeated_pillar_stardust: EnemyDefeated = ...
        self.pillar_solar_present: EventOngoing = ...
        self.pillar_vortex_present: EventOngoing = ...
        self.pillar_nebula_present: EventOngoing = ...
        self.pillar_stardust_present: EventOngoing = ...
        self.impendingdoom_approaching: EventOngoing = ...
        self.party_center_active: PartyCenterActive = ...
        self.party_spontaneous_active: PartySpontaneousActive = ...
        self.party_spontaneous_cooldown: PartySpontaneousCooldown = ...
        self.party_partecipants: PartyPartecipants = ...
        self.sandstorm_ongoing: EventOngoing = ...
        self.sandstorm_duration: SandstormDuration = ...
        self.sandstorm_severity_current: SandstormSeverity = ...
        self.sandstorm_severity_target: SandstormSeverity = ...
        self.rescued_bartender: Milestone = ...
        self.defeated_oldonesarmy_a: EnemyDefeated = ...
        self.defeated_oldonesarmy_b: EnemyDefeated = ...
        self.defeated_oldonesarmy_c: EnemyDefeated = ...
        self.mushroom_background: MushroomBackground = ...
        self.underworld_background: UnderworldBackground = ...
        self.forest_background_b: ForestBackground = ...
        self.forest_background_c: ForestBackground = ...
        self.forest_background_d: ForestBackground = ...
        self.used_advancedcombattechniques_1: Milestone = ...
        self.lanternnight_spontaneous_cooldown: LanternNightSpontaneousCooldown = ...
        self.lanternnight_spontaneous_active: LanternNightSpontaneousActive = ...
        self.lanternnight_celebration_active: LanternNightCelebrationActive = ...
        self.lanternnight_celebration_scheduled: LanternNightCelebrationScheduled = ...
        self.treetops: Treetops = ...
        self.halloween_ongoing: EventOngoing = ...
        self.christmas_ongoing: EventOngoing = ...
        self.ore_copper_tier: OreAvailable = ...
        self.ore_iron_tier: OreAvailable = ...
        self.ore_silver_tier: OreAvailable = ...
        self.ore_gold_tier: OreAvailable = ...
        self.bought_cat: NPCRescued = ...
        self.bought_dog: NPCRescued = ...
        self.bought_bunny: NPCRescued = ...
        self.defeated_empressoflight: EnemyDefeated = ...
        self.defeated_queenslime: EnemyDefeated = ...
        self.defeated_deerclops: EnemyDefeated = ...
        self.unlocked_slime_nerdy: NPCRescued = ...
        self.unlocked_merchant: NPCRescued = ...
        self.unlocked_demolitionist: NPCRescued = ...
        self.unlocked_partygirl: NPCRescued = ...
        self.unlocked_dyetrader: NPCRescued = ...
        self.unlocked_truffle: NPCRescued = ...
        self.unlocked_armsdealer: NPCRescued = ...
        self.unlocked_nurse: NPCRescued = ...
        self.unlocked_princess: NPCRescued = ...
        self.used_advancedcombattechniques_2: Milestone = ...
        self.used_peddlerssatchel: Milestone = ...
        self.unlocked_slime_cool: NPCRescued = ...
        self.unlocked_slime_elder: NPCRescued = ...
        self.unlocked_slime_clumsy: NPCRescued = ...
        self.unlocked_slime_diva: NPCRescued = ...
        self.unlocked_slime_surly: NPCRescued = ...
        self.unlocked_slime_mystic: NPCRescued = ...
        self.unlocked_slime_squire: NPCRescued = ...
        self.moondial_running: TimedialRunning = ...
        self.moondial_cooldown: TimedialCooldown = ...
        self.secret_halloween: SecretSeedActive = ...
        self.secret_christmas: SecretSeedActive = ...
        self.secret_vampirism: SecretSeedActive = ...
        self.secret_purification: SecretSeedActive = ...
        self.meteorshower_remaining: MeteorShowerRemaining = ...
        self.coinrain_remaining: CoinRainRemaining = ...
        self.secret_teams: SecretSeedActive = ...
        self.secret_teams_spawns: SecretTeamsSpawns = ...
        self.secret_dualdungeons: SecretSeedActive = ...
        self.secret_morelightning: SecretSeedActive = ...
        self.secret_nolightning: SecretSeedActive = ...
        self.manifest: WorldManifest = ...

        super().__init__(*args, **kwargs)

    @classmethod
    @override
    def _fields(cls, version: FileVersion = FileVersion.V_1_4_5_5, **kwargs) -> list[PaCo.Field[Self, Pack]]:
        fields = []

        fields.append(cls.name)
        fields.append(cls.generator_seed)
        fields.append(cls.generator_version)
        fields.append(cls.uuid)
        fields.append(cls.id)
        fields.append(cls.bounds)
        fields.append(cls.size)
        fields.append(cls.difficulty)
        fields.append(cls.special_drunk)
        fields.append(cls.special_fortheworthy)
        fields.append(cls.special_anniversary)
        fields.append(cls.special_dontstarve)
        fields.append(cls.special_notthebees)
        fields.append(cls.special_remix)
        fields.append(cls.special_notraps)
        fields.append(cls.special_zenith)
        fields.append(cls.special_skyblock)
        fields.append(cls.created_on)
        fields.append(cls.last_saved_on)
        fields.append(cls.moon_style)
        fields.append(cls.forest_boundary_a_b)
        fields.append(cls.forest_boundary_b_c)
        fields.append(cls.forest_boundary_c_d)
        fields.append(cls.forest_treetop_a)
        fields.append(cls.forest_treetop_b)
        fields.append(cls.forest_treetop_c)
        fields.append(cls.forest_treetop_d)
        fields.append(cls.cavern_boundary_a_b)
        fields.append(cls.cavern_boundary_b_c)
        fields.append(cls.cavern_boundary_c_d)
        fields.append(cls.cavern_background_a)
        fields.append(cls.cavern_background_b)
        fields.append(cls.cavern_background_c)
        fields.append(cls.cavern_background_d)
        fields.append(cls.ice_background)
        fields.append(cls.jungle_underground_background)
        fields.append(cls.hell_background)
        fields.append(cls.point_spawn)
        fields.append(cls.underground_surface_boundary)
        fields.append(cls.cavern_underground_boundary)
        fields.append(cls.clock_time)
        fields.append(cls.day_time)
        fields.append(cls.moon_phase)
        fields.append(cls.bloodmoon_ongoing)
        fields.append(cls.eclipse_ongoing)
        fields.append(cls.point_dungeon)
        fields.append(cls.evil)
        fields.append(cls.defeated_eyeofcthulhu)
        fields.append(cls.defeated_eaterofworlds)
        fields.append(cls.defeated_skeletron)
        fields.append(cls.defeated_queenbee)
        fields.append(cls.defeated_thetwins)
        fields.append(cls.defeated_thedestroyer)
        fields.append(cls.defeated_skeletronprime)
        fields.append(cls.defeated_anymechanicalboss)
        fields.append(cls.defeated_plantera)
        fields.append(cls.defeated_golem)
        fields.append(cls.defeated_kingslime)
        fields.append(cls.rescued_goblin)
        fields.append(cls.rescued_wizard)
        fields.append(cls.rescued_mechanic)
        fields.append(cls.defeated_goblinarmy)
        fields.append(cls.defeated_clown)
        fields.append(cls.defeated_frostlegion)
        fields.append(cls.defeated_pirateinvasion)
        fields.append(cls.shadoworb_smashed)
        fields.append(cls.meteorite_scheduled)
        fields.append(cls.shadoworb_count)
        fields.append(cls.altar_count)
        fields.append(cls.mode)
        fields.append(cls.party_doomed)
        fields.append(cls.invasion_delay)
        fields.append(cls.invasion_power_left)
        fields.append(cls.invasion_kind)
        fields.append(cls.invasion_position)
        fields.append(cls.slimerain_duration)
        fields.append(cls.sundial_cooldown)
        fields.append(cls.rain_ongoing)
        fields.append(cls.rain_duration)
        fields.append(cls.rain_strength)
        fields.append(cls.ore_cobalt_tier)
        fields.append(cls.ore_mythril_tier)
        fields.append(cls.ore_adamantite_tier)
        fields.append(cls.forest_background_a)
        fields.append(cls.corruption_background)
        fields.append(cls.jungle_surface_background)
        fields.append(cls.snow_background)
        fields.append(cls.hallow_background)
        fields.append(cls.crimson_background)
        fields.append(cls.desert_background)
        fields.append(cls.ocean_background)
        fields.append(cls.cloud_background_active)
        fields.append(cls.cloud_count)
        fields.append(cls.wind_speed)
        fields.append(cls.fishingquest_completed_by)
        fields.append(cls.rescued_angler)
        fields.append(cls.fishingquest_goal)
        fields.append(cls.rescued_stylist)
        fields.append(cls.rescued_taxcollector)
        fields.append(cls.rescued_golfer)
        fields.append(cls.invasion_power_total)
        fields.append(cls.cultists_cooldown)
        fields.append(cls.banner_kill_counts)
        fields.append(cls.banner_claimable_counts)
        fields.append(cls.sundial_running)
        fields.append(cls.defeated_dukefishron)
        fields.append(cls.defeated_martianmadness)
        fields.append(cls.defeated_lunaticcultist)
        fields.append(cls.defeated_moonlord)
        fields.append(cls.defeated_pumpking)
        fields.append(cls.defeated_mourningwood)
        fields.append(cls.defeated_icequeen)
        fields.append(cls.defeated_santank1)
        fields.append(cls.defeated_everscream)
        fields.append(cls.defeated_pillar_solar)
        fields.append(cls.defeated_pillar_vortex)
        fields.append(cls.defeated_pillar_nebula)
        fields.append(cls.defeated_pillar_stardust)
        fields.append(cls.pillar_solar_present)
        fields.append(cls.pillar_vortex_present)
        fields.append(cls.pillar_nebula_present)
        fields.append(cls.pillar_stardust_present)
        fields.append(cls.impendingdoom_approaching)
        fields.append(cls.party_center_active)
        fields.append(cls.party_spontaneous_active)
        fields.append(cls.party_spontaneous_cooldown)
        fields.append(cls.party_partecipants)
        fields.append(cls.sandstorm_ongoing)
        fields.append(cls.sandstorm_duration)
        fields.append(cls.sandstorm_severity_current)
        fields.append(cls.sandstorm_severity_target)
        fields.append(cls.rescued_bartender)
        fields.append(cls.defeated_oldonesarmy_a)
        fields.append(cls.defeated_oldonesarmy_b)
        fields.append(cls.defeated_oldonesarmy_c)
        fields.append(cls.mushroom_background)
        fields.append(cls.underworld_background)
        fields.append(cls.forest_background_b)
        fields.append(cls.forest_background_c)
        fields.append(cls.forest_background_d)
        fields.append(cls.used_advancedcombattechniques_1)
        fields.append(cls.lanternnight_spontaneous_cooldown)
        fields.append(cls.lanternnight_spontaneous_active)
        fields.append(cls.lanternnight_celebration_active)
        fields.append(cls.lanternnight_celebration_scheduled)
        fields.append(cls.treetops)
        fields.append(cls.halloween_ongoing)
        fields.append(cls.christmas_ongoing)
        fields.append(cls.ore_copper_tier)
        fields.append(cls.ore_iron_tier)
        fields.append(cls.ore_silver_tier)
        fields.append(cls.ore_gold_tier)
        fields.append(cls.bought_cat)
        fields.append(cls.bought_dog)
        fields.append(cls.bought_bunny)
        fields.append(cls.defeated_empressoflight)
        fields.append(cls.defeated_queenslime)
        fields.append(cls.defeated_deerclops)
        fields.append(cls.unlocked_slime_nerdy)
        fields.append(cls.unlocked_merchant)
        fields.append(cls.unlocked_demolitionist)
        fields.append(cls.unlocked_partygirl)
        fields.append(cls.unlocked_dyetrader)
        fields.append(cls.unlocked_truffle)
        fields.append(cls.unlocked_armsdealer)
        fields.append(cls.unlocked_nurse)
        fields.append(cls.unlocked_princess)
        fields.append(cls.used_advancedcombattechniques_2)
        fields.append(cls.used_peddlerssatchel)
        fields.append(cls.unlocked_slime_cool)
        fields.append(cls.unlocked_slime_elder)
        fields.append(cls.unlocked_slime_clumsy)
        fields.append(cls.unlocked_slime_diva)
        fields.append(cls.unlocked_slime_surly)
        fields.append(cls.unlocked_slime_mystic)
        fields.append(cls.unlocked_slime_squire)
        fields.append(cls.moondial_running)
        fields.append(cls.moondial_cooldown)
        fields.append(cls.secret_halloween)
        fields.append(cls.secret_christmas)
        fields.append(cls.secret_vampirism)
        fields.append(cls.secret_purification)
        fields.append(cls.meteorshower_remaining)
        fields.append(cls.coinrain_remaining)
        fields.append(cls.secret_teams)
        fields.append(cls.secret_teams_spawns)
        fields.append(cls.secret_dualdungeons)

        if version >= FileVersion.V_1_4_5_7:
            fields.append(cls.secret_morelightning)
            fields.append(cls.secret_nolightning)

        fields.append(cls.manifest)

        return fields

    def bosses(self) -> list[EnemyDefeated]:
        """
        :return: The :class:`list` of :class:`EnemyDefeated` flags for all bosses in the game.
        """
        return [
            self.defeated_eyeofcthulhu,
            self.defeated_eaterofworlds,
            self.defeated_skeletron,
            self.defeated_queenbee,
            self.defeated_thetwins,
            self.defeated_thedestroyer,
            self.defeated_skeletronprime,
            self.defeated_anymechanicalboss,
            self.defeated_plantera,
            self.defeated_golem,
            self.defeated_kingslime,
            self.defeated_goblinarmy,
            self.defeated_clown,
            self.defeated_frostlegion,
            self.defeated_pirateinvasion,
            self.defeated_dukefishron,
            self.defeated_martianmadness,
            self.defeated_lunaticcultist,
            self.defeated_moonlord,
            self.defeated_pumpking,
            self.defeated_mourningwood,
            self.defeated_icequeen,
            self.defeated_santank1,
            self.defeated_everscream,
            self.defeated_pillar_solar,
            self.defeated_pillar_vortex,
            self.defeated_pillar_nebula,
            self.defeated_pillar_stardust,
            self.defeated_oldonesarmy_a,
            self.defeated_oldonesarmy_b,
            self.defeated_oldonesarmy_c,
        ]


__all__ = ("WorldHeader",)
