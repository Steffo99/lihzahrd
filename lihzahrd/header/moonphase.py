import enum


class MoonPhase(enum.IntEnum):
    FULL_MOON = 0
    WANING_GIBBOUS = 1
    THIRD_QUARTER = 2
    WANING_CRESCENT = 3
    NEW_MOON = 4
    WAXING_CRESCENT = 5
    FIRST_QUARTER = 6
    WAXING_GIBBOUS = 7

    def __repr__(self):
        return f"MoonPhases('{self.name}')"
