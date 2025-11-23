from typing import Self

from ..version import Version
from ..worldversionedpackable import WorldVersionedPackable
from ...utils import FilePacker


class Generator(WorldVersionedPackable):
    """Information about how a world was generated."""

    def __init__(self, seed_, version_):
        self.seed = seed_
        """The seed used for generation."""

        self.version = version_
        """The generator version used for generation."""

    def serialize(self, f: FilePacker, *, v: Version) -> None:
        f.write_string_variable(self.seed)
        f.write_uint8(self.version)

    @classmethod
    def deserialize(cls, f: FilePacker, *, v: Version) -> Self:
        seed_ = f.read_string_variable()
        version_ = f.read_uint8()
        return cls(
            seed_=seed_,
            version_=version_,
        )

    def __repr__(self) -> str:
        seed_ = self.seed
        version_ = self.version
        return f"{self.__class__.__qualname__}({seed_=}, {version_=})"

    def __eq__(self, other: "Generator") -> bool:
        """
        Determine if two worlds were generated in the same way.
        """
        return self.seed == other.seed and self.version == other.version
