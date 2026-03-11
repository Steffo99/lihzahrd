# language=rst
"""
Submodule for :class:`.PrefixBase`.
"""

from logging import getLogger

from lihzahrd.terraria.data.classenums.prefix_enum import PrefixEnum

log = getLogger(__name__)


class PrefixBase(metaclass=PrefixEnum, register=False):
    """
    The prefix.

    All prefixes inherit from this one; it's a :term:`ClassMemberBase` for members of :class:`.PrefixEnum`.

    It:

    - annotates the mandatory attributes that all prefixes should have.

    :raises NotImplementedError: If attempted to instantiate.
    """

    __slots__ = ()

    ID: int
    "The ID of the prefix."

    NAME: str
    "The prefix."

    def __init__(self):
        raise NotImplementedError("PrefixBase forbids instantiation")


__all__ = ("PrefixBase",)
