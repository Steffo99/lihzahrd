from logging import getLogger
from typing import override, Any

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class BannerKillCounts(PackPrimitive[list[int]]):
    """
    Counts of enemies killed for banner purposes, by enemy ID.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        total = sum(self.value)
        return f"<{self.__class__.__qualname__}: {total} total kills>"

    class UnknownListLengthError(PackPrimitive[list[int]].ValidationError):
        """
        The list contains more items than how many there usually are in a Terraria version.
        """

    class OverflowError(PackPrimitive[list[int]].ValidationError):
        """
        At least one item in the list is out of representable range.
        """

    EXPECTED_LENGTH = 293

    @classmethod
    @override
    def _validate(cls, value: list[int], **kwargs: Any) -> None:
        length = len(value)
        if length != cls.EXPECTED_LENGTH:
            raise cls.UnknownListLengthError(value)
        for item in value:
            if not FileProcessor.INT_MIN <= item <= FileProcessor.INT_MAX:
                raise cls.OverflowError(value)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> list[int]:
        length = fp.read_short()
        counts: list[int] = []
        for _ in range(length):
            count = fp.read_int()
            counts.append(count)
        return counts

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: list[int], **kwargs: Any) -> None:
        length = len(value)
        fp.write_short(length)
        for item in value:
            fp.write_int(item)


__all__ = ("BannerKillCounts",)
