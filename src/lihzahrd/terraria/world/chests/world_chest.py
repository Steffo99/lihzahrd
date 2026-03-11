# language=rst
"""
Submodule containing :class:`.WorldChest`.
"""

from logging import getLogger
from typing import Any

from lihzahrd.terraria.data.classenums.item_enum import ItemEnum
from lihzahrd.terraria.data.classenums.prefix_enum import PrefixEnum
from lihzahrd.terraria.data.classmembers.item_base import ItemBase
from lihzahrd.terraria.data.classmembers.prefix_base import PrefixBase
from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.pack import Pack
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.utils.structures.coordinates import Coordinates
from lihzahrd.terraria.world.chests.world_chest_data import WorldChestData


class WorldChest(PackPrimitive[WorldChestData]):
    """
    :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` to process a storage container (a chest) in a Terraria world.
    """

    _LOG = getLogger(__name__)

    EXPECTED_CONTAINER_SIZE = 40
    "The number of stacks that can be stored in a single container."

    class UnknownContainerSizeError(Pack.ValidationError):
        """
        At least one container has a different amount of items than the number normally allowed in a Terraria version.
        """

    @classmethod
    def _validate(cls, value: WorldChestData, **kwargs: Any) -> None:
        if len(value.contents) != cls.EXPECTED_CONTAINER_SIZE:
            raise cls.UnknownContainerSizeError()

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> WorldChestData:
        position = Coordinates(
            x=fp.read_int(),
            y=fp.read_int(),
        )

        name = fp.read_string_variable()

        size = fp.read_int()
        contents = []
        for slot in range(size):
            quantity = fp.read_short()

            if quantity == 0:
                contents.append(None)
                continue

            item_kind = fp.read_int()
            prefix_kind = fp.read_byte()

            item_class: type[ItemBase] = ItemEnum.INDEXES["ID"][item_kind]
            prefix_class: type[PrefixBase] = PrefixEnum.INDEXES["ID"][prefix_kind] if prefix_kind != 0 else None

            item = item_class(
                quantity=quantity,
                prefix=prefix_class,
            )
            contents.append(item)

        return WorldChestData(
            position=position,
            name=name,
            contents=contents,
        )

    @classmethod
    def _write(cls, fp: FileProcessor, value: WorldChestData, **kwargs: Any) -> None:
        fp.write_int(value.position.x)
        fp.write_int(value.position.y)

        fp.write_string_variable(value.name)

        fp.write_int(len(value.contents))
        for item in value.contents:
            if item is None:
                fp.write_short(0)
            else:
                fp.write_short(item.quantity)
                fp.write_int(item.ID)
                if item.prefix:
                    fp.write_byte(item.prefix.ID)
                else:
                    fp.write_byte(0)


__all__ = ("WorldChest",)
