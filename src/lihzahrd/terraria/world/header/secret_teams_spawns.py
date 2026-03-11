from logging import getLogger
from typing import Any, override

from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.utils.structures.coordinates import Coordinates


class SecretTeamsSpawns(PackPrimitive[list[Coordinates]]):
    """
    Spawn points of the various teams in a Teams secret seed.
    """

    _LOG = getLogger(__name__)

    def __repr__(self):
        if len(self.value) == 0:
            return f"<{self.__class__.__qualname__}: not set>"
        elif len(self.value) == self.EXPECTED_LENGTH:
            return f"<{self.__class__.__qualname__}: READY!>"
        else:
            return f"<{self.__class__.__qualname__}: unknown>"

    @property
    def white(self) -> Coordinates | None:
        if len(self.value) == 0:
            return None
        else:
            return self.value[0]

    @property
    def red(self) -> Coordinates | None:
        if len(self.value) == 0:
            return None
        else:
            return self.value[1]

    @property
    def green(self) -> Coordinates | None:
        if len(self.value) == 0:
            return None
        else:
            return self.value[2]

    @property
    def blue(self) -> Coordinates | None:
        if len(self.value) == 0:
            return None
        else:
            return self.value[3]

    @property
    def yellow(self) -> Coordinates | None:
        if len(self.value) == 0:
            return None
        else:
            return self.value[4]

    @property
    def purple(self) -> Coordinates | None:
        if len(self.value) == 0:
            return None
        else:
            return self.value[5]

    def set(
        self,
        white: Coordinates,
        red: Coordinates,
        green: Coordinates,
        blue: Coordinates,
        yellow: Coordinates,
        purple: Coordinates,
    ) -> None:
        self.value = [white, red, green, blue, yellow, purple]

    def clear(self):
        self.value = None

    class UnknownListLengthError(PackPrimitive[list[Coordinates]].ValidationError):
        """
        The list contains more items than how many there usually are in a Terraria version.
        """

    class OverflowError(PackPrimitive[list[Coordinates]].ValidationError):
        """
        At least one item in the list is out of representable range.
        """

    EXPECTED_LENGTH = 6

    @classmethod
    @override
    def _validate(cls, value: list[Coordinates], **kwargs: Any) -> None:
        length = len(value)
        if length != 0 and length != cls.EXPECTED_LENGTH:
            raise cls.UnknownListLengthError(value)
        for item in value:
            if not FileProcessor.SHORT_MIN <= item.x <= FileProcessor.SHORT_MAX:
                raise cls.OverflowError(value)
            if not FileProcessor.SHORT_MIN <= item.y <= FileProcessor.SHORT_MAX:
                raise cls.OverflowError(value)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> list[Coordinates]:
        length = fp.read_byte()
        spawns: list[Coordinates] = []
        for _ in range(length):
            x = fp.read_short()
            y = fp.read_short()
            spawn = Coordinates(x=x, y=y)
            spawns.append(spawn)
        return spawns

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: list[Coordinates], **kwargs: Any) -> None:
        length = len(value)
        fp.write_byte(length)
        for item in value:
            fp.write_short(item.x)
            fp.write_short(item.y)
