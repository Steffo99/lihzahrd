from logging import getLogger
from typing import override, Any

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive


class Treetops(PackPrimitive[list[int]]):
    _LOG = getLogger(__name__)

    @property
    def forest_a(self) -> int:
        """
        Treetop value of forest area A.
        """
        return self.value[0]

    @forest_a.setter
    def forest_a(self, value: int):
        self.value[0] = value

    @property
    def forest_b(self) -> int:
        """
        Treetop value of forest area B.
        """
        return self.value[1]

    @forest_b.setter
    def forest_b(self, value: int):
        self.value[1] = value

    @property
    def forest_c(self) -> int:
        """
        Treetop value of forest area C.
        """
        return self.value[2]

    @forest_c.setter
    def forest_c(self, value: int):
        self.value[2] = value

    @property
    def forest_d(self) -> int:
        """
        Treetop value of forest area D.
        """
        return self.value[3]

    @forest_d.setter
    def forest_d(self, value: int):
        self.value[3] = value

    @property
    def corruption(self) -> int:
        """
        Treetop value of the corruption biome.
        """
        return self.value[4]

    @corruption.setter
    def corruption(self, value: int):
        self.value[4] = value

    @property
    def jungle(self) -> int:
        """
        Treetop value of the jungle biome.
        """
        return self.value[5]

    @jungle.setter
    def jungle(self, value: int):
        self.value[5] = value

    @property
    def snow(self) -> int:
        """
        Treetop value of the snow biome.
        """
        return self.value[6]

    @snow.setter
    def snow(self, value: int):
        self.value[6] = value

    @property
    def hallow(self) -> int:
        """
        Treetop value of the hallow biome.
        """
        return self.value[7]

    @hallow.setter
    def hallow(self, value: int):
        self.value[7] = value

    @property
    def crimson(self) -> int:
        """
        Treetop value of the crimson biome.
        """
        return self.value[8]

    @crimson.setter
    def crimson(self, value: int):
        self.value[8] = value

    @property
    def desert(self) -> int:
        """
        Treetop value of the desert biome.
        """
        return self.value[9]

    @desert.setter
    def desert(self, value: int):
        self.value[9] = value

    @property
    def ocean(self) -> int:
        """
        Treetop value of the ocean biome.
        """
        return self.value[10]

    @ocean.setter
    def ocean(self, value: int):
        self.value[10] = value

    @property
    def mushroom(self) -> int:
        """
        Treetop value of the corruption biome.
        """
        return self.value[11]

    @mushroom.setter
    def mushroom(self, value: int):
        self.value[11] = value

    @property
    def hell(self) -> int:
        """
        Treetop value of the hell biome.
        """
        return self.value[12]

    @hell.setter
    def hell(self, value: int):
        self.value[12] = value

    class UnknownListLengthError(PackPrimitive[list[int]].ValidationError):
        """
        The list contains more items than how many there usually are in a Terraria version.
        """

    class OverflowError(PackPrimitive[list[int]].ValidationError):
        """
        At least one item in the list is out of representable range.
        """

    EXPECTED_LENGTH = 13
    "The expected amount of items in :attr:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive.value`."

    @classmethod
    @override
    def _validate(cls, value: list[int], **kwargs: Any) -> None:
        length = len(value)
        if length != cls.EXPECTED_LENGTH:
            raise cls.UnknownListLengthError(value)
        for item in value:
            if not FileProcessor.INT_MIN <= item <= FileProcessor.INT_MAX:
                raise cls.OverflowError(value)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> list[int]:
        length = fp.read_int()
        variants: list[int] = []
        for _ in range(length):
            variant = fp.read_int()
            variants.append(variant)
        return variants

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: list[int], **kwargs: Any) -> None:
        length = len(value)
        fp.write_int(length)
        for item in value:
            fp.write_int(item)


__all__ = ("Treetops",)
