from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool
from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean


class MeteoriteScheduled(OpBoolean[bool], PackBool):
    """
    Whether a meteorite is scheduled to land at the next midnight.
    """

    _LOG = getLogger(__name__)


__all__ = ("MeteoriteScheduled",)
