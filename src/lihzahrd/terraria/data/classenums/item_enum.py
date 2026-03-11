# language=rst
"""
Submodule for :class:`.ItemEnum`.
"""

from collections import defaultdict
from logging import getLogger

from lihzahrd.terraria.data.classenumtype.class_enum_type_dict import ClassEnumTypeDict


class ItemEnum(ClassEnumTypeDict):
    """
    A :term:`ClassEnum` tracking the kinds of items existing in inventories.
    """

    INDEXES = defaultdict(dict)


__all__ = ("ItemEnum",)
