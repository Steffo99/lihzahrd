from itertools import product

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

    def __bool__(self):
        return self.red or self.green or self.blue or self.yellow or self.actuator

    @classmethod
    def from_flags(cls, flags2=None, flags3=None):
        return cls._CACHE[(flags2 or (False,) * 8) + (flags3 or (False,) * 8)]

    @classmethod
    def from_flags_no_cache(cls, flags2=None, flags3=None):
        if flags2 is not None:
            if flags3 is not None:
                return cls(red=flags2[1], green=flags2[2], blue=flags2[3], yellow=flags3[5], actuator=flags3[1])
            return cls(red=flags2[1], green=flags2[2], blue=flags2[3])
        return cls()

Wiring._CACHE = {
    c: Wiring.from_flags_no_cache(c[0:8], c[8:16]) for c in product((True, False), repeat=16)
}
