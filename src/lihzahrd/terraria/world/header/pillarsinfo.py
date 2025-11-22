class PillarsInfo:
    """A container for information associated with the Lunar Pillars."""

    def __init__(self, solar, vortex, nebula, stardust):
        self.solar = solar
        self.vortex = vortex
        self.nebula = nebula
        self.stardust = stardust

    def __repr__(self):
        return f"PillarsInfo(solar={self.solar}, vortex={self.vortex}, nebula={self.nebula}, stardust={self.stardust})"
