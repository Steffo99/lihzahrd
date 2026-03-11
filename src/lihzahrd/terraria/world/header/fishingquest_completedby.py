from logging import getLogger
from typing import Any, override

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class FishingQuestCompletedBy(PackPrimitive[list[str]]):
    """
    List of names of the players who completed today's Angler Fishing Quest.
    """

    _LOG = getLogger(__name__)

    class ListOverflowError(PackPrimitive[list[str]].ValidationError):
        """
        The list contains more items than how many can possibly be represented.
        """

    @classmethod
    @override
    def _validate(cls, value: list[str], **kwargs: Any) -> None:
        length = len(value)
        if not FileProcessor.INT_MIN <= length <= FileProcessor.INT_MAX:
            raise cls.ListOverflowError(value)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> list[str]:
        length = fp.read_int()
        names: list[str] = []
        for _ in range(length):
            name = fp.read_string_variable()
            names.append(name)
        return names

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: list[str], **kwargs: Any) -> None:
        length = len(value)
        fp.write_int(length)
        for item in value:
            fp.write_string_variable(item)


__all__ = ("FishingQuestCompletedBy",)
