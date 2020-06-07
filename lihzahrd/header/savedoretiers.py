from typing import *
from ..enums import BlockType


class SavedOreTiers:
    """The types of ores that generated in the world."""

    def __init__(self,
                 tier_1: BlockType,
                 tier_2: BlockType,
                 tier_3: BlockType,
                 tier_4: BlockType,
                 hardmode_tier_1: Optional[BlockType],
                 hardmode_tier_2: Optional[BlockType],
                 hardmode_tier_3: Optional[BlockType]):

        self.tier_1: BlockType = tier_1
        """Copper or Tin?"""
        assert self.tier_1 == BlockType.COPPER or self.tier_1 == BlockType.TIN

        self.tier_2: BlockType = tier_2
        """Iron or Lead?"""
        assert self.tier_2 == BlockType.IRON or self.tier_2 == BlockType.LEAD

        self.tier_3: BlockType = tier_3
        """Silver or Tungsten?"""
        assert self.tier_3 == BlockType.SILVER or self.tier_3 == BlockType.TUNGSTEN

        self.tier_4: BlockType = tier_4
        """Gold or Platinum?"""
        assert self.tier_4 == BlockType.GOLD or self.tier_4 == BlockType.PLATINUM

        self.hardmode_tier_1: Optional[BlockType] = hardmode_tier_1
        """Cobalt or Palladium? None if it hasn't been determined yet."""
        assert self.hardmode_tier_1 is None \
               or self.hardmode_tier_1 == BlockType.COBALT \
               or self.hardmode_tier_1 == BlockType.PALLADIUM

        self.hardmode_tier_2: Optional[BlockType] = hardmode_tier_2
        """Mythril or Orichalcum? None if it hasn't been determined yet."""
        assert self.hardmode_tier_2 is None \
               or self.hardmode_tier_2 == BlockType.MYTHRIL \
               or self.hardmode_tier_2 == BlockType.ORICHALCUM

        self.hardmode_tier_3: Optional[BlockType] = hardmode_tier_3
        """Adamantite or Titanium? None if it hasn't been determined yet."""
        assert self.hardmode_tier_3 is None \
               or self.hardmode_tier_3 == BlockType.ADAMANTITE \
               or self.hardmode_tier_3 == BlockType.TITANIUM

    def __repr__(self):
        return f"<SavedOreTiers>"
