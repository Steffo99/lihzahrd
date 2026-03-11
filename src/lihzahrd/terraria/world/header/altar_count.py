from logging import getLogger
from typing import Literal

from lihzahrd.terraria.utils.pack.primitive.int import PackInt
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class AltarCount(OpInteger[int], PackInt):
    """
    How many altars have been smashed in the world so far.
    """

    _LOG = getLogger(__name__)

    def next_ore_tier(self) -> Literal["cobalt_tier"] | Literal["mythril_tier"] | Literal["adamantite_tier"]:
        """
        :return: A string representing the ore tier that will be added to the world when an altar is broken.
        """
        tier = self.value % 3
        if tier == 0:
            return "cobalt_tier"
        elif tier == 1:
            return "mythril_tier"
        else:
            return "adamantite_tier"


__all__ = ("AltarCount",)
