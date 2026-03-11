# language=rst
"""
Submodule for :class:`.OpBoolean`.
"""

from abc import ABCMeta
from typing import Self

from black import Any

from lihzahrd.terraria.utils.pack.primitive.op.equality import OpEquality
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class OpBoolean[Value](OpEquality[Value], metaclass=ABCMeta):
    """
    Extension of :class:`~lihzahrd.terraria.utils.pack.primitive.op.equality.OpEquality` which adds boolean operators based on :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`.
    """

    def __bool__(self) -> bool:
        return bool(self.value)

    def __and__(self, other: Any) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value & other.value)
        else:
            return self.__class__(self.value & other)

    def __iand__(self, other: Any) -> None:
        if isinstance(other, PackPrimitive):
            self.value &= other.value
        else:
            self.value &= other

    def __or__(self, other: Any) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value | other.value)
        else:
            return self.__class__(self.value | other)

    def __ior__(self, other: Any) -> None:
        if isinstance(other, PackPrimitive):
            self.value |= other.value
        else:
            self.value |= other

    def __xor__(self, other: Any) -> Self:
        if isinstance(other, PackPrimitive):
            return self.__class__(self.value ^ other.value)
        else:
            return self.__class__(self.value ^ other)

    def __ixor__(self, other: Any) -> None:
        if isinstance(other, PackPrimitive):
            self.value ^= other.value
        else:
            self.value ^= other

    def __invert__(self) -> Self:
        return self.__class__(not self.value)


__all__ = ("OpBoolean",)
