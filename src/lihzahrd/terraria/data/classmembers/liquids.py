# language=rst
"""
Module for :term:`ClassMember` of :class:`~lihzahrd.terraria.data.classenums.liquid_enum.LiquidEnum`.
"""

from lihzahrd.terraria.data.classenums.liquid_enum import LiquidEnum


class Water(metaclass=LiquidEnum, ID=1):
    """
    `Water`_.

    .. _`Water`: https://terraria.wiki.gg/wiki/Water
    """


class Lava(metaclass=LiquidEnum, ID=2):
    """
    `Lava`_.

    .. _`Lava`: https://terraria.wiki.gg/wiki/Lava
    """


class Honey(metaclass=LiquidEnum, ID=3):
    """
    `Honey`_.

    .. _`Honey`: https://terraria.wiki.gg/wiki/Honey
    """


class Shimmer(metaclass=LiquidEnum, ID=4):
    """
    `Shimmer`_.

    .. _`Shimmer`: https://terraria.wiki.gg/wiki/Shimmer
    """


__all__ = (
    "Water",
    "Lava",
    "Honey",
    "Shimmer",
)
