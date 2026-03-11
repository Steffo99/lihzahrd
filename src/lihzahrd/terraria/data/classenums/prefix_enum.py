# language=rst
"""
Submodule for :class:`.PrefixEnum`.
"""

from collections import defaultdict

from lihzahrd.terraria.data.classenumtype.class_enum_type_dict import ClassEnumTypeDict


class PrefixEnum(ClassEnumTypeDict):
    """
    A :term:`ClassEnum` tracking the kinds of prefixes existing in items in inventories.
    """

    INDEXES = defaultdict(dict)


__all__ = ("PrefixEnum",)
