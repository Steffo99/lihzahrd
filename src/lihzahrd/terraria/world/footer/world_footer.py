# language=rst
"""
Submodule containing :class:`.WorldFooter`.
"""

from typing import Self, override

from lihzahrd.terraria.utils.pack.composite.composite import PackComposite as PaCo
from lihzahrd.terraria.utils.pack.pack import Pack
from lihzahrd.terraria.utils.pack.primitive.bool import PackTrue
from lihzahrd.terraria.world.header.world_id import WorldID
from lihzahrd.terraria.world.header.world_name import WorldName


class WorldFooter(PaCo):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.composite.PackComposite` representing the footer of a Terraria world.
    """

    true: PaCo.Field[Self, PackTrue] = PaCo.Field(PackTrue)
    "A value which needs to always be ``1`` for the world to be valid."

    name: PaCo.Field[Self, WorldName] = PaCo.Field(WorldName)
    "The world's :attr:`~lihzahrd.terraria.world.header.world_header.WorldHeader.name`... again. Must be the same to pass validation."

    id: PaCo.Field[Self, WorldID] = PaCo.Field(WorldID)
    "The world's :attr:`~lihzahrd.terraria.world.header.world_header.WorldHeader.id`... again. Must be the same to pass validation."

    # noinspection PyTypeChecker
    @override
    def __init__(self, *args):
        self.true: PackTrue = ...
        self.name: WorldName = ...
        self.id: WorldID = ...
        super().__init__(*args)

    @override
    @classmethod
    def _fields(cls, **kwargs) -> list[PaCo.Field[Self, Pack]]:
        return [
            cls.true,
            cls.name,
            cls.id,
        ]


__all__ = ("WorldFooter",)
