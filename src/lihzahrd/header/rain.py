class Rain:
    """Rain related information."""

    def __init__(self, is_active: bool, time_left: int, max_rain: float):
        self.is_active: bool = is_active
        """If it is currently raining in the world."""

        self.time_left: int = time_left
        """How long it will continue to rain for."""

        self.max_rain: float = max_rain

    def __repr__(self):
        return f"WorldRain(is_active={self.is_active}, time_left={self.time_left}, max_rain={self.max_rain})"
