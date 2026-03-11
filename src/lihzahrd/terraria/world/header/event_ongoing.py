from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool
from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean


class EventOngoing(OpBoolean[bool], PackBool):
    """
    A flag denoting whether an event is currently ongoing in the world or not.
    """

    _LOG = getLogger(__name__)


__all__ = ("EventOngoing",)
