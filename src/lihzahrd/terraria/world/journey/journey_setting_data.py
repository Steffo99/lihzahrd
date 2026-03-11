# language=rst
"""
Submodule containing :class:`.JourneySettingData`.
"""

from abc import ABCMeta, abstractmethod


class JourneySettingData(metaclass=ABCMeta):
    """
    Base class for Journey setting data.

    .. todo::

        Like with :attr:`lihzahrd.terraria.world.tile_entities.tile_entity_data.TileEntityData.extra`, a better, more extensible way to implement this would be via a :term:`ClassEnum` and inheritance, as that would allow new kinds of journey settings to be registered without having to edit :mod:`lihzahrd`.
    """

    @staticmethod
    @abstractmethod
    def kind() -> int:
        """
        :return: The ID of the associated Journey setting.
        """


__all__ = ("JourneySettingData",)
