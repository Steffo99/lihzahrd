from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool
from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean


class TimedialRunning(OpBoolean[bool], PackBool):
    """
    Whether the *Sundial* or *Moondial* is running or not.
    """

    _LOG = getLogger(__name__)


__all__ = ("TimedialRunning",)
