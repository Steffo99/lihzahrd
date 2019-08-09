import enum


class Liquid(enum.IntEnum):
    NO_LIQUID = 0
    WATER = 1
    LAVA = 2
    HONEY = 3

    @classmethod
    def from_flags(cls, flags1):
        if flags1[3] and flags1[4]:
            return cls.HONEY
        if flags1[4]:
            return cls.LAVA
        if flags1[3]:
            return cls.WATER
        return cls.NO_LIQUID
