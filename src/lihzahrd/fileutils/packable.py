from __future__ import annotations

from typing import Self, TYPE_CHECKING

from lihzahrd.fileutils import FilePacker

if TYPE_CHECKING:
    from lihzahrd.header import Version


class Packable:
    """
    An object which can be serialized and deserialized via a :class:`lihzahrd.fileutils.FilePacker`.
    """

    def write(self, f: FilePacker, v: Version | None):
        raise NotImplementedError()

    @classmethod
    def read(cls, f: FilePacker, v: Version | None) -> Self:
        raise NotImplementedError()
