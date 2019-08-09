import enum


class WorldEvilType(enum.Enum):
    CORRUPTION = False
    CRIMSON = True

    def __repr__(self):
        return f"CorruptionType('{self.name}')"
