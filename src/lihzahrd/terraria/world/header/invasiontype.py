import enum


class InvasionType(enum.IntEnum):
    NONE = 0
    GOBLIN_INVASION = 1
    FROST_LEGION = 2
    PIRATE_INVASION = 3
    MARTIAN_MADNESS = 4

    def __repr__(self):
        return f"InvasionType('{self.name}')"
