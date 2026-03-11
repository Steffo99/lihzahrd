# language=rst
"""
Submodule containing :class:`.TimeFrozenData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.world.journey.journey_setting_data import JourneySettingData


@dataclass
class TimeFrozenData(JourneySettingData):
    """
    Data about the Freeze Time power.
    """

    frozen: bool
    "Whether time is currently frozen and cannot advance."

    @staticmethod
    def kind() -> int:
        return 0


__all__ = ("TimeFrozenData",)
