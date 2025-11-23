import enum


class Difficulty(enum.IntEnum):
    JOURNEY = 3
    """Journey mode."""

    CLASSIC = 0
    """Classic mode, or Expert mode in for-the-worthy worlds."""

    EXPERT = 1
    """Expert mode, or Master mode in for-the-worthy worlds."""

    MASTER = 2
    """Master mode, or Legendary mode in for-the-worthy worlds."""

    def __repr__(self):
        return f"{self.__class__.__qualname__}.{self.name}"
