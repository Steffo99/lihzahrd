import enum


class HardmodeTier1Ore(enum.IntEnum):
    NOT_DETERMINED = -1
    COBALT = 107
    PALLADIUM = 221

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


class HardmodeTier2Ore(enum.IntEnum):
    NOT_DETERMINED = -1
    MYTHRIL = 108
    ORICHALCUM = 222

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


class HardmodeTier3Ore(enum.IntEnum):
    NOT_DETERMINED = -1
    NOT_DETERMINED_TOO = 16785407  # ???
    ADAMANTITE = 111
    TITANIUM = 223

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"
