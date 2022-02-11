from .invasion import Invasion
from .rain import Rain
from .party import Party
from .sandstorm import Sandstorm
from .lunarevents import LunarEvents
from .lanternnight import LanternNight


class Events:
    """Information about the ongoing world events."""

    def __init__(
        self,
        blood_moon: bool,
        solar_eclipse: bool,
        invasion: Invasion,
        slime_rain: float,
        rain: Rain,
        party: Party,
        sandstorm: Sandstorm,
        lunar_events: LunarEvents,
        lantern_night: LanternNight,
    ):
        self.blood_moon: bool = blood_moon
        """If the current moon is a Blood Moon."""

        self.solar_eclipse: bool = solar_eclipse
        """If the current day is a Solar Eclipse."""

        self.invasion: Invasion = invasion
        """Information about the currently ongoing invasion."""

        self.slime_rain: float = slime_rain
        """How long the slime rain will go on for."""

        self.rain: Rain = rain
        """Information about the currently ongoing rain."""

        self.party: Party = party
        """Information about the currently ongoing party."""

        self.sandstorm: Sandstorm = sandstorm
        """Information about the currently ongoing sandstorm."""

        self.lunar_events: LunarEvents = lunar_events
        """Information about the currently ongoing Lunar Events."""

        self.lantern_night: LanternNight = lantern_night
        """Information about the currently ongoing lantern night."""

    def __repr__(self):
        return f"<WorldEvents>"
