from typing import Self

from ..utils import Packable, FilePacker


class Version(Packable):
    """A Terraria version."""

    # TODO: Add all versions
    VERSION_IDS = {
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
        238: "1.4.2.3",
        274: "1.4.4.5",
        278: "1.4.4.8",
        279: "1.4.4.9",
    }

    __slots__ = ("id",)

    def __init__(self, data: int | str):
        if isinstance(data, int):
            self.id = data
        else:
            for version in self.VERSION_IDS:
                if self.VERSION_IDS[version] == data:
                    self.id = version
                    break
            else:
                raise ValueError("No such version")

    def serialize(self, f: FilePacker) -> None:
        f.write_int4(self.id)

    @classmethod
    def deserialize(cls, f: FilePacker) -> Self:
        return cls(f.read_int4())

    def __repr__(self) -> str:
        """
        :return: The expression to create the same :class:`.Version` object.
        """
        return f"Version({self.id})"

    def name(self) -> str:
        """
        :return: The name of the version, for example, `"1.4.4.9"`.
        :raises KeyError: If the name of the version is not known.
        """
        return self.VERSION_IDS[self.id]

    def __str__(self) -> str:
        """
        :return: The name of the version, for example, `"1.4.4.9"`, or `"Unknown ({id})"` if it isn't known.
        """
        try:
            return self.name()
        except KeyError:
            return f"Unknown ({self.id})"

    def __eq__(self, other) -> bool:
        """
        :return: If two versions match.
        """
        return self.id == other.id

    def __gt__(self, other) -> bool:
        """
        :return: If the version on the left is more recent than the one on the right.
        """
        return self.id > other.id

    def __ge__(self, other) -> bool:
        """
        :return: If the version on the left is greater or equal to the one on the right.
        """
        return self.id >= other.id

    def __lt__(self, other) -> bool:
        """
        :return: If the version on the left is less recent than the one on the right.
        """
        return self.id < other.id

    def __le__(self, other) -> bool:
        """
        :return: If the version on the left is lesser or equal to the one on the right.
        """
        return self.id <= other.id


__all__ = (
    "Version",
)
