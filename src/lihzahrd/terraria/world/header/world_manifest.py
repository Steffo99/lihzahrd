from json import dumps, loads
from logging import getLogger
from typing import override, Any

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.str import PackStrVariable


class WorldManifest(PackStrVariable):
    """
    Unknown. Contains JSON.
    """

    _LOG = getLogger(__name__)

    @override
    def __repr__(self):
        return f"<{self.__class__.__qualname__}>"

    def get_json(self) -> Any:
        """
        :return: The Python :class:`object` resulting from parsing :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`.
        """
        return loads(self.value)

    def set_from_json(self, value: Any) -> None:
        """
        :param value: The Python :class:`object` to use as value. Must be JSON-able.
        """
        self.value = dumps(value)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs) -> str:
        return fp.read_string_variable()

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: str, **kwargs: Any) -> None:
        fp.write_string_variable(value)


__all__ = ("WorldManifest",)
