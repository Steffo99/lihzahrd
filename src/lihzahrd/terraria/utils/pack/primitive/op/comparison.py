# language=rst
"""
Submodule for :class:`.OpComparison`.
"""

from abc import ABCMeta
from typing import Self

from lihzahrd.terraria.utils.pack.primitive.op.equality import OpEquality
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class OpComparison[Value](OpEquality[Value], metaclass=ABCMeta):
    """
    Extension of :class:`~lihzahrd.terraria.utils.pack.primitive.op.equality.OpEquality` which adds comparison operators based on :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`.
    """

    def __gt__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.value > other.value
        else:
            return self.value > other

    def __ge__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.value >= other.value
        else:
            return self.value >= other

    def __lt__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.value < other.value
        else:
            return self.value < other

    def __le__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.value <= other.value
        else:
            return self.value <= other


__all__ = ("OpComparison",)
