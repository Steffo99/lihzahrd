# language=rst
"""
Submodule containing :class:`.TimeScaleData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.world.journey.journey_setting_data import JourneySettingData


@dataclass
class TimeScaleData(JourneySettingData):
    """
    Data about the timescale setting.
    """

    scale: float
    "The speed at which time is currently flowing (``1.0``-``24.0``)."

    @staticmethod
    def kind() -> int:
        return 8


__all__ = ("TimeScaleData",)
