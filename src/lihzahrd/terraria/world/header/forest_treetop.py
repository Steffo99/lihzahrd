from enum import IntEnum
from logging import getLogger

from lihzahrd.terraria.utils.pack.primitive.enumeration import PackEnum
from lihzahrd.terraria.utils.pack.primitive.int import PackInt


class ForestTreetopEnum(IntEnum):
    """
    Possible treetops for the forest biome.
    """

    TREE_0 = 0
    """
    .. image:: https://terraria.wiki.gg/images/Treetop_Forest_1.png
    """

    TREE_1 = 1
    """
    .. image:: https://terraria.wiki.gg/images/Treetop_Forest_Alt1_1.png
    """

    TREE_2 = 2
    """
    .. image:: https://terraria.wiki.gg/images/Treetop_Forest_Alt2_1.png
    """

    TREE_3 = 3
    """
    .. image:: https://terraria.wiki.gg/images/Treetop_Forest_Alt3_1.png
    """

    TREE_4 = 4
    """
    .. image:: https://terraria.wiki.gg/images/Treetop_Forest_Alt4_1.png
    """

    TREE_5 = 5
    """
    .. image:: https://terraria.wiki.gg/images/Treetop_Forest_Alt5_1.png
    """


class ForestTreetop(PackEnum[ForestTreetopEnum, int], PackInt):
    """
    The style of the forest trees in a segment of a Terraria world.
    """

    _LOG = getLogger(__name__)

    ENUM = ForestTreetopEnum


__all__ = (
    "ForestTreetopEnum",
    "ForestTreetop",
)
