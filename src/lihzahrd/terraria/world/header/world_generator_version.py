from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.int import PackULong
from lihzahrd.terraria.utils.pack.primitive.op.integer import OpInteger


class WorldGeneratorVersion(OpInteger[int], PackULong):
    """
    The version of the generator used to generate a Terraria world.
    """

    _LOG = getLogger(__name__)


__all__ = ("WorldGeneratorVersion",)
