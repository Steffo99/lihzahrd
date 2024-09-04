from .moonstyle import MoonStyle
from .fourpartsplit import FourPartSplit


class Styles:
    """The styles of various world elements."""

    def __init__(
        self,
        moon: MoonStyle,
        trees: FourPartSplit,
        moss: FourPartSplit,
    ):
        self.moon: MoonStyle = moon
        self.trees: FourPartSplit = trees
        self.moss: FourPartSplit = moss

    def __repr__(self):
        return f"WorldStyles(moon={repr(self.moon)}, trees={repr(self.trees)}, moss={repr(self.moss)})"
