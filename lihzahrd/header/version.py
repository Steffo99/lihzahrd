import typing


class Version:
    """A Terraria version."""

    __slots__ = ("id", )

    _version_ids = {
        12: "1.0.5",
        20: "1.0.6",
        22: "1.0.6.1",
        37: "1.1.1",
        39: "1.1.2",
        67: "1.2",
        71: "1.2.0.3.1",
        72: "1.2.1.1",
        73: "1.2.1.2",
        77: "1.2.2",
        94: "1.2.3.1",
        # 104: "1.2.3", This seems like a typo?
        101: "1.2.4",
        102: "1.2.4.1",
        140: "1.3.0.1",
        146: "1.3.0.1",
        147: "1.3.0.2",
        149: "1.3.0.3",
        151: "1.3.0.4",
        153: "1.3.0.5",
        154: "1.3.0.6",
        155: "1.3.0.7",
        156: "1.3.0.8",
        168: "1.3.1",
        169: "1.3.1.1",
        170: "1.3.2",
        173: "1.3.2.1",
        174: "1.3.3",
        175: "1.3.3.1",
        176: "1.3.3.2",
        177: "1.3.3.3",
        178: "1.3.4",
        185: "1.3.4.1",
        186: "1.3.4.2",
        187: "1.3.4.3",
        188: "1.3.4.4",
        191: "1.3.5",
        192: "1.3.5.1",
        193: "1.3.5.2",
        194: "1.3.5.3",
        225: "1.4.0.1",
        226: "1.4.0.2",
        227: "1.4.0.3",
        228: "1.4.0.4",
        230: "1.4.0.5",
    }

    def __init__(self, data: typing.Union[int, str]):
        if isinstance(data, int):
            self.id = data
        else:
            for version in self._version_ids:
                if self._version_ids[version] == data:
                    self.id = version
                    break
            else:
                raise ValueError("No such version")

    @property
    def name(self):
        # TODO: Add all versions
        try:
            return self._version_ids[self.id]
        except KeyError:
            return "Unknown"

    def __repr__(self):
        return f"Version({self.id})"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other

    def __gt__(self, other):
        return self.id > other

    def __lt__(self, other):
        return self.id < other
