# language=rst
"""
Submodule containing :class:`.SpreadFrozenData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.world.journey.journey_setting_data import JourneySettingData


@dataclass
class SpreadFrozenData(JourneySettingData):
    """
    Data about the Freeze Infection Spread power.
    """

    frozen: bool
    "Whether infection is currently frozen and cannot happen."

    @staticmethod
    def kind() -> int:
        return 13


__all__ = ("SpreadFrozenData",)
