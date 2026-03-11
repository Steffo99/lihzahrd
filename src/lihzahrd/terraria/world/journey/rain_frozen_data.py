# language=rst
"""
Submodule containing :class:`.RainFrozenData`.
"""

from dataclasses import dataclass

from lihzahrd.terraria.world.journey.journey_setting_data import JourneySettingData


@dataclass
class RainFrozenData(JourneySettingData):
    """
    Data about the Freeze Rain power.
    """

    frozen: bool
    "Whether rain is currently frozen and cannot change."

    @staticmethod
    def kind() -> int:
        return 9


__all__ = ("RainFrozenData",)
