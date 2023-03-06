class SavedNPCs:
    def __init__(
        self,
        goblin_tinkerer: bool,
        wizard: bool,
        mechanic: bool,
        angler: bool,
        stylist: bool,
        tax_collector: bool,
        bartender: bool,
        golfer: bool,
        advanced_combat: bool,
        slime_nerdy: bool,
        merchant: bool,
        demolitionist: bool,
        party_girl: bool,
        dye_trader: bool,
        truffle: bool,
        arms_dealer: bool,
        nurse: bool,
        princess: bool,
        advanced_combat_2: bool,
        peddlers_satchel: bool,
        slime_cool: bool,
        slime_elder: bool,
        slime_clumsy: bool,
        slime_diva: bool,
        slime_surly: bool,
        slime_mystic: bool,
        slime_squire: bool,
    ):
        self.goblin_tinkerer: bool = goblin_tinkerer
        self.wizard: bool = wizard
        self.mechanic: bool = mechanic
        self.angler: bool = angler
        self.stylist: bool = stylist
        self.tax_collector: bool = tax_collector
        self.bartender: bool = bartender
        self.golfer: bool = golfer
        self.advanced_combat: bool = advanced_combat
        self.slime_nerdy: bool = slime_nerdy
        self.merchant: bool = merchant
        self.demolitionist: bool = demolitionist
        self.party_girl: bool = party_girl
        self.dye_trader: bool = dye_trader
        self.truffle: bool = truffle
        self.arms_dealer: bool = arms_dealer
        self.nurse: bool = nurse
        self.princess: bool = princess
        self.advanced_combat_2: bool = advanced_combat_2
        self.peddlers_satchel: bool = peddlers_satchel
        self.slime_cool: bool = slime_cool
        self.slime_elder: bool = slime_elder
        self.slime_clumsy: bool = slime_clumsy
        self.slime_diva: bool = slime_diva
        self.slime_surly: bool = slime_surly
        self.slime_mystic: bool = slime_mystic
        self.slime_squire: bool = slime_squire

    def __repr__(self):
        return (
            f"SavedNPCs("
            f"goblin_tinkerer={self.goblin_tinkerer}, "
            f"wizard={self.wizard}, "
            f"mechanic={self.mechanic}, "
            f"angler={self.angler}, "
            f"stylist={self.stylist}, "
            f"tax_collector={self.tax_collector}, "
            f"bartender={self.bartender}, "
            f"golfer={self.golfer}, "
            f"advanced_combat={self.advanced_combat}, "
            f"slime_nerdy={self.slime_nerdy}, "
            f"merchant={self.merchant}, "
            f"demolitionist={self.demolitionist}, "
            f"party_girl={self.party_girl}, "
            f"dye_trader={self.dye_trader}, "
            f"truffle={self.truffle}, "
            f"arms_dealer={self.arms_dealer}, "
            f"nurse={self.nurse}, "
            f"princess={self.princess}, "
            f"advanced_combat_2={self.advanced_combat_2}, "
            f"peddlers_satchel={self.peddlers_satchel}, "
            f"slime_cool={self.slime_cool}, "
            f"slime_elder={self.slime_elder}, "
            f"slime_clumsy={self.slime_clumsy}, "
            f"slime_diva={self.slime_diva}, "
            f"slime_surly={self.slime_surly}, "
            f"slime_mystic={self.slime_mystic}, "
            f"slime_squire={self.slime_squire}"
            f")"
        )
