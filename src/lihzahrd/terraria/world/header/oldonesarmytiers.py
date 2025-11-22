class OldOnesArmyTiers:
    def __init__(self, tier1, tier2, tier3):
        self.tier1: bool = tier1
        self.tier2: bool = tier2
        self.tier3: bool = tier3

    def __repr__(self):
        return f"OldOneArmyTiers({self.tier1}, {self.tier2}, {self.tier3})"
