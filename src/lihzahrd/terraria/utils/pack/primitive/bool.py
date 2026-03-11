# language=rst
"""
Submodule containing processors for boolean types.
"""

from logging import getLogger
from typing import Any, override

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class PackBool(PackPrimitive[bool]):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing a :attr:`~lihzahrd.terraria.utils.file_processor.FileProcessor.BOOL` as :class:`bool`.
    """

    _LOG = getLogger(__name__)

    @classmethod
    @override
    def _validate(cls, value: bool, **kwargs: Any) -> None:
        super()._validate(value, **kwargs)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> bool:
        return fp.read_bool()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: bool, **kwargs: Any) -> None:
        fp.write_bool(value)


class PackTrue(PackBool):
    """
    A :class:`PackBool` where only :obj:`True` values pass validation, and :obj:`False` values raise :exc:`.IsFalseError`.
    """

    class IsFalseError(PackBool.ValidationError):
        """
        The value is :obj:`False`.
        """

    @classmethod
    @override
    def _validate(cls, value: bool, **kwargs: Any) -> None:
        super()._validate(value, **kwargs)
        if not value:
            raise cls.IsFalseError(value)


__all__ = (
    "PackBool",
    "PackTrue",
)
