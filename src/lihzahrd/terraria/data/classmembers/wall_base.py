# language=rst
"""
Submodule for :class:`.WallBase`.
"""

from logging import getLogger

from lihzahrd.terraria.utils.structures.color import ColorRGB

from lihzahrd.terraria.data.classenums.wall_enum import WallEnum
from lihzahrd.terraria.data.enums.paint import PaintEnum

log = getLogger(__name__)


class WallBase(metaclass=WallEnum, register=False):
    """
    The kind of Terraria wall.

    All walls inherit from this; it's a :term:`ClassMemberBase` for members of :class:`.WallEnum`.

    It:

    - annotates the mandatory attributes that all walls should have.

    :param paint: The paint that is applied to the wall, or :obj:`None` if no paint is applied.
    :param is_illuminant: Whether the wall has had Illuminant Coating applied to it and is therefore always full bright.
    :param is_echo: Whether the wall has had Echo Coating applied to it and is therefore invisible.
    """

    ID: int
    "The ID of the prefix."

    NAME: str
    "The prefix."

    COLOR: ColorRGB | None = None
    "The default color of the *ClassMember*."

    BLEND: int
    "Unknown."

    __slots__ = (
        "paint",
        "is_illuminant",
        "is_echo",
    )

    def __init__(
        self,
        paint: PaintEnum = None,
        is_illuminant: bool = False,
        is_echo: bool = False,
    ):
        self.paint: PaintEnum = paint
        "The paint covering the wall."

        self.is_illuminant: bool = is_illuminant
        "Whether the wall has had Illuminant Coating applied to it."

        self.is_echo: bool = is_echo
        "Whether the wall has had Echo Coating applied to it."

    def __repr__(self):
        return f"<{self.__class__.__qualname__}>"


__all__ = ("WallBase",)
