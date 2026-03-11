from enum import IntEnum
from logging import getLogger
from typing import override

from lihzahrd.terraria.data.classmembers.item_base import ItemBase
from lihzahrd.terraria.data.classmembers.items import (
    Batfish,
    BumblebeeTuna,
    Catfish,
    Cloudfish,
    Cursedfish,
    Dirtfish,
    DynamiteFish,
    EaterofPlankton,
    FallenStarfish,
    TheFishofCthulhu,
    Harpyfish,
    Hungerfish,
    Ichorfish,
    Jewelfish,
    MirageFish,
    MutantFlinxfin,
    Pengfish,
    Pixiefish,
    Spiderfish,
    TundraTrout,
    UnicornFish,
    GuideVoodooFish,
    Wyverntail,
    ZombieFish,
    AmanitiaFungifin,
    Angelfish,
    BloodyManowar,
    Bonefish,
    Bunnyfish,
    CapnTunabeard,
    Clownfish,
    DemonicHellfish,
    Derpfish,
    Fishron,
    InfectedScabbardfish,
    Mudfish,
    Slimefish,
    TropicalBarracuda,
    Fishotron,
)
from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class FishingQuestGoalEnum(IntEnum):
    """
    Possible fishing quest goals and their IDs.
    """

    BATFISH = 0
    "Batfish."

    BUMBLEBEE_TUNA = 1
    "Bumblebee Tuna."

    CATFISH = 2
    "Catfish."

    CLOUDFISH = 3
    "Cloudfish."

    CURSEDFISH = 4
    "Cursedfish."

    DIRTFISH = 5
    "Dirtfish."

    DYNAMITE_FISH = 6
    "Dynamite Fish."

    EATER_OF_PLANKTON = 7
    "Eater of Plankton."

    FALLEN_STARFISH = 8
    "Fallen Starfish."

    THE_FISH_OF_CTHULHU = 9
    "The Fish of Cthulhu."

    FISHOTRON = 10
    "Fishotron."

    HARPYFISH = 11
    "Harpyfish."

    HUNGERFISH = 12
    "Hungerfish."

    ICHORFISH = 13
    "Ichorfish."

    JEWELFISH = 14
    "Jewelfish."

    MIRAGE_FISH = 15
    "Mirage Fish."

    MUTANT_FLINXFIN = 16
    "Mutant Flinxfin."

    PENGFISH = 17
    "Pengfish."

    PIXIEFISH = 18
    "Pixiefish."

    SPIDERFISH = 19
    "Spiderfish."

    TUNDRA_TROUT = 20
    "Tundra Trout."

    UNICORN_FISH = 21
    "Unicorn Fish."

    GUIDE_VOODOO_FISH = 22
    "Guide Voodoo Fish."

    WYVERNTAIL = 23
    "Wyverntail."

    ZOMBIE_FISH = 24
    "Zombie Fish."

    AMANITIA_FUNGIFIN = 25
    "Amanitia Fungifin."

    ANGELFISH = 26
    "Angelfish."

    BLOODY_MANOWAR = 27
    "Bloody Manowar."

    BONEFISH = 28
    "Bonefish."

    BUNNYFISH = 29
    "Bunnyfish."

    CAPN_TUNABEAR = 30
    "Cap'n Tunabeard."

    CLOWNFISH = 31
    "Clownfish."

    DEMONIC_HELLFISH = 32
    "Demonic Hellfish."

    DERPFISH = 33
    "Derpfish."

    FISHRON = 34
    "Fishron."

    INFECTED_SCABBARDFISH = 35
    "Infected Scabbardfish."

    MUDFISH = 36
    "Mudfish."

    SLIMEFISH = 37
    "Slimefish."

    TROPICAL_BARRACUDA = 38
    "Tropical Barracuda."


