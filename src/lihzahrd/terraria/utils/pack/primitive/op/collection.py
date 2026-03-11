# language=rst
"""
Submodule for :class:`.OpCollection`.
"""

import operator
from abc import ABCMeta
from typing import Iterator, Any

from lihzahrd.terraria.utils.pack.primitive.op.equality import OpEquality


class OpCollection[Value](OpEquality[Value], metaclass=ABCMeta):
    """
    Extension of :class:`~lihzahrd.terraria.utils.pack.primitive.op.equality.OpEquality` which adds collection operators based on :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`.
    """

    def __len__(self) -> int:
        return len(self.value)

    def __length_hint__(self) -> int:
        return operator.length_hint(self.value)

    def __getitem__(self, item) -> Any:
        return self.value.__getitem__(item)

    def __setitem__(self, key, value) -> None:
        self.value.__setitem__(key, value)

    def __delitem__(self, key) -> None:
        self.value.__delitem__(key)

    def __iter__(self) -> Iterator[Any]:
        return iter(self.value)

    def __reversed__(self) -> Iterator[Any]:
        return reversed(self.value)

    def __contains__(self, item) -> bool:
        return item in self.value
