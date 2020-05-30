class SavedNPCs:
    def __init__(self,
                 goblin_tinkerer: bool,
                 wizard: bool,
                 mechanic: bool,
                 angler: bool,
                 stylist: bool,
                 tax_collector: bool,
                 bartender: bool,
                 golfer: bool,
                 advanced_combat: bool):
        self.goblin_tinkerer: bool = goblin_tinkerer
        self.wizard: bool = wizard
        self.mechanic: bool = mechanic
        self.angler: bool = angler
        self.stylist: bool = stylist
        self.tax_collector: bool = tax_collector
        self.bartender: bool = bartender
        self.golfer: bool = golfer
        self.advanced_combat: bool = advanced_combat
        """Was the Advanced Combat Technique Book used."""

    def __repr__(self):
        return f"SavedNPCs(goblin_tinkerer={self.goblin_tinkerer}, wizard={self.wizard}, mechanic={self.mechanic}," \
               f" angler={self.angler}, stylist={self.stylist}, tax_collector={self.tax_collector}," \
               f" bartender={self.bartender}, golfer={self.golfer}, advanced_combat={self.advanced_combat}"
