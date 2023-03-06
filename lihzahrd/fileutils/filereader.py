import typing
import struct
import uuid
import datetime
from .rect import Rect


INT_TO_BITS_CACHE = {
    i: (
        bool(i & 0b0000_0001),
        bool(i & 0b0000_0010),
        bool(i & 0b0000_0100),
        bool(i & 0b0000_1000),
        bool(i & 0b0001_0000),
        bool(i & 0b0010_0000),
        bool(i & 0b0100_0000),
        bool(i & 0b1000_0000)
    )
    for i in range(256)
}


class FileReader:
    """Helper class for deserializing a Terraria world file."""

    __slots__ = ("file",)

    def __init__(self, file: typing.IO):
        self.file: typing.IO = file

    _bool = struct.Struct("?").unpack

    def bool(self) -> bool:
        return self._bool(self.file.read(1))[0]

    _int1 = struct.Struct("B").unpack

    def int1(self) -> int:
        return self._int1(self.file.read(1))[0]

    def uint1(self) -> int:
        return self._int1(self.file.read(1))[0]

    _int2 = struct.Struct("h").unpack

    def int2(self) -> int:
        return self._int2(self.file.read(2))[0]

    _uint2 = struct.Struct("H").unpack

    def uint2(self) -> int:
        return self._uint2(self.file.read(2))[0]

    _int4 = struct.Struct("i").unpack

    def int4(self) -> int:
        return self._int4(self.file.read(4))[0]

    _uint4 = struct.Struct("i").unpack

    def uint4(self) -> int:
        return self._uint4(self.file.read(4))[0]

    _int8 = struct.Struct("q").unpack

    def int8(self) -> int:
        return self._int8(self.file.read(8))[0]

    _uint8 = struct.Struct("Q").unpack

    def uint8(self) -> int:
        return self._uint8(self.file.read(8))[0]

    _single = struct.Struct("f").unpack

    def single(self) -> float:
        return self._single(self.file.read(4))[0]

    _double = struct.Struct("d").unpack

    def double(self) -> float:
        return self._double(self.file.read(8))[0]

    def bits(self) -> typing.Tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
        data = self._int1(self.file.read(1))[0]
        return INT_TO_BITS_CACHE[data]

    _rect = struct.Struct("iiii").unpack

    def rect(self) -> Rect:
        left, right, top, bottom = self._rect(self.file.read(16))
        return Rect(left, right, top, bottom)

    def uleb128(self) -> int:
        times = 0
        value = 0
        more = True
        while more:
            byte = self.uint1()
            shifted_byte = (byte & 0b0111_1111) << (7 * times)
            times += 1
            value += shifted_byte
            more = bool(byte & 0b1000_0000)
        return value

    def string(self, size=None) -> str:
        if size is None:
            size = self.uleb128()
        return str(self.file.read(size), encoding="latin1")

    def uuid(self) -> uuid.UUID:
        # TODO: convert to uuid
        # https://docs.microsoft.com/en-us/dotnet/api/system.guid.tobytearray?view=netframework-4.8
        uuid_bytes = self.file.read(16)
        return uuid_bytes

    def datetime(self) -> datetime.datetime:
        # TODO: convert to datetime
        # https://docs.microsoft.com/it-it/dotnet/api/system.datetime.kind?view=netframework-4.8#System_DateTime_Kind
        datetime_bytes = self.file.read(8)
        return datetime_bytes

    def read_until(self, address: int) -> bytearray:
        data = bytearray()
        if self.file.tell() > address:
            raise ValueError("Can't read backwards")
        while self.file.tell() < address:
            data += self.file.read(1)
        return data

    def skip_until(self, address: int) -> None:
        self.file.seek(address)

    def __repr__(self):
        return f"<FileReader at {hex(self.file.tell())}>"
