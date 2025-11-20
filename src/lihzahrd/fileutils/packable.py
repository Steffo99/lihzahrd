from abc import ABCMeta, abstractmethod
from typing import Self

from lihzahrd.fileutils import FilePacker


class Packable(metaclass=ABCMeta):
    """
    An object which can be serialized and deserialized via a :class:`lihzahrd.fileutils.FilePacker`.
    """

    @abstractmethod
    def write(self, f: FilePacker):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def read(cls, f: FilePacker) -> Self:
        raise NotImplementedError()
