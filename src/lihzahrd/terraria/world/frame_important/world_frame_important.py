# language=rst
"""
Submodule containing :class:`.WorldSections`.
"""

from itertools import batched
from logging import getLogger
from math import ceil

from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class WorldFrameImportant(PackPrimitive[list[bool]]):
    """
    :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` representing a variable-length :class:`list` of :class:`bool` denoting whether each block ID was written to the file as :term:`FrameImportant` or not.
    """

    _LOG = getLogger(__name__)

    class TooManyItemsError(PackPrimitive[list[bool]].ValidationError):
        """
        There are more items in the list than how many can be represented.
        """

    def __getitem__(self, key: int) -> bool:
        """
        Check whether the block ID ``key`` was written as :term:`FrameImportant` or not.

        If the inner :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` does not have as many entries as required by ``key``, return :obj:`False`.

        :param key: The block ID to check.
        :return: Whether it is :term:`FrameImportant`.
        """
        try:
            return self.value[key]
        except IndexError:
            return False

    def __setitem__(self, key: int, value: bool) -> None:
        """
        Mark the block ID ``key`` as positively or negatively :term:`FrameImportant`.

        If the inner :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` does not have as many entries as required by ``key``, create them, and initialize them as :obj:`False`.

        :param key: The block ID to alter the value of.
        :param value: Whether it should be :term:`FrameImportant`.
        """
        try:
            self.value[key] = value
        except IndexError:
            length = len(self.value)
            while length < key:
                self.value.append(False)
            self.value.append(value)

    @classmethod
    def _validate(cls, value: list[bool], **kwargs) -> None:
        super()._validate(value, **kwargs)

        if not FileProcessor.SHORT_MIN <= len(value) <= FileProcessor.SHORT_MAX:
            raise cls.TooManyItemsError(value)

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs) -> list[bool]:
        count = fp.read_short()
        count_bytes = ceil(count / 8)
        value: list[bool] = []

        for _byte in range(count_bytes):
            bits = fp.read_bits()
            value += bits

        return value[0:count]

    @classmethod
    def _write(cls, fp: FileProcessor, value: list[bool], **kwargs) -> None:
        count = len(value)
        fp.write_short(count)

        for byte in batched(value, n=8):
            while len(byte) < 8:
                # noinspection PyTypeChecker
                byte = (*byte, False)
            byte: tuple[bool, bool, bool, bool, bool, bool, bool, bool]
            fp.write_bits(byte)


__all__ = ("WorldFrameImportant",)
