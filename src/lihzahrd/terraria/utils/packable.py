from typing import Self

from .filepacker import FilePacker


class Packable:
    """
    An object which can be serialized and deserialized via a :class:`lihzahrd.utils.FilePacker`.
    """

    def serialize(self, f: FilePacker) -> None:
        raise NotImplementedError()

    @classmethod
    def deserialize(cls, f: FilePacker) -> Self:
        raise NotImplementedError()


__all__ = (
    "Packable",
)