class ShadowOrbs:
    """Information related to the Shadow Orbs (or the Crimson Hearts) smashed in the world."""

    def __init__(self,
                 smashed_at_least_once: bool,
                 spawn_meteorite: bool,
                 evil_boss_counter: int):
        self.smashed_at_least_once: bool = smashed_at_least_once
        """If a Shadow Orb has ever been smashed in this world."""

        self.spawn_meteorite: bool = spawn_meteorite
        """If a Meteorite should land in the world at midnight.

        It is set to True when a Shadow Orb is smashed, then it is set to False when the meteorite actually lands."""

        self.evil_boss_counter: int = evil_boss_counter
        """If it is 2, the Eater of Worlds will spawn when a Shadow Orb is smashed.

        It is the number of Shadow Orbs broken, modulo 3."""

    def __repr__(self):
        return f"WorldShadowOrbs(smashed_at_least_once={self.smashed_at_least_once}," \
               f" spawn_meteorite={self.spawn_meteorite}, evil_boss_counter={self.evil_boss_counter})"
