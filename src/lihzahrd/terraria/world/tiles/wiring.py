# language=rst
"""
Submodule containing :class:`.Tile`.
"""

from dataclasses import dataclass


@dataclass(kw_only=True, slots=True)
class Wiring:
    """
    The wiring of a Terraria tile.
    """

    has_red: bool = False
    "If the tile has *Red Wire*."

    has_blue: bool = False
    "If the tile has *Blue Wire*."

    has_green: bool = False
    "If the tile has *Green Wire*."

    has_yellow: bool = False
    "If the tile has *Yellow Wire*."

    has_actuator: bool = False
    "If the tile has an *Actuator*."

    def __bool__(self) -> bool:
        """
        :return: Whether the tile has any wiring.
        """
        return self.has_red or self.has_blue or self.has_green or self.has_yellow or self.has_actuator

    def __repr__(self):
        has_red = self.has_red
        has_blue = self.has_blue
        has_green = self.has_green
        has_yellow = self.has_yellow
        has_actuator = self.has_actuator
        params = ""
        if has_red:
            params += f"{has_red=}, "
        if has_blue:
            params += f"{has_blue=}, "
        if has_green:
            params += f"{has_green=}, "
        if has_yellow:
            params += f"{has_yellow=}, "
        if has_actuator:
            params += f"{has_actuator=}"
        return f"{self.__class__.__qualname__}({params})"


__all__ = ("Wiring",)
