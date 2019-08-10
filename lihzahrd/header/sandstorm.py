class Sandstorm:
    """Sandstorm related information."""
    def __init__(self,
                 is_active: bool,
                 time_left: int,
                 severity: float,
                 intended_severity: float):
        self.is_active: bool = is_active
        """If a sandstorm is currently ongoing in the desert."""

        self.time_left: int = time_left
        """How long the sandstorm will continue for."""

        self.severity: float = severity
        self.intended_severity: float = intended_severity

    def __repr__(self):
        return f"WorldSandstorm(is_active={self.is_active}, time_left={self.time_left}," \
               f" severity={self.severity}, intended_severity={self.intended_severity})"
