class Time:
    """Game time related information."""
    def __init__(self, current: float,
                 is_daytime: bool,
                 moon_phase: int,
                 sundial_cooldown: int,
                 fast_forward_time: bool):
        self.current: float = current
        """The current game time."""

        self.is_daytime: bool = is_daytime
        """If the current time represents a day or a night."""

        self.moon_phase: int = moon_phase
        """The current moon phase."""

        self.sundial_cooldown: int = sundial_cooldown
        """The number of days the Enchanted Sundial can't be used for."""

        self.fast_forward_time: bool = fast_forward_time

    def __repr__(self):
        return f"WorldTime(current={self.current}, is_daytime={self.is_daytime}, moon_phase={self.moon_phase}," \
               f" sundial_cooldown={self.sundial_cooldown}, fast_forward_time={self.fast_forward_time})"
