import enum


class Liquid(enum.IntEnum):
    NO_LIQUID = 0
    WATER = 1
    LAVA = 2
    HONEY = 3

    @classmethod
    def from_flags(cls, flags13, flags14):
        if flags13 and flags14:
            return cls.HONEY
        if flags14:
            return cls.LAVA
        if flags13:
            return cls.WATER
        return cls.NO_LIQUID
