# language=rst
"""
Submodule for :class:`.OpInteger`.
"""

from abc import ABCMeta
from typing import Self

from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean
from lihzahrd.terraria.utils.pack.primitive.op.number import OpNumber
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class OpInteger[Value](OpNumber[Value], OpBoolean[Value], metaclass=ABCMeta):
    """
    Extension of both :class:`~lihzahrd.terraria.utils.pack.primitive.op.number.OpNumber` and :class:`~lihzahrd.terraria.utils.pack.primitive.op.boolean.OpBoolean` which adds integer operators based on :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`.
    """

    def __int__(self) -> int:
        return int(self.value)

    def __index__(self) -> int:
        return int(self)

    def __floordiv__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value // other.value)
        else:
            return self.__class__(self.value // other)

    def __ifloordiv__(self, other) -> None:
        if isinstance(other, PackPrimitive):
            self.value //= other.value
        else:
            self.value //= other

    def __mod__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value % other.value)
        else:
            return self.__class__(self.value % other)

    def __imod__(self, other) -> None:
        if isinstance(other, PackPrimitive):
            self.value %= other.value
        else:
            self.value %= other

    def __lshift__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value << other.value)
        else:
            return self.__class__(self.value << other)

    def __ilshift__(self, other) -> None:
        if isinstance(other, PackPrimitive):
            self.value <<= other.value
        else:
            self.value <<= other

    def __rshift__(self, other) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value >> other.value)
        else:
            return self.__class__(self.value >> other)

    def __irshift__(self, other) -> None:
        if isinstance(other, PackPrimitive):
            self.value >>= other.value
        else:
            self.value >>= other


__all__ = ("OpInteger",)
