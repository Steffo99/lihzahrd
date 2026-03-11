from logging import getLogger

from lihzahrd.terraria.world.header.event_ongoing import EventOngoing


class LanternNightSpontaneousActive(EventOngoing):
    """
    Whether a (spontaneous) *Lantern Night* is ongoing or not.
    """

    _LOG = getLogger(__name__)


__all__ = ("LanternNightSpontaneousActive",)
