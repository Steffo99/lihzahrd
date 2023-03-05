import enum
import functools


class LiquidType(enum.IntEnum):
    """All possible types of liquids."""

    NO_LIQUID = 0
    WATER = 1
    LAVA = 2
    HONEY = 3
    SHIMMER = 4

    @classmethod
    def from_flags(cls, flags1, flags3=None):
        return cls._from_flags(flags1[3], flags1[4], flags3[7] if flags3 else False)

    @classmethod
    @functools.lru_cache(4)
    def _from_flags(cls, flags13, flags14, flags37):
        if flags37:
            return cls.SHIMMER
        if flags13 and flags14:
            return cls.HONEY
        if flags14:
            return cls.LAVA
        if flags13:
            return cls.WATER
        return cls.NO_LIQUID

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"
