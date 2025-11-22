class JourneyPowers:
    """Journey mode powers settings. Spawn rate does not appear to be stored in the world."""

    __slots__ = (
        "freeze_time",
        "god_mode",
        "time_rate",
        "freeze_rain",
        "freeze_wind",
        "far_placement_range",
        "difficulty",
        "freeze_biome_spread",
    )

    def __init__(
            self,
            freeze_time: bool | None = None,
            time_rate: float | None = None,
            freeze_rain: bool | None = None,
            freeze_wind: bool | None = None,
            difficulty: float | None = None,
            freeze_biome_spread: bool | None = None,
    ):
        self.freeze_time: bool | None = freeze_time
        """Is time frozen?"""

        self.time_rate: float | None = time_rate
        """How fast does time go, 1x to 24x. Value ranges from 0.0 to 1.0."""

        self.freeze_rain: bool | None = freeze_rain
        """Can the rain change."""

        self.freeze_wind: bool | None = freeze_wind
        """Can the wind speed and direction change."""

        self.difficulty: float | None = difficulty
        """Enemy difficulty scaling, 0.5x to 3x. Value ranges from 0.0 to 1.0."""

        self.freeze_biome_spread: bool | None = freeze_biome_spread
        """Can evil biomes & the hallow spread."""

    def __repr__(self):
        return (
            f"JourneyPowers("
            f"freeze_time={self.freeze_time},"
            f" freeze_rain={self.freeze_rain},"
            f" freeze_wind={self.freeze_wind},"
            f" freeze_biome_spread={self.freeze_biome_spread},"
            f" time_rate={self.time_rate},"
            f" difficulty={self.difficulty}"
            f")"
        )
