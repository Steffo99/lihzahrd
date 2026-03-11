from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool
from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean


class WorldMode(OpBoolean[bool], PackBool):
    """
    The current mode of a Terraria world.

    Is it in Hardmode yet?
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        if self.value:
            return f"<{self.__class__.__qualname__}: HARDMODE>"
        else:
            return f"<{self.__class__.__qualname__}: pre-hardmode>"

    def is_prehardmode(self) -> bool:
        """
        :return: Whether the world has yet to enter hardmode.
        """
        return not self.value

    def is_hardmode(self) -> bool:
        """
        :return: Whether the world has entered hardmode.
        """
        return self.value

    def set_to_prehardmode(self) -> None:
        """
        Set the world to pre-hardmode.
        """
        self.value = False

    def set_to_hardmode(self) -> None:
        """
        Set the world to hardmode.
        """
        self.value = True


__all__ = ("WorldMode",)
