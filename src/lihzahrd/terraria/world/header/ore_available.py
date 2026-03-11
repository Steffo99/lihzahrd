from logging import getLogger
from typing import Any, override

from lihzahrd.terraria.data.classmembers.block_base import BlockBase
from lihzahrd.terraria.data.classenums.block_enum import BlockEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class OreAvailable(PackInt):
    """
    The kind of ore that's available in a Terraria world.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        tile = self.get_block()
        if tile is not None:
            return f"<{self.__class__.__qualname__}: {tile.__qualname__}>"
        else:
            return f"<{self.__class__.__qualname__}: undetermined>"

    def get_block(self) -> type[BlockBase] | None:
        """
        Convert :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` into a block :term:`ClassMember`.

        :return: :obj:`None` if no ore has been selected yet or the block kind if it exists.
        :raise ValueError: If no corresponding Tile exists.
        """
        if self.value == -1:
            return None

        # noinspection PyTypeChecker
        tile: type[BlockBase] = BlockEnum.INDEXES["ID"][self.value]

        if tile:
            return tile
        else:
            raise ValueError("Tile ID is unknown: ", self.value)

    def set_from_block(self, block: type[BlockBase] | None) -> None:
        """
        Set :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` from the given block :term:`ClassMember`.

        :param block: The kind of the block to set, or :obj:`None` to mark this as not selected yet.
        """
        if block is None:
            self.value = -1
        else:
            self.value = block.ID

    class UnknownOreError(PackInt.ValidationError):
        """
        The ore's value does not correspond to any known tile ID, nor it represents an undetermined value.
        """

    @classmethod
    @override
    def _validate(cls, value: int, **kwargs: Any) -> None:
        if value == -1:
            return
        elif _tile := BlockEnum.INDEXES["ID"][value]:
            return
        else:
            raise cls.UnknownOreError(value)


__all__ = ("OreAvailable",)
