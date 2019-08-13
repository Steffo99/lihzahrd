from ..fileutils import Coordinates


class WeighedPressurePlate:
    """A single `Weighed Pressure Plate <https://terraria.gamepedia.com/Pressure_Plates>`_ placed in the world."""

    __slots__ = ("position", )

    def __init__(self, position: Coordinates):
        self.position: Coordinates = position

    def __repr__(self):
        return f"PressurePlate(position={self.position})"
