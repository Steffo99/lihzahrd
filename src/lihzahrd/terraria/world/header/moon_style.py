from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackByte


class MoonStyleEnum(IntEnum):
    """
    Possible moon styles.
    """

    WHITE = 0
    """
    White moon.

    .. image:: https://terraria.wiki.gg/images/Moon.png
    """

    YELLOW = 1
    """
    Yellow moon.

    .. image:: https://terraria.wiki.gg/images/Moon_style_1.png
    """

    RINGED = 2
    """
    Green ringed moon.

    .. image:: https://terraria.wiki.gg/images/Moon_style_2.png
    """

    MYTHRIL = 3
    """
    Mythil moon.

    .. image:: https://terraria.wiki.gg/images/Moon_style_3.png
    """

    BLUE = 4
    """
    Bright blue moon.

    .. image:: https://terraria.wiki.gg/images/Moon_style_4.png
    """

    GREEN = 5
    """
    Green moon.

    .. image:: https://terraria.wiki.gg/images/Moon_style_5.png
    """

    PINK = 6
    """
    Pink moon.

    .. image:: https://terraria.wiki.gg/images/Moon_style_6.png
    """

    ORANGE = 7
    """
    Orange moon.

    .. image:: https://terraria.wiki.gg/images/Moon_style_7.png
    """

    PURPLE = 8
    """
    Purple moon.

    .. image:: https://terraria.wiki.gg/images/Moon_style_8.png
    """


class MoonStyle(PackEnum[MoonStyleEnum, int], PackByte):
    """
    The style of the moon of a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = MoonStyleEnum


__all__ = (
    "MoonStyleEnum",
    "MoonStyle",
)
