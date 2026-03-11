# language=rst
"""
Submodule containing processors for :class:`~datetime.datetime`.
"""

from datetime import datetime
from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.op.comparison import OpComparison


class PackDatetime(OpComparison[datetime]):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing a :class:`~datetime.datetime`.
    """

    _LOG = getLogger(__name__)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs) -> datetime:
        return fp.read_datetime()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: datetime, **kwargs) -> None:
        fp.write_datetime(value)


__all__ = ("PackDatetime",)
