# language=rst
"""
Submodule containing :class:`.JourneySettingsCollection`.
"""

from logging import getLogger

from lihzahrd.terraria.utils.pack.composite.flag_array import PackFlagArray
from lihzahrd.terraria.world.journey.journey_setting import JourneySetting


class JourneySettingsCollection(PackFlagArray[JourneySetting]):
    """
    :class:`~lihzahrd.terraria.utils.pack.composite.flag_array.PackFlagArray` which groups each possible Journey Mode setting.
    """

    _LOG = getLogger(__name__)

    ITEM = JourneySetting


__all__ = ["JourneySettingsCollection"]
