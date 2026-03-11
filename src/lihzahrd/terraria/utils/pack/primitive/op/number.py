# language=rst
"""
Submodule for :class:`.OpNumber`.
"""

from abc import ABCMeta
from typing import Self

from lihzahrd.terraria.utils.pack.primitive.op.comparison import OpComparison
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class OpNumber[Value](OpComparison[Value], metaclass=ABCMeta):
    """
    Extension of :class:`~lihzahrd.terraria.utils.pack.primitive.op.comparison.OpComparison` which adds number operators based on :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`.

    .. note::

        :meth:`~object.__pow__` and :meth:`~object.__ipow__` are not implemented due to ambiguity regarding how to handle the ``modulo`` parameter.
    """

    def __neg__(self) -> Self:
        return self.__class__(-self.value)

    def __pos__(self) -> Self:
        return self.__class__(+self.value)

    def __abs__(self) -> Self:
        return self.__class__(abs(self.value))

    def __add__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value + other.value)
        else:
            return self.__class__(self.value + other)

    def __iadd__(self, other) -> None:
        if isinstance(other, PackPrimitive):
            self.value += other.value
        else:
            self.value += other

    def __sub__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value - other.value)
        else:
            return self.__class__(self.value - other)

    def __isub__(self, other) -> None:
        if isinstance(other, PackPrimitive):
            self.value -= other.value
        else:
            self.value -= other

    def __mul__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value * other.value)
        else:
            return self.__class__(self.value * other)

    def __imul__(self, other) -> None:
        if isinstance(other, PackPrimitive):
            self.value *= other.value
        else:
            self.value *= other

    def __truediv__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value / other.value)
        else:
            return self.__class__(self.value / other)

    def __itruediv__(self, other) -> None:
        if isinstance(other, PackPrimitive):
            self.value /= other.value
        else:
            self.value /= other
