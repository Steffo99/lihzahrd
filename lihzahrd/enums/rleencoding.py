import enum
import functools


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
        return cls._from_flags(flags1[6], flags1[7])

    @classmethod
    @functools.lru_cache(3)
    def _from_flags(cls, flags16, flags17):
        return cls(flags17 * 2 + flags16)
