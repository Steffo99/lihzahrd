# language=rst
"""
Submodule containing processors for strings.
"""

from abc import ABCMeta
from logging import getLogger
from typing import Any, override

from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class PackStrFixed(PackPrimitive[str], metaclass=ABCMeta):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing fixed-length strings.

    On validation, it ensures that the represented value is exactly :attr:`DATA_LEN` bytes long, and raises :exc:`.InvalidLengthError` otherwise.
    """

    _LOG = getLogger(__name__)

    DATA_LEN: int = NotImplemented
    "The expected length of the string."

    class InvalidLengthError(PackPrimitive[str].ValidationError):
        """
        The string is not of the required length.
        """

    @classmethod
    @override
    def _validate(cls, value: str, **kwargs: Any) -> None:
        super()._validate(value, **kwargs)

        assert cls.DATA_LEN is not NotImplemented

        data = bytes(value, encoding="latin1")
        if len(data) != cls.DATA_LEN:
            raise cls.InvalidLengthError(value)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> str:
        return fp.read_string_raw(count=cls.DATA_LEN)

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: str, **kwargs: Any) -> None:
        fp.write_string_raw(value)


class PackStrVariable(PackPrimitive[str]):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing variable-length strings.
    """

    _LOG = getLogger(__name__)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> str:
        return fp.read_string_variable()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: str, **kwargs: Any) -> None:
        fp.write_string_variable(value)


__all__ = (
    "PackStrFixed",
    "PackStrVariable",
)
