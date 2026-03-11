# language=rst
"""
Submodule for :class:`.LiquidEnum`.
"""

from collections import defaultdict
from lihzahrd.terraria.data.classenumtype.class_enum_type_dict import ClassEnumTypeDict


class LiquidEnum(ClassEnumTypeDict):
    """
    A :term:`ClassEnum` tracking the kinds of liquids existing in the world.
    """

    INDEXES = defaultdict(dict)


__all__ = ("LiquidEnum",)
