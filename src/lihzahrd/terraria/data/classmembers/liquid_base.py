# language=rst
"""
Submodule for :class:`.LiquidBase`.
"""

from logging import getLogger

from lihzahrd.terraria.utils.structures.color import ColorRGB

from lihzahrd.terraria.data.classenums.wall_enum import WallEnum
from lihzahrd.terraria.data.enums.paint import PaintEnum

log = getLogger(__name__)


class LiquidBase(metaclass=WallEnum, register=False):
    """
    The kind of Terraria liquid.

    All liquid inherit from this; it's a :term:`ClassMemberBase` for members of :class:`.LiquidEnum`.

    It:

    - annotates the mandatory attributes that all liquids should have.

    :param volume: The volume of the liquid.
    """

    __slots__ = ("volume",)

    ID: int
    "The ID of the prefix."

    NAME: str
    "The prefix."

    COLOR: ColorRGB | None = None
    "The default color of the *ClassMember*."

    def __init__(
        self,
        volume: int,
    ):
        self.volume: int = volume
        "The volume of the liquid."

    def __repr__(self):
        return f"<{self.__class__.__qualname__}: {self.volume}>"


__all__ = ("LiquidBase",)
