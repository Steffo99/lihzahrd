from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Self, TYPE_CHECKING

from lihzahrd.fileutils import FilePacker

if TYPE_CHECKING:
    from lihzahrd.header import Version


class Packable(metaclass=ABCMeta):
    """
    An object which can be serialized and deserialized via a :class:`lihzahrd.fileutils.FilePacker`.
    """

    @abstractmethod
    def write(self, f: FilePacker, v: Version | None):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def read(cls, f: FilePacker, v: Version | None) -> Self:
        raise NotImplementedError()
