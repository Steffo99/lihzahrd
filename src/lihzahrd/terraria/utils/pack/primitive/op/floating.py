# language=rst
"""
Submodule for :class:`.OpFloating`.
"""

from abc import ABCMeta
from math import trunc, floor, ceil
from typing import Self

from lihzahrd.terraria.utils.pack.primitive.op.number import OpNumber


class OpFloating[Value](OpNumber[Value], metaclass=ABCMeta):
    """
    Extension of :class:`~lihzahrd.terraria.utils.pack.primitive.op.number.OpNumber` which adds floating-point operators based on :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`.
    """

    def __float__(self) -> float:
        return float(self.value)

    def __complex__(self) -> complex:
        return complex(real=self.value)

    def __round__(self, ndigits=None) -> Self:
        return self.__class__(round(self.value, ndigits=ndigits))

    def __trunc__(self) -> Self:
        return self.__class__(trunc(self.value))

    def __floor__(self) -> Self:
        return self.__class__(floor(self.value))

    def __ceil__(self) -> Self:
        return self.__class__(ceil(self.value))


__all__ = ("OpFloating",)
