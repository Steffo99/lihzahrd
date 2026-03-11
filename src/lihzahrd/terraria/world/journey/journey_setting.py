# language=rst
"""
Submodule containing :class:`.JourneySetting`.
"""

from logging import getLogger
from typing import Any

from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.world.journey.journey_difficulty_data import JourneyDifficultyData
from lihzahrd.terraria.world.journey.journey_setting_data import JourneySettingData
from lihzahrd.terraria.world.journey.rain_frozen_data import RainFrozenData
from lihzahrd.terraria.world.journey.spread_frozen_data import SpreadFrozenData
from lihzahrd.terraria.world.journey.time_frozen_data import TimeFrozenData
from lihzahrd.terraria.world.journey.time_scale_data import TimeScaleData
from lihzahrd.terraria.world.journey.wind_frozen_data import WindFrozenData


class JourneySetting(PackPrimitive[JourneySettingData]):
    """
    :class:`lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` processing a single Journey Mode setting.
    """

    _LOG = getLogger(__name__)

    class ReadUnknownJourneySettingError(PackPrimitive[JourneySettingData].ReadError):
        """
        The tile entity could not be read because its kind is unknown.

        If this happens, there's no way to determine how the journey setting should be read, and so no way to determine which data belongs to it and which to a different one, so reading cannot continue.
        """

        __slots__ = ("kind",)

        def __init__(self, kind: int):
            self.kind: int = kind
            "The ID of the unknown Journey setting."

    class WriteUnknownJourneySettingError(PackPrimitive[JourneySettingData].WriteError):
        """
        The tile entity could not be written because its kind is unknown.

        If this happens, there's no way to determine how the journey setting should be written, and so no way to determine which data belongs to it and which to a different one, so reading cannot continue.
        """

        __slots__ = ("data",)

        def __init__(self, data: JourneySettingData):
            self.data: JourneySettingData = data
            "The data of the unknown Journey setting."

    @classmethod
    def _validate(cls, value: JourneySettingData, **kwargs: Any) -> None:
        pass

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> JourneySettingData:
        kind = fp.read_short()
        match kind:
            case 0:
                return TimeFrozenData(frozen=fp.read_bool())
            case 8:
                return TimeScaleData(scale=fp.read_float())
            case 9:
                return RainFrozenData(frozen=fp.read_bool())
            case 10:
                return WindFrozenData(frozen=fp.read_bool())
            case 12:
                return JourneyDifficultyData(multiplier=fp.read_float())
            case 13:
                return SpreadFrozenData(frozen=fp.read_bool())
            case _:
                cls._LOG.error("Unknown journey setting: %r", kind)
                raise cls.ReadUnknownJourneySettingError(kind=kind)

    @classmethod
    def _write(cls, fp: FileProcessor, value: JourneySettingData, **kwargs: Any) -> None:
        fp.write_short(value.kind())
        match value:
            case TimeFrozenData(frozen):
                fp.write_bool(frozen)
            case TimeScaleData(scale):
                fp.write_float(scale)
            case RainFrozenData(frozen):
                fp.write_bool(frozen)
            case WindFrozenData(frozen):
                fp.write_bool(frozen)
            case JourneyDifficultyData(multiplier):
                fp.write_float(multiplier)
            case SpreadFrozenData(frozen):
                fp.write_bool(frozen)
            case _:
                cls._LOG.error("Unknown journey setting: %r", value)
                raise WriteUnknownJourneySettingError(value)


__all__ = ("JourneySetting",)
