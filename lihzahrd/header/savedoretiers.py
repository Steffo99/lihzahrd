import typing

class SavedOreTiers:
    """Information about the treetop variants in the worls"""
    def __init__(self,
        saved_ore_tier_copper: int,
        saved_ore_tier_iron: int,
        saved_ore_tier_silver: int,
        saved_ore_tier_gold: int,
        ):
        self.copper: int = saved_ore_tier_copper
        self.iron: int = saved_ore_tier_iron
        self.silver: int = saved_ore_tier_silver
        self.gold: int = saved_ore_tier_gold

    def __repr__(self):
        return f"WorldSavedOreTier(copper={self.copper}, iron={self.iron}, silver={self.silver}, gold={self.gold})"
