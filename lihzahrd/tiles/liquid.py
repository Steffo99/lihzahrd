from .liquidtype import LiquidType


class Liquid:
    __slots__ = "type", "volume"

    def __init__(self, type_: LiquidType, volume: int):
        self.type: LiquidType = type_
        self.volume: int = volume
