import typing


class LanternNight:
    """Lantern Night event related information."""
    def __init__(self,
                 nights_on_cooldown: int,
                 genuine: bool,
                 manual: bool,
                 next_night_is_lantern_night: bool):
        self.nights_on_cooldown: int = nights_on_cooldown
        """How many nights before the next lantern night can happen."""

        self.genuine: bool = genuine
        """Was this night started by the game spontaneously?"""

        self.manual: bool = manual
        """Was this night started by the player?"""

        self.next_night_is_lantern_night: bool = next_night_is_lantern_night
        """Was a boss just defeated, making the next night a Lantern Night?"""

    def __repr__(self):
        return f"WorldLanternNight(nights_on_cooldown={self.nights_on_cooldown}," \
               f" genuine={self.genuine}, manual={self.manual}, nights_on_cooldown={self.nights_on_cooldown})"

    @property
    def is_active(self):
        return self.genuine or self.manual  # ToDo: Test this!
