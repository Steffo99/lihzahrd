# language=rst
"""
Submodule containing processors for integer types.
"""

from abc import ABCMeta
from logging import getLogger
from typing import Any, override

from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class PackInteger(PackPrimitive[int], metaclass=ABCMeta):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing integers.

    On validation, it ensures that the represented value is between :attr:`.VALUE_MIN` and :attr:`.VALUE_MAX`, and raises :exc:`OverflowError` otherwise.
    """

    _LOG = getLogger(__name__)

    VALUE_MIN: int = NotImplemented
    "The minimum value that this type of integer can take."

    VALUE_MAX: int = NotImplemented
    "The maximum value that this type of integer can take."

    class OverflowError(PackPrimitive[int].ValidationError):
        """
        The processed value is out of representable range.
        """

    @classmethod
    @override
    def _validate(cls, value: int, **kwargs: Any) -> None:
        super()._validate(value, **kwargs)

        assert cls.VALUE_MIN is not NotImplemented
        assert cls.VALUE_MAX is not NotImplemented

        if not cls.VALUE_MIN <= value <= cls.VALUE_MAX:
            raise cls.OverflowError(value)


class PackSByte(PackInteger):
    """
    A :class:`.PackInteger` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.SBYTE` as :class:`int`.
    """

    _LOG = getLogger(__name__)

    VALUE_MIN = FileProcessor.SBYTE_MIN
    VALUE_MAX = FileProcessor.SBYTE_MAX

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> int:
        return fp.read_sbyte()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: int, **kwargs: Any) -> None:
        fp.write_sbyte(value)


class PackByte(PackInteger):
    """
    A :class:`.PackInteger` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.BYTE` as :class:`int`.
    """

    _LOG = getLogger(__name__)

    VALUE_MIN = FileProcessor.BYTE_MIN
    VALUE_MAX = FileProcessor.BYTE_MAX

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> int:
        return fp.read_byte()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: int, **kwargs: Any) -> None:
        fp.write_byte(value)


class PackShort(PackInteger):
    """
    A :class:`.PackInteger` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.SHORT` as :class:`int`.
    """

    _LOG = getLogger(__name__)

    VALUE_MIN = FileProcessor.SHORT_MIN
    VALUE_MAX = FileProcessor.SHORT_MAX

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> int:
        return fp.read_short()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: int, **kwargs: Any) -> None:
        fp.write_short(value)


class PackUShort(PackInteger):
    """
    A :class:`.PackInteger` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.USHORT` as :class:`int`.
    """

    _LOG = getLogger(__name__)

    VALUE_MIN = FileProcessor.USHORT_MIN
    VALUE_MAX = FileProcessor.USHORT_MAX

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> int:
        return fp.read_ushort()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: int, **kwargs: Any) -> None:
        fp.write_ushort(value)


class PackInt(PackInteger):
    """
    A :class:`.PackInteger` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.INT` as :class:`int`.
    """

    _LOG = getLogger(__name__)

    VALUE_MIN = FileProcessor.INT_MIN
    VALUE_MAX = FileProcessor.INT_MAX

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> int:
        return fp.read_int()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: int, **kwargs: Any) -> None:
        fp.write_int(value)


class PackUInt(PackInteger):
    """
    A :class:`.PackInteger` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.UINT` as :class:`int`.
    """

    _LOG = getLogger(__name__)

    VALUE_MIN = FileProcessor.UINT_MIN
    VALUE_MAX = FileProcessor.UINT_MAX

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> int:
        return fp.read_uint()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: int, **kwargs: Any) -> None:
        fp.write_uint(value)


class PackLong(PackInteger):
    """
    A :class:`.PackInteger` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.LONG` as :class:`int`.
    """

    _LOG = getLogger(__name__)

    VALUE_MIN = FileProcessor.LONG_MIN
    VALUE_MAX = FileProcessor.LONG_MAX

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> int:
        return fp.read_long()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: int, **kwargs: Any) -> None:
        fp.write_long(value)


class PackULong(PackInteger):
    """
    A :class:`.PackInteger` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.ULONG` as :class:`int`.
    """

    _LOG = getLogger(__name__)

    VALUE_MIN = FileProcessor.ULONG_MIN
    VALUE_MAX = FileProcessor.ULONG_MAX

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> int:
        return fp.read_ulong()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: int, **kwargs: Any) -> None:
        fp.write_ulong(value)


__all__ = (
    "PackInteger",
    "PackSByte",
    "PackByte",
    "PackShort",
    "PackUShort",
    "PackInt",
    "PackUInt",
    "PackLong",
    "PackULong",
)
