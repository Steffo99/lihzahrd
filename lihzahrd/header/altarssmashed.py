from .hardmodeore import HardmodeTier1Ore, HardmodeTier2Ore, HardmodeTier3Ore


class AltarsSmashed:
    """Information related to the first three hardmode ores."""
    def __init__(self,
                 count: int,
                 ore_tier1: HardmodeTier1Ore,
                 ore_tier2: HardmodeTier2Ore,
                 ore_tier3: HardmodeTier3Ore):
        self.count: int = count
        """The number of altars smashed."""

        self.ore_tier1: HardmodeTier1Ore = ore_tier1
        self.ore_tier2: HardmodeTier2Ore = ore_tier2
        self.ore_tier3: HardmodeTier3Ore = ore_tier3

    def __repr__(self):
        return f"WorldAltars(count={self.count}, ore_tier1={self.ore_tier1}, ore_tier2={self.ore_tier2}," \
               f" ore_tier3={self.ore_tier3})"
