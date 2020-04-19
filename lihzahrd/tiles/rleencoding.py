from itertools import product
import enum


class RLEEncoding(enum.IntEnum):
    """How the RLE compression is encoded."""

    NO_COMPRESSION = 0
    """The read data refers to a single tile."""

    SINGLE_BYTE = 1
    """The read data refers to 2-255 tiles (1 byte)."""

    DOUBLE_BYTE = 2
    """The read data refers to 256-4800 tiles (2 bytes)."""

    @classmethod
    def from_flags(cls, flags1):
        return cls._CACHE[flags1]

    @classmethod
    def from_flags_no_cache(cls, flags1):
        if flags1[7]:
            return cls(cls.DOUBLE_BYTE)
        if flags1[6]:
            return cls(cls.SINGLE_BYTE)
        return cls(cls.NO_COMPRESSION)

RLEEncoding._CACHE = {
    c: RLEEncoding.from_flags_no_cache(c) for c in product((True, False), repeat=8)
}
