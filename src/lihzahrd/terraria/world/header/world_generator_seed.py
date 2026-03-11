from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.op.collection import OpCollection
from lihzahrd.terraria.utils.pack.primitive.str import PackStrVariable


class WorldGeneratorSeed(OpCollection[str], PackStrVariable):
    """
    The seed used to randomize the generator used to generate a Terraria world.
    """

    _LOG = getLogger(__name__)


__all__ = ("WorldGeneratorSeed",)
