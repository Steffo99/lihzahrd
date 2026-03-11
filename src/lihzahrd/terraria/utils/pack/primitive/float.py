# language=rst
"""
Submodule containing processors for floating-point numeric types.
"""

from abc import ABCMeta
from logging import getLogger
from typing import Any, override

from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class PackFloating(PackPrimitive[float], metaclass=ABCMeta):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing floating-point numeric types.
    """


class PackFloat(PackFloating):
    """
    A :class:`.PackFloating` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.FLOAT` as :class:`float`.
    """

    _LOG = getLogger(__name__)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> float:
        return fp.read_float()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: float, **kwargs: Any) -> None:
        fp.write_float(value)


class PackDouble(PackFloating):
    """
    A :class:`.PackDouble` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.FLOAT` as :class:`float`.
    """

    _LOG = getLogger(__name__)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> float:
        return fp.read_double()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: float, **kwargs: Any) -> None:
        fp.write_double(value)


__all__ = (
    "PackFloating",
    "PackFloat",
    "PackDouble",
)