class FishingQuestGoal(PackEnum[FishingQuestGoalEnum, int], PackInt):
    """
    The fish that should be caught to complete today's Angler Fishing Quest.
    """

    _LOG = getLogger(__name__)

    ENUM = FishingQuestGoalEnum

    @override
    def __repr__(self):
        item = self.get_item()
        if item is not None:
            return f"<{self.__class__.__qualname__}: {item.__qualname__}>"
        else:
            return super().__repr__()

    QUEST_TO_ITEM: dict[FishingQuestGoalEnum, type[ItemBase]] = {
        FishingQuestGoalEnum.BATFISH: Batfish,
        FishingQuestGoalEnum.BUMBLEBEE_TUNA: BumblebeeTuna,
        FishingQuestGoalEnum.CATFISH: Catfish,
        FishingQuestGoalEnum.CLOUDFISH: Cloudfish,
        FishingQuestGoalEnum.CURSEDFISH: Cursedfish,
        FishingQuestGoalEnum.DIRTFISH: Dirtfish,
        FishingQuestGoalEnum.DYNAMITE_FISH: DynamiteFish,
        FishingQuestGoalEnum.EATER_OF_PLANKTON: EaterofPlankton,
        FishingQuestGoalEnum.FALLEN_STARFISH: FallenStarfish,
        FishingQuestGoalEnum.THE_FISH_OF_CTHULHU: TheFishofCthulhu,
        FishingQuestGoalEnum.FISHOTRON: Fishotron,
        FishingQuestGoalEnum.HARPYFISH: Harpyfish,
        FishingQuestGoalEnum.HUNGERFISH: Hungerfish,
        FishingQuestGoalEnum.ICHORFISH: Ichorfish,
        FishingQuestGoalEnum.JEWELFISH: Jewelfish,
        FishingQuestGoalEnum.MIRAGE_FISH: MirageFish,
        FishingQuestGoalEnum.MUTANT_FLINXFIN: MutantFlinxfin,
        FishingQuestGoalEnum.PENGFISH: Pengfish,
        FishingQuestGoalEnum.PIXIEFISH: Pixiefish,
        FishingQuestGoalEnum.SPIDERFISH: Spiderfish,
        FishingQuestGoalEnum.TUNDRA_TROUT: TundraTrout,
        FishingQuestGoalEnum.UNICORN_FISH: UnicornFish,
        FishingQuestGoalEnum.GUIDE_VOODOO_FISH: GuideVoodooFish,
        FishingQuestGoalEnum.WYVERNTAIL: Wyverntail,
        FishingQuestGoalEnum.ZOMBIE_FISH: ZombieFish,
        FishingQuestGoalEnum.AMANITIA_FUNGIFIN: AmanitiaFungifin,
        FishingQuestGoalEnum.ANGELFISH: Angelfish,
        FishingQuestGoalEnum.BLOODY_MANOWAR: BloodyManowar,
        FishingQuestGoalEnum.BONEFISH: Bonefish,
        FishingQuestGoalEnum.BUNNYFISH: Bunnyfish,
        FishingQuestGoalEnum.CAPN_TUNABEAR: CapnTunabeard,
        FishingQuestGoalEnum.CLOWNFISH: Clownfish,
        FishingQuestGoalEnum.DEMONIC_HELLFISH: DemonicHellfish,
        FishingQuestGoalEnum.DERPFISH: Derpfish,
        FishingQuestGoalEnum.FISHRON: Fishron,
        FishingQuestGoalEnum.INFECTED_SCABBARDFISH: InfectedScabbardfish,
        FishingQuestGoalEnum.MUDFISH: Mudfish,
        FishingQuestGoalEnum.SLIMEFISH: Slimefish,
        FishingQuestGoalEnum.TROPICAL_BARRACUDA: TropicalBarracuda,
    }
    """
    Mapping from :class:`.FishingQuestGoalEnum` to :term:`ClassMember`.
    
    :meta hide-value:
    """

    ITEM_TO_QUEST: dict[type[ItemBase], FishingQuestGoalEnum] = {
        Batfish: FishingQuestGoalEnum.BATFISH,
        BumblebeeTuna: FishingQuestGoalEnum.BUMBLEBEE_TUNA,
        Catfish: FishingQuestGoalEnum.CATFISH,
        Cloudfish: FishingQuestGoalEnum.CLOUDFISH,
        Cursedfish: FishingQuestGoalEnum.CURSEDFISH,
        Dirtfish: FishingQuestGoalEnum.DIRTFISH,
        DynamiteFish: FishingQuestGoalEnum.DYNAMITE_FISH,
        EaterofPlankton: FishingQuestGoalEnum.EATER_OF_PLANKTON,
        FallenStarfish: FishingQuestGoalEnum.FALLEN_STARFISH,
        TheFishofCthulhu: FishingQuestGoalEnum.THE_FISH_OF_CTHULHU,
        Fishotron: FishingQuestGoalEnum.FISHOTRON,
        Harpyfish: FishingQuestGoalEnum.HARPYFISH,
        Hungerfish: FishingQuestGoalEnum.HUNGERFISH,
        Ichorfish: FishingQuestGoalEnum.ICHORFISH,
        Jewelfish: FishingQuestGoalEnum.JEWELFISH,
        MirageFish: FishingQuestGoalEnum.MIRAGE_FISH,
        MutantFlinxfin: FishingQuestGoalEnum.MUTANT_FLINXFIN,
        Pengfish: FishingQuestGoalEnum.PENGFISH,
        Pixiefish: FishingQuestGoalEnum.PIXIEFISH,
        Spiderfish: FishingQuestGoalEnum.SPIDERFISH,
        TundraTrout: FishingQuestGoalEnum.TUNDRA_TROUT,
        UnicornFish: FishingQuestGoalEnum.UNICORN_FISH,
        GuideVoodooFish: FishingQuestGoalEnum.GUIDE_VOODOO_FISH,
        Wyverntail: FishingQuestGoalEnum.WYVERNTAIL,
        ZombieFish: FishingQuestGoalEnum.ZOMBIE_FISH,
        AmanitiaFungifin: FishingQuestGoalEnum.AMANITIA_FUNGIFIN,
        Angelfish: FishingQuestGoalEnum.ANGELFISH,
        BloodyManowar: FishingQuestGoalEnum.BLOODY_MANOWAR,
        Bonefish: FishingQuestGoalEnum.BONEFISH,
        Bunnyfish: FishingQuestGoalEnum.BUNNYFISH,
        CapnTunabeard: FishingQuestGoalEnum.CAPN_TUNABEAR,
        Clownfish: FishingQuestGoalEnum.CLOWNFISH,
        DemonicHellfish: FishingQuestGoalEnum.DEMONIC_HELLFISH,
        Derpfish: FishingQuestGoalEnum.DERPFISH,
        Fishron: FishingQuestGoalEnum.FISHRON,
        InfectedScabbardfish: FishingQuestGoalEnum.INFECTED_SCABBARDFISH,
        Mudfish: FishingQuestGoalEnum.MUDFISH,
        Slimefish: FishingQuestGoalEnum.SLIMEFISH,
        TropicalBarracuda: FishingQuestGoalEnum.TROPICAL_BARRACUDA,
    }
    """
    Mapping from :term:`ClassMember` to :class:`.FishingQuestGoalEnum`.
    
    :meta hide-value:
    """

    def get_item(self) -> type[ItemBase]:
        """
        Convert :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` into an item :term:`ClassMember`.

        :return: The item :term:`ClassMember`.
        :raise ValueError: If no corresponding item :term:`ClassMember` exists.
        """

        quest_item = self.variant()

        try:
            return self.QUEST_TO_ITEM[quest_item]
        except KeyError:
            raise ValueError("Item ID is unknown: ", self.value)

    def set_from_item(self, item: type[ItemBase]) -> None:
        """
        Set the :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` to the given item :term:`ClassMember`.

        :param item: The item :term:`ClassMember`.
        :raise ValueError: If no corresponding :class:`.FishingQuestGoalEnum` exists.
        """
        try:
            quest_item = self.ITEM_TO_QUEST[item]
        except KeyError:
            raise ValueError("Item is not a Quest Fish: ", item)

        self.set_from_variant(quest_item)


__all__ = (
    "FishingQuestGoalEnum",
    "FishingQuestGoal",
)
