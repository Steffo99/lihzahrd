from logging import getLogger
from typing import Any, override

from lihzahrd.terraria.utils.pack.primitive.op.collection import OpCollection
from lihzahrd.terraria.utils.pack.primitive.str import PackStrVariable


class WorldName(OpCollection[str], PackStrVariable):
    """
    The name of a Terraria world.
    """

    _LOG = getLogger(__name__)

    class NameTooLongError(PackStrVariable.ValidationError):
        """
        The name of the world surpasses in length the maximum length that the Terraria game client allows to enter.
        """

    VALUE_LEN_MAX = 27
    "Maximum length of the world name."

    @classmethod
    @override
    def _validate(cls, value: str, **kwargs: Any) -> None:
        super()._validate(value, **kwargs)

        if not len(value) <= cls.VALUE_LEN_MAX:
            raise cls.NameTooLongError(value)


__all__ = ("WorldName",)
