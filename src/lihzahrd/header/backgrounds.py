from .fourpartsplit import FourPartSplit


class Backgrounds:
    """The backgrounds of various world biomes."""

    def __init__(
        self,
        underground_snow: int,
        underground_jungle: int,
        hell: int,
        forest: FourPartSplit,
        corruption: int,
        jungle: int,
        snow: int,
        hallow: int,
        crimson: int,
        desert: int,
        ocean: int,
        mushroom: int,
        underworld: int,
    ):
        self.underground_snow: int = underground_snow
        self.underground_jungle: int = underground_jungle
        self.hell: int = hell
        self.forest: FourPartSplit = forest
        self.corruption: int = corruption
        self.jungle: int = jungle
        self.snow: int = snow
        self.hallow: int = hallow
        self.crimson: int = crimson
        self.desert: int = desert
        self.ocean: int = ocean
        self.mushroom: int = mushroom
        self.underworld: int = underworld

    def __repr__(self):
        return (
            f"WorldBackgrounds({self.underground_snow}, {self.underground_jungle}, {self.hell},"
            f" {self.forest}, {self.corruption}, {self.jungle}, {self.snow}, {self.hallow},"
            f" {self.crimson}, {self.desert}, {self.ocean},"
            f" {self.mushroom}, {self.underworld})"
        )
