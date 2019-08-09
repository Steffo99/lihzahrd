import enum


class RLEEncoding(enum.IntEnum):
    NO_COMPRESSION = 0
    SINGLE_BYTE = 1
    DOUBLE_BYTE = 2

    @classmethod
    def from_flags(cls, flags1):
        return cls(flags1[7] * 2 + flags1[6])
