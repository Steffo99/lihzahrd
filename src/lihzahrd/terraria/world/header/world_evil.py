from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool


class WorldEvil(PackBool):
    """
    The primary evil present in a Terraria world.

    Either Corruption, or Crimson.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        if not self.value:
            return f"<{self.__class__.__qualname__}: Corruption>"
        else:
            return f"<{self.__class__.__qualname__}: Crimson>"

    def is_corruption(self) -> bool:
        """
        :return: Whether the world has Corruption as main evil.
        """
        return not self.value

    def is_crimson(self) -> bool:
        """
        :return: Whether the world has Crimson as main evil.
        """
        return self.value

    def set_to_corruption(self) -> None:
        """
        Set :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` to represent Corruption.
        """
        self.value = False

    def set_to_crimson(self) -> None:
        """
        Set :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value` to represent Crimson.
        """
        self.value = True


__all__ = ("WorldEvil",)
