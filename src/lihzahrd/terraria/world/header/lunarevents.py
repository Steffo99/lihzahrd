from .pillarsinfo import PillarsInfo


class LunarEvents:
    """Lunar Events (Lunar Pillars) related information."""

    def __init__(self, are_active: bool, pillars_present: PillarsInfo):
        self.are_active: bool = are_active
        """If the Lunar Events are active or not."""

        self.pillars_present: PillarsInfo = pillars_present
        """Which pillars are currently present in the world."""

    def __repr__(self):
        return f"WorldLunarEvents(are_active={self.are_active}, pillars_present={repr(self.pillars_present)})"
