from logging import getLogger
from typing import override

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool


class Daytime(PackBool):
    """
    Whether it is daytime or nighttime in a Terraria world.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        if self.is_day():
            return f"<{self.__class__.__qualname__}: day>"
        else:
            return f"<{self.__class__.__qualname__}: night>"

    def is_day(self) -> bool:
        return self.value

    def is_night(self) -> bool:
        return not self.value

    def set_day(self):
        self.value = True

    def set_night(self):
        self.value = False


__all__ = ("Daytime",)
