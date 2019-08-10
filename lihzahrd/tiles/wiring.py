class Wiring:
    """Wiring data for a certain tile."""

    __slots__ = "red", "green", "blue", "yellow", "actuator"

    def __init__(self,
                 red: bool = False,
                 green: bool = False,
                 blue: bool = False,
                 yellow: bool = False,
                 actuator: bool = False):
        self.red: bool = red
        """If there's a red Wire in the tile."""

        self.green: bool = green
        """If there's a green Wire in the tile."""

        self.blue: bool = blue
        """If there's a blue Wire in the tile."""

        self.yellow: bool = yellow
        """If there's a yellow Wire in the tile."""

        self.actuator: bool = actuator
        """If there's an Actuator in the tile."""

    def __repr__(self):
        return f"Wires(red={self.red}, green={self.green}, blue={self.blue}, yellow={self.yellow}," \
               f" actuator={self.actuator})"
