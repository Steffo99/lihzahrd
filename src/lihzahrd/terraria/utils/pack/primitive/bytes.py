# language=rst
"""
Submodule containing processors for raw bytes.
"""

from logging import getLogger
from typing import Any

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class PackUnknown(PackPrimitive[bytes]):
    """
    A :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing blocks of raw :class:`bytes`.

    When this class starts a :meth:`~lihzahrd.terraria.utils.pack.pack.Pack.read`, it keeps on reading until it reaches the address specified by the ``until`` keyword argument.

    If instance of this class contain a non-zero amount of bytes, it will fail validation with :exc:`.UnknonwnBytesError` (as that probably means that something went wrong during the parsing of the corresponding save file section), unless the ``acceptable`` keyword argument is :obj:`True`.

    .. tip::

        This behavior can be useful when you want to deliberately skip processing some sections of a save file, because for example they were loaded from a cache.
        This behavior can be useful when you want to deliberately skip processing some sections of a save file, because for example they were loaded from a cache.

    :kwarg until: The byte offset at which to stop reading.
    :kwarg acceptable: If :obj:`True`, no :exc:`.UnknownBytesError` will be raised on validation.
    """

    _LOG = getLogger(__name__)

    class UnknownBytesError(PackPrimitive[bytes].ValidationError):
        """
        Unknown bytes are present.
        """

    def __repr__(self):
        length = len(self.value)
        if length > 0:
            return f"<{self.__class__.__qualname__}: {length} UNKNOWN BYTES!>"
        else:
            return f"<{self.__class__.__qualname__}>"

    @classmethod
    def _validate(cls, value: bytes, **kwargs: Any) -> None:
        super()._validate(value, **kwargs)

        acceptable = kwargs.get("acceptable", False)

        if not acceptable and len(value) != 0:
            raise cls.UnknownBytesError(value)

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> bytes:
        until = kwargs["until"]
        return fp.read_bytes_until(until)

    @classmethod
    def _write(cls, fp: FileProcessor, value: bytes, **kwargs: Any) -> None:
        fp.write_bytes(value)


__all__ = ("PackUnknown",)
