from .pillarsinfo import PillarsInfo
from .oldonesarmytiers import OldOnesArmyTiers


class BossesDefeated:
    def __init__(self,
                 eye_of_cthulhu: bool,
                 eater_of_worlds: bool,
                 skeletron: bool,
                 queen_bee: bool,
                 the_twins: bool,
                 the_destroyer: bool,
                 skeletron_prime: bool,
                 any_mechnical_boss: bool,
                 plantera: bool,
                 golem: bool,
                 king_slime: bool,
                 goblin_army: bool,
                 clown: bool,
                 frost_moon: bool,
                 pirates: bool,
                 duke_fishron: bool,
                 moon_lord: bool,
                 pumpking: bool,
                 mourning_wood: bool,
                 ice_queen: bool,
                 santa_nk1: bool,
                 everscream: bool,
                 martian_madness: bool,
                 lunatic_cultist: bool,
                 lunar_pillars: PillarsInfo,
                 old_ones_army: OldOnesArmyTiers,
                 empress_of_light: bool,
                 queen_slime: bool):
        self.eye_of_cthulhu: bool = eye_of_cthulhu
        self.eater_of_worlds: bool = eater_of_worlds
        self.skeletron: bool = skeletron
        self.queen_bee: bool = queen_bee
        self.the_twins: bool = the_twins
        self.the_destroyer: bool = the_destroyer
        self.skeletron_prime: bool = skeletron_prime

        self.any_mechnical_boss: bool = any_mechnical_boss
        """Appearently, there's a different flag for beating any mechanical boss and a specific mechanical boss."""

        self.plantera: bool = plantera
        self.golem: bool = golem
        self.king_slime: bool = king_slime
        self.goblin_army: bool = goblin_army
        self.clown: bool = clown
        self.frost_moon: bool = frost_moon
        self.pirates: bool = pirates
        self.duke_fishron: bool = duke_fishron
        self.moon_lord: bool = moon_lord
        self.pumpking: bool = pumpking
        self.mourning_wood: bool = mourning_wood
        self.ice_queen: bool = ice_queen
        self.santa_nk1: bool = santa_nk1
        self.everscream: bool = everscream
        self.martian_madness: bool = martian_madness
        self.lunatic_cultist: bool = lunatic_cultist
        self.lunar_pillars: PillarsInfo = lunar_pillars
        self.old_ones_army: OldOnesArmyTiers = old_ones_army
        self.empress_of_light: bool = empress_of_light
        self.queen_slime: bool = queen_slime

    def __repr__(self):
        return f"<BossesDefeated>"
