# language=rst
"""
Submodule containing :class:`.TileEntityExtra`.
"""

from abc import ABCMeta, abstractmethod


class TileEntityExtra(metaclass=ABCMeta):
    """
    Base class for tile entity extra data.
    """

    @staticmethod
    @abstractmethod
    def tile_entity_kind() -> int:
        """
        :return: The kind id of the associated tile entity.
        """


__all__ = ("TileEntityExtra",)
