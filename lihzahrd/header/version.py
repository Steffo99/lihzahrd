import typing


class Version:
    """A Terraria version."""

    __slots__ = ("id", )

    _version_ids = {
        71: "1.2.0.3.1",
        77: "1.2.2",
        104: "1.2.3",
        140: "1.3.0.1",
        151: "1.3.0.4",
        153: "1.3.0.5",
        154: "1.3.0.6",
        155: "1.3.0.7",
        156: "1.3.0.8",
        170: "1.3.2",
        174: "1.3.3",
        178: "1.3.4",
        194: "1.3.5.3"
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
