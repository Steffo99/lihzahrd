import enum


class Difficulty(enum.IntEnum):
    JOURNEY = 3
    CLASSIC = 0
    EXPERT = 1
    MASTER = 2

    def __repr__(self):
        return f"{self.__class__.__qualname__}.{self.NAME}"
