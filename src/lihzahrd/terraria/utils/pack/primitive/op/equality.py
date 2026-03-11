# language=rst
"""
Submodule for :class:`.OpEquality`.
"""

from abc import ABCMeta
from typing import Self

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class OpEquality[Value](PackPrimitive[Value], metaclass=ABCMeta):
    """
    Extension of :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` which adds equality operators based on :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`.
    """

    def __eq__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.value == other.value
        else:
            return self.value == other

    def __ne__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.value != other.value
        else:
            return self.value != other


__all__ = ("OpEquality",)
