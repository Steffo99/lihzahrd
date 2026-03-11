# language=rst
"""
Submodule containing processors for :class:`~uuid.UUID`.
"""

from logging import getLogger
from uuid import UUID

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class PackUUID(PackPrimitive[UUID]):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing a :class:`~uuid.UUID`.
    """

    _LOG = getLogger(__name__)

    @classmethod
    def _validate(cls, value: UUID, **kwargs) -> None:
        super()._validate(value, **kwargs)

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs) -> UUID:
        return fp.read_uuid()

    @classmethod
    def _write(cls, fp: FileProcessor, value: UUID, **kwargs) -> None:
        fp.write_uuid(value)


__all__ = ("PackUUID",)
