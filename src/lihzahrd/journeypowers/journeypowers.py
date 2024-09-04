import typing


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
        freeze_time: typing.Optional[bool] = None,
        time_rate: typing.Optional[float] = None,
        freeze_rain: typing.Optional[bool] = None,
        freeze_wind: typing.Optional[bool] = None,
        difficulty: typing.Optional[float] = None,
        freeze_biome_spread: typing.Optional[bool] = None,
    ):

        self.freeze_time: bool = freeze_time
        """Is time frozen?"""

        self.time_rate: float = time_rate
        """How fast does time go, 1x to 24x. Value ranges from 0.0 to 1.0."""

        self.freeze_rain: bool = freeze_rain
        """Can the rain change."""

        self.freeze_wind: bool = freeze_wind
        """Can the wind speed and direction change."""

        self.difficulty: float = difficulty
        """Enemy difficulty scaling, 0.5x to 3x. Value ranges from 0.0 to 1.0."""

        self.freeze_biome_spread: bool = freeze_biome_spread
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
