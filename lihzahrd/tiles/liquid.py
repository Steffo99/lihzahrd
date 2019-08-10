from .liquidtype import LiquidType


class Liquid:
    def __init__(self, type_: LiquidType, volume: int):
        self.type: LiquidType = type_
        self.volume: int = volume
