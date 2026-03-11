# language=rst
"""
Submodule containing :class:`.WorldSign`.
"""

from logging import getLogger
from typing import Any

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.utils.structures.coordinates import Coordinates
from lihzahrd.terraria.world.signs.world_sign_data import WorldSignData


class WorldSign(PackPrimitive[WorldSignData]):
    """
    :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` to process a readable block (a sign) in a Terraria world.
    """

    _LOG = getLogger(__name__)

    @classmethod
    def _validate(cls, value: WorldSignData, **kwargs: Any) -> None:
        pass

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> WorldSignData:
        text = fp.read_string_variable()
        position = Coordinates(
            x=fp.read_int(),
            y=fp.read_int(),
        )
        return WorldSignData(
            text=text,
            position=position,
        )

    @classmethod
    def _write(cls, fp: FileProcessor, value: WorldSignData, **kwargs: Any) -> None:
        fp.write_string_variable(value.text)
        fp.write_int(value.position.x)
        fp.write_int(value.position.y)


__all__ = ("WorldSign",)
