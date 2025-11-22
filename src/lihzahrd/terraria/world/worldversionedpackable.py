from typing import Self

from ..utils import FilePacker
from .version import Version


class WorldVersionedPackable:
    """
    A :class:`lihzahrd.terraria.utils.Packable` with differences in serialization between :class:`World` :class:`Version`.
    """

    def serialize(self, f: FilePacker, *, v: Version) -> None:
        raise NotImplementedError()

    @classmethod
    def deserialize(cls, f: FilePacker, *, v: Version) -> Self:
        raise NotImplementedError()


__all__ = (
    "WorldVersionedPackable",
)
