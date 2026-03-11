from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool
from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean


class LanternNightCelebrationScheduled(OpBoolean[bool], PackBool):
    """
    Whether a celebratory (boss defeated) *Lantern Night* will start at the next night.
    """

    _LOG = getLogger(__name__)


__all__ = ("LanternNightCelebrationScheduled",)
