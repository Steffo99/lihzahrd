from typing import Self

from lihzahrd.fileutils import VersionedPackable, FilePacker
from lihzahrd.header import Version


class Header(VersionedPackable):
    def __init__(self):
        self.name: str = name
        """The name the world was given at creation. Doesn't always match the filename."""

        self.generator: GeneratorInfo = generator
        """Information about the generation of this world."""

        self.uuid: UUID = uuid
        """The Universally Unique ID of this world."""

    def serialize(self, f: FilePacker, v: Version):
        f.write_uint8(self.value)

    @classmethod
    def deserialize(cls, f: FilePacker, v: Version) -> Self:
        return cls(f.read_uint8())