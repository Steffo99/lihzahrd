import enum


class RLEEncoding(enum.IntEnum):
    """How the RLE compression is encoded."""

    NO_COMPRESSION = 0
    """The read data refers to a single tile."""

    SINGLE_BYTE = 1
    """The read data refers to 2-255 tiles (1 byte)."""

    DOUBLE_BYTE = 2
    """The read data refers to 256-4800 tiles (2 bytes)."""

    UNKNOWN_3 = 3
    """The read data refers to unknown tiles, assuming 256-4800 (2 bytes).
    
    Found in certain tModLoader worlds."""

    @classmethod
    def from_flags(cls, flags1):
        return cls(flags1[7] * 2 + flags1[6])
