# language=rst
"""
Submodule for :class:`.BlockEnum`.
"""

from collections import defaultdict
from logging import getLogger

from lihzahrd.terraria.data.classenumtype.class_enum_type_dict import ClassEnumTypeDict


class BlockEnum(ClassEnumTypeDict):
    """
    A :term:`ClassEnum` tracking the kinds of blocks existing in the world.
    """

    INDEXES = defaultdict(dict)


__all__ = ("BlockEnum",)
