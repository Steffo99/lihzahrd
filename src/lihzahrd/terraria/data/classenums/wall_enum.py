# language=rst
"""
Submodule for :class:`.WallEnum`.
"""

from collections import defaultdict
from lihzahrd.terraria.data.classenumtype.class_enum_type_dict import ClassEnumTypeDict


class WallEnum(ClassEnumTypeDict):
    """
    A :term:`ClassEnum` tracking the kinds of walls existing in the world.
    """

    INDEXES = defaultdict(dict)


__all__ = ("WallEnum",)
