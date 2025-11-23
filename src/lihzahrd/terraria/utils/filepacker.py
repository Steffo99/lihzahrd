import logging
import struct
import uuid
from typing import Any

from .rect import Rect

log = logging.getLogger(__name__)


class FilePacker:
    """Helper class for serializing and deserializing a Terraria world file."""

    __slots__ = ("data", "cursor")

    def __init__(self, data: bytearray):
        self.data: bytearray = data
        """The world data."""

        self.cursor = 0
        """The byte currently being edited."""

    def __repr__(self):
        length = len(self.data)
        return f"<FilePacker, size {length:08x}, cursor {self.cursor:08x}>"

    def __len__(self):
        return len(self.data)

    def read(self, structure: struct.Struct) -> Any:
        value = structure.unpack_from(self.data, self.cursor)
        self.cursor += structure.size
        return value

    def write(self, structure: struct.Struct, value: Any) -> None:
        structure.pack_into(self.data, self.cursor, value)
        self.cursor += self._boolean.size

    _boolean = struct.Struct("?")

    def read_boolean(self) -> bool:
        value = self.read(self._boolean)[0]
        log.info("%r: Read boolean %r", self, value)
        return value

    def write_boolean(self, value: bool) -> None:
        log.info("%r: Writing boolean %r", self, value)
        self.write(self._boolean, value)

    _uint1 = struct.Struct("B")

    def read_uint1(self) -> int:
        value = self.read(self._uint1)[0]
        log.info("%r: Read uint1 %r", self, value)
        return value

    def write_uint1(self, value: int) -> None:
        log.info("%r: Writing uint1 %r", self, value)
        self.write(self._uint1, value)

    BITS = {
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

    def read_bits(self) -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
        byte = self.read(self._uint1)[0]
        value = self.BITS[byte]
        log.info("%r: Read bits %r", self, value)
        return value

    def write_bits(self, value: tuple[bool, bool, bool, bool, bool, bool, bool, bool]) -> None:
        log.info("%r: Writing bits %r", self, value)
        byte = \
            value[0] * (1 << 0) + \
            value[1] * (1 << 1) + \
            value[2] * (1 << 2) + \
            value[3] * (1 << 3) + \
            value[4] * (1 << 4) + \
            value[5] * (1 << 5) + \
            value[6] * (1 << 6) + \
            value[7] * (1 << 7)
        self.write(self._uint1, byte)

    _int2 = struct.Struct("h")

    def read_int2(self) -> int:
        value = self.read(self._int2)[0]
        log.info("%r: Read int2 %r", self, value)
        return value

    def write_int2(self, value: int) -> None:
        log.info("%r: Writing int2 %r", self, value)
        self.write(self._int2, value)

    _uint2 = struct.Struct("H")

    def read_uint2(self) -> int:
        value = self.read(self._uint2)[0]
        log.info("%r: Read uint2 %r", self, value)
        return value

    def write_uint2(self, value: int) -> None:
        log.info("%r: Writing uint2 %r", self, value)
        self.write(self._uint2, value)

    _int4 = struct.Struct("i")

    def read_int4(self) -> int:
        value = self.read(self._int4)[0]
        log.info("%r: Read int4 %r", self, value)
        return value

    def write_int4(self, value: int) -> None:
        log.info("%r: Writing int4 %r", self, value)
        self.write(self._int4, value)

    _uint4 = struct.Struct("i")

    def read_uint4(self) -> int:
        value = self.read(self._uint4)[0]
        log.info("%r: Read uint4 %r", self, value)
        return value

    def write_uint4(self, value: int) -> None:
        log.info("%r: Writing uint4 %r", self, value)
        self.write(self._uint4, value)

    _int8 = struct.Struct("q")

    def read_int8(self) -> int:
        value = self.read(self._int8)[0]
        log.info("%r: Read int8 %r", self, value)
        return value

    def write_int8(self, value: int) -> None:
        log.info("%r: Writing int8 %r", self, value)
        self.write(self._int8, value)

    _uint8 = struct.Struct("Q")

    def read_uint8(self) -> int:
        value = self.read(self._uint8)[0]
        log.info("%r: Read uint8 %r", self, value)
        return value

    def write_uint8(self, value: int) -> None:
        log.info("%r: Writing uint8 %r", self, value)
        self.write(self._uint8, value)

    _fsingle = struct.Struct("f")

    def read_fsingle(self) -> float:
        value = self.read(self._fsingle)[0]
        log.info("%r: Read fsingle %r", self, value)
        return value

    def write_fsingle(self, value: float) -> None:
        log.info("%r: Writing fsingle %r", self, value)
        self.write(self._fsingle, value)

    _fdouble = struct.Struct("d")

    def read_fdouble(self) -> float:
        value = self.read(self._fdouble)[0]
        log.info("%r: Read fdouble %r", self, value)
        return value

    def write_fdouble(self, value: float) -> None:
        log.info("%r: Writing fdouble %r", self, value)
        self.write(self._fdouble, value)

    _rect = struct.Struct("iiii")

    def read_rect(self) -> Rect:
        value = Rect(*self.read(self._rect))
        log.info("%r: Read rect %r", self, value)
        return value

    def write_rect(self, value: Rect) -> None:
        log.info("%r: Writing rect %r", self, value)
        self.write(self._rect, value.to_tuple())

    def read_uleb128(self) -> int:
        times = 0
        value = 0
        more = True
        while more:
            byte = self.read_uint1()
            shifted_byte = (byte & 0b0111_1111) << (7 * times)
            times += 1
            value += shifted_byte
            more = bool(byte & 0b1000_0000)
        log.info("%r: Read uleb128 %r", self, value)
        return value

    def write_uleb128(self, value: int) -> None:
        log.info("%r: Writing uleb128 %r", self, value)
        more = True
        while more:
            byte = value & 0b0111_1111
            value -= 0b0111_1111
            more = value > 0
            if more:
                byte |= 0b1000_0000
            self.write_uint1(value)

    def _read_string_base(self, size: int) -> str:
        value = str(self.data[self.cursor:self.cursor + size], encoding="latin1")
        self.cursor += size
        return value

    def _write_string_base(self, value: bytes) -> None:
        self.data[self.cursor:self.cursor + len(value)] = value
        self.cursor += len(value)

    def read_string_fixed(self, size: int):
        value = self._read_string_base(size)
        log.info("%r: Read string_fixed %r", self, value)
        return value

    def write_string_fixed(self, value: str, expected_size: int) -> None:
        log.info("%r: Writing string_fixed %r", self, value)
        data = bytes(value, encoding="latin1")
        size = len(data)
        if size != expected_size:
            raise ValueError(f"expected value to be of size {expected_size}, was of size {size} instead")
        self._write_string_base(data)

    def read_string_variable(self) -> str:
        size = self.read_uleb128()
        value = self._read_string_base(size)
        log.info("%r: Read string_variable %r", self, value)
        return value

    def write_string_variable(self, value: str) -> None:
        log.info("%r: Writing string_variable %r", self, value)
        data = bytes(value, encoding="latin1")
        size = len(data)
        self.write_uleb128(size)
        self._write_string_base(data)

    def read_uuid(self) -> uuid.UUID:
        data = self.data[self.cursor:self.cursor + 16]
        value = uuid.UUID(bytes=bytes(data))
        self.cursor += 16
        log.info("%r: Read uuid %r", self, value)
        return value

    def write_uuid(self, value: uuid.UUID) -> None:
        log.info("%r: Writing uuid %r", self, value)
        data = value.bytes
        self.data[self.cursor:self.cursor + 16] = data
        self.cursor += 16

    def read_datetime(self) -> bytearray:
        # TODO: convert to datetime
        # https://docs.microsoft.com/it-it/dotnet/api/system.datetime.kind?view=netframework-4.8#System_DateTime_Kind
        value = self.data[self.cursor:self.cursor + 8]
        self.cursor += 8
        log.info("%r: Read datetime %r", self, value)
        return value

    def write_datetime(self, value: bytearray) -> None:
        log.info("%r: Writing datetime %r", self, value)
        # TODO: convert from datetime
        self.data[self.cursor:self.cursor + 8] = value
        self.cursor += 8

    def read_bytearray(self, address: int = -1) -> bytearray:
        # TODO: remove this
        if address > self.cursor:
            raise ValueError("address is behind the current position of the cursor")
        value = self.data[self.cursor:address]
        self.cursor += len(value)
        log.info("%r: Read bytearray to address %r", self, value)
        return value

    def write_bytearray(self, value: bytearray) -> None:
        log.info("%r: Writing bytearray %r", self, value)
        length = len(value)
        self.data[self.cursor:self.cursor + length] = value


__all__ = (
    "FilePacker",
)
