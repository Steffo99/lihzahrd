# language=rst
"""
Submodule containing :class:`.JourneyDifficultyData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.world.journey.journey_setting_data import JourneySettingData


@dataclass
class JourneyDifficultyData(JourneySettingData):
    """
    Data about the Journey mode difficulty setting.
    """

    multiplier: float
    "The difficulty multiplier."

    @staticmethod
    def kind() -> int:
        return 12


__all__ = ("JourneyDifficultyData",)
