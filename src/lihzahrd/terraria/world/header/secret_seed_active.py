from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.bool import PackBool
from lihzahrd.terraria.utils.pack.primitive.op.boolean import OpBoolean


class SecretSeedActive(OpBoolean[bool], PackBool):
    """
    A flag denoting whether a world is running a secret world seed.
    """

    _LOG = getLogger(__name__)


__all__ = ("SecretSeedActive",)
