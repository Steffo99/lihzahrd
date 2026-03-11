# language=rst
"""
Submodule containing :class:`.WindFrozenData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.world.journey.journey_setting_data import JourneySettingData


@dataclass
class WindFrozenData(JourneySettingData):
    """
    Data about the Freeze Wind power.
    """

    frozen: bool
    "Whether wind is currently frozen and cannot change."

    @staticmethod
    def kind() -> int:
        return 10


__all__ = ("WindFrozenData",)
