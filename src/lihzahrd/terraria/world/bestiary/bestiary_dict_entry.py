# language=rst
"""
Submodule containing :class:`.BestiaryDictEntry`.
"""

from logging import getLogger
from typing import Any

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.world.bestiary.bestiary_dict_data import BestiaryDictData


class BestiaryDictEntry(PackPrimitive[BestiaryDictData]):
    """
    :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` to process a single :class:`~lihzahrd.terraria.world.bestiary.bestiary_dict_data.BestiaryDictData`.
    """

    _LOG = getLogger(__name__)

    ITEM = BestiaryDictData

    @classmethod
    def _validate(cls, value: BestiaryDictData, **kwargs: Any) -> None:
        pass

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> BestiaryDictData:
        return BestiaryDictData(
            name=fp.read_string_variable(),
            count=fp.read_int(),
        )

    @classmethod
    def _write(cls, fp: FileProcessor, value: BestiaryDictData, **kwargs: Any) -> None:
        fp.write_string_variable(value.name)
        fp.write_int(value.count)


__all__ = ("BestiaryDictEntry",)
