from logging import getLogger

from lihzahrd.terraria.world.header.event_ongoing import EventOngoing


class LanternNightCelebrationActive(EventOngoing):
    """
    Whether a celebratory (boss defeated) *Lantern Night* is ongoing.
    """

    _LOG = getLogger(__name__)


__all__ = ("LanternNightCelebrationActive",)
