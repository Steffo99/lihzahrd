# language=rst
"""
Submodule for :class:`.NPCEnum`.
"""

from collections import defaultdict
from logging import getLogger

from lihzahrd.terraria.data.classenumtype.class_enum_type_dict import ClassEnumTypeDict


class NPCEnum(ClassEnumTypeDict):
    """
    A :term:`ClassEnum` tracking the kinds of NPCs existing in the world.
    """

    INDEXES = defaultdict(dict)


__all__ = ("NPCEnum",)
