# language=rst
"""
Submodule for low level Terraria save file operations, and in particular, the :class:`.FileProcessor` class.
"""

import logging
import struct
import uuid
from datetime import datetime, timedelta, timezone
from typing import BinaryIO, Any, Literal, Iterable

from lihzahrd.terraria.utils.structures.rectangle import Rectangle

log = logging.getLogger(__name__)


class FileProcessor:
    """
    Helper class for reading and writing C# data structures to Terraria save files.
    """

    __slots__ = ("stream",)

    def __init__(self, stream: BinaryIO):
        self.stream: BinaryIO = stream
        """The binary stream (:class:`~typing.BinaryIO`) to operate on."""

    def __repr__(self) -> str:
        stream = self.stream
        return f"{self.__class__.__qualname__}({stream=})"

    def read(self, structure: struct.Struct) -> Any:
        """
        Read the given structure from :attr:`.stream`.

        :param structure: The structure to read.
        :return: The value of the read structure (will probably be a :class:`tuple`).
        """
        data = self.stream.read(structure.size)
        value = structure.unpack(data)
        return value

    def write(self, structure: struct.Struct, value: Iterable[Any]) -> None:
        """
        Write the given structure from :attr:`.stream`.

        :param structure: The structure to write.
        :param value: The value of the structure.
        """
        data = structure.pack(*value)
        self.stream.write(data)

    BOOL: struct.Struct = struct.Struct("?")
    "A serialized C# ``bool``."

    def read_bool(self) -> bool:
        """
        Read a :attr:`.BOOL` from :attr:`.stream`.

        :return: The read value, as a :class:`bool`.
        """
        value = self.read(self.BOOL)[0]
        log.debug("Read bool: %r", value)
        return value

    def write_bool(self, value: bool) -> None:
        """
        Write a :attr:`.BOOL` to :attr:`.stream`.

        :param value: The value to write, as a :class:`bool`.
        """

        log.debug("Writing bool: %r", value)
        self.write(self.BOOL, (value,))

    SBYTE: struct.Struct = struct.Struct("b")
    "A serialized C# ``sbyte``."

    SBYTE_MIN: Literal[-128] = -(2 ** (8 - 1))
    "The minimum value that a :attr:`.SBYTE` can have."

    SBYTE_MAX: Literal[127] = 2 ** (8 - 1) - 1
    "The maximum value that a :attr:`.SBYTE` can have."

    def read_sbyte(self) -> int:
        """
        Read a :attr:`.SBYTE` from :attr:`.stream`.

        :return: The read value, as a :class:`int`.
        """
        value = self.read(self.SBYTE)[0]
        log.debug("Read SBYTE: %r", value)
        return value

    def write_sbyte(self, value: int) -> None:
        """
        Write a :attr:`.SBYTE` to :attr:`.stream`.

        :param value: The value to write, as a :class:`int`.
        """
        log.debug("Writing SBYTE: %r", value)
        self.write(self.SBYTE, (value,))

    BYTE: struct.Struct = struct.Struct("B")
    "A serialized C# ``byte``."

    BYTE_MIN: Literal[0] = 0
    "The minimum value that a :attr:`.BYTE` can have."

    BYTE_MAX: Literal[255] = 2**8 - 1
    "The maximum value that a :attr:`.BYTE` can have."

    def read_byte(self) -> int:
        """
        Read a :attr:`.BYTE` from :attr:`.stream`.

        :return: The read value, as a :class:`int`.
        """
        value = self.read(self.BYTE)[0]
        log.debug("Read BYTE: %r", value)
        return value

    def write_byte(self, value: int) -> None:
        """
        Write a :attr:`.BYTE` to :attr:`.stream`.

        :param value: The value to write, as a :class:`int`.
        """
        log.debug("Writing BYTE: %r", value)
        self.write(self.BYTE, (value,))

    INT_TO_BITS: dict[int, tuple[bool, bool, bool, bool, bool, bool, bool, bool]] = {
        i: (
            bool(i & 0b0000_0001),
            bool(i & 0b0000_0010),
            bool(i & 0b0000_0100),
            bool(i & 0b0000_1000),
            bool(i & 0b0001_0000),
            bool(i & 0b0010_0000),
            bool(i & 0b0100_0000),
            bool(i & 0b1000_0000),
        )
        for i in range(256)
    }
    """
    Cache associating each :class:`int` between 0 and 255 to a :class:`tuple` of 8 :class:`bool` elements of its bits in little-endian order.
    
    .. admonition:: Example
    
        .. code-block:: python
        
            >>> FileProcessor.INT_TO_BITS[0]
            (False, False, False, False, False, False, False, False)
            >>> FileProcessor.INT_TO_BITS[1]
            (True, False, False, False, False, False, False, False)
            >>> FileProcessor.INT_TO_BITS[128]
            (False, False, False, False, False, False, False, True)
    
    .. note::
    
        This is necessary to speed up bits processing, which would otherwise take a long time.
    
    :meta hide-value:
    """

    def read_bits(self) -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
        """
        Read a :attr:`.BYTE` from :attr:`.stream`, then get its :attr:`.INT_TO_BITS`.

        :return: The read bits, as a :class:`tuple` of :class:`bool`.
        """
        byte = self.read(self.BYTE)[0]
        value = self.INT_TO_BITS[byte]
        log.debug("Read bits: %r", value)
        return value

    def write_bits(self, value: tuple[bool, bool, bool, bool, bool, bool, bool, bool]) -> None:
        """
        Convert a series of :attr:`.INT_TO_BITS` to a :attr:`.BYTE`, then write it to :attr:`.stream`.

        :param value: The bits to write, as a :class:`tuple` of :class:`bool`.
        """
        log.debug("Writing bits: %r", value)
        byte = (
            value[0] * (1 << 0)
            + value[1] * (1 << 1)
            + value[2] * (1 << 2)
            + value[3] * (1 << 3)
            + value[4] * (1 << 4)
            + value[5] * (1 << 5)
            + value[6] * (1 << 6)
            + value[7] * (1 << 7)
        )
        self.write(self.BYTE, (byte,))

    SHORT: struct.Struct = struct.Struct("h")
    "A serialized C# ``short``."

    SHORT_MIN: Literal[-32_768] = -(2 ** (16 - 1))
    "The minimum value that a :attr:`.SHORT` can have."

    SHORT_MAX: Literal[32_767] = 2 ** (16 - 1) - 1
    "The maximum value that a :attr:`.SHORT` can have."

    def read_short(self) -> int:
        """
        Read a :attr:`.SHORT` from :attr:`.stream`.

        :return: The read value, as a :class:`int`.
        """
        value = self.read(self.SHORT)[0]
        log.debug("Read i16: %r", value)
        return value

    def write_short(self, value: int) -> None:
        """
        Write a :attr:`.SHORT` to :attr:`.stream`.

        :param value: The value to write, as a :class:`int`.
        """
        log.debug("Writing i16: %r", value)
        self.write(self.SHORT, (value,))

    USHORT: struct.Struct = struct.Struct("H")
    "A serialized C# ``ushort``."

    USHORT_MIN: Literal[0] = 0
    "The minimum value that a :attr:`.USHORT` can have."

    USHORT_MAX: Literal[65_535] = 2**16 - 1
    "The maximum value that a :attr:`.USHORT` can have."

    def read_ushort(self) -> int:
        """
        Read a :attr:`.USHORT` from :attr:`.stream`.

        :return: The read value, as a :class:`int`.
        """
        value = self.read(self.USHORT)[0]
        log.debug("Read USHORT: %r", value)
        return value

    def write_ushort(self, value: int) -> None:
        """
        Write a :attr:`.USHORT` to :attr:`.stream`.

        :param value: The value to write, as a :class:`int`.
        """
        log.debug("Writing USHORT: %r", value)
        self.write(self.USHORT, (value,))

    INT: struct.Struct = struct.Struct("i")
    "A serialized C# ``int``."

    INT_MIN: Literal[-2_147_483_648] = -(2 ** (32 - 1))
    "The minimum value that a :attr:`.INT` can have."

    INT_MAX: Literal[2_147_483_647] = 2 ** (32 - 1) - 1
    "The maximum value that a :attr:`.INT` can have."

    def read_int(self) -> int:
        """
        Read a :attr:`.INT` from :attr:`.stream`.

        :return: The read value, as a :class:`int`.
        """
        value = self.read(self.INT)[0]
        log.debug("Read INT: %r", value)
        return value

    def write_int(self, value: int) -> None:
        """
        Write a :attr:`.INT` to :attr:`.stream`.

        :param value: The value to write, as a :class:`int`.
        """
        log.debug("Writing INT: %r", value)
        self.write(self.INT, (value,))

    UINT: struct.Struct = struct.Struct("i")
    "A serialized C# ``uint``."

    UINT_MIN: Literal[0] = 0
    "The minimum value that a :attr:`.UINT` can have."

    UINT_MAX: Literal[4_294_967_295] = 2**32 - 1
    "The maximum value that a :attr:`.UINT` can have."

    def read_uint(self) -> int:
        """
        Read a :attr:`.UINT` from :attr:`.stream`.

        :return: The read value, as a :class:`int`.
        """
        value = self.read(self.UINT)[0]
        log.debug("Read UINT: %r", value)
        return value

    def write_uint(self, value: int) -> None:
        """
        Write a :attr:`.UINT` to :attr:`.stream`.

        :param value: The value to write, as a :class:`int`.
        """
        log.debug("Writing UINT: %r", value)
        self.write(self.UINT, (value,))

    LONG: struct.Struct = struct.Struct("q")
    "A serialized C# ``long``."

    LONG_MIN: Literal[-9_223_372_036_854_775_808] = -(2 ** (64 - 1))
    "The minimum value that a :attr:`.LONG` can have."

    LONG_MAX: Literal[9_223_372_036_854_775_807] = 2 ** (64 - 1) - 1
    "The maximum value that a :attr:`.LONG` can have."

    def read_long(self) -> int:
        """
        Read a :attr:`.LONG` from :attr:`.stream`.

        :return: The read value, as a :class:`int`.
        """
        value = self.read(self.LONG)[0]
        log.debug("Read LONG: %r", value)
        return value

    def write_long(self, value: int) -> None:
        """
        Write a :attr:`.LONG` to :attr:`.stream`.

        :param value: The value to write, as a :class:`int`.
        """
        log.debug("Writing LONG: %r", value)
        self.write(self.LONG, (value,))

    ULONG: struct.Struct = struct.Struct("Q")
    "A serialized C# ``ulong``."

    ULONG_MIN: Literal[0] = 0
    "The minimum value that a :attr:`.ULONG` can have."

    ULONG_MAX: Literal[18_446_744_073_709_551_615] = 2**64 - 1
    "The maximum value that a :attr:`.ULONG` can have."

    def read_ulong(self) -> int:
        """
        Read a :attr:`.ULONG` from :attr:`.stream`.

        :return: The read value, as a :class:`int`.
        """
        value = self.read(self.ULONG)[0]
        log.debug("Read ULONG: %r", value)
        return value

    def write_ulong(self, value: int) -> None:
        """
        Write a :attr:`.ULONG` to :attr:`.stream`.

        :param value: The value to write, as a :class:`int`.
        """
        log.debug("Writing ULONG: %r", value)
        self.write(self.ULONG, (value,))

    FLOAT: struct.Struct = struct.Struct("f")
    "A serialized C# ``float``."

    def read_float(self) -> float:
        """
        Read a :attr:`.FLOAT` from :attr:`.stream`.

        :return: The read value, as a :class:`float`.
        """
        value = self.read(self.FLOAT)[0]
        log.debug("Read FLOAT: %r", value)
        return value

    def write_float(self, value: float) -> None:
        """
        Write a :attr:`.FLOAT` to :attr:`.stream`.

        :param value: The value to write, as a :class:`float`.
        """
        log.debug("Writing FLOAT: %r", value)
        self.write(self.FLOAT, (value,))

    DOUBLE: struct.Struct = struct.Struct("d")
    "A serialized C# ``double``."

    def read_double(self) -> float:
        """
        Read a :attr:`.DOUBLE` from :attr:`.stream`.

        .. note::

            Since Python's :class:`float` is 64-bit, no data is lost in the conversion.

        :return: The read value, as a :class:`float`.
        """
        value = self.read(self.DOUBLE)[0]
        log.debug("Read DOUBLE: %r", value)
        return value

    def write_double(self, value: float) -> None:
        """
        Write a :attr:`.DOUBLE` to :attr:`.stream`.

        :param value: The value to write, as a :class:`float`.
        """
        log.debug("Writing DOUBLE: %r", value)
        self.write(self.DOUBLE, (value,))

    RECT = struct.Struct("iiii")
    "A :class:`~lihzahrd.terraria.utils.structures.Rectangle` of :attr:`.INT`."

    def read_rect(self) -> Rectangle[int]:
        """
        Read a :attr:`.RECT` from :attr:`.stream`.

        :return: The read value, as a :class:`~lihzahrd.terraria.utils.structures.rectangle.Rectangle` of :class:`int`.
        """
        value = Rectangle(*self.read(self.RECT))
        log.debug("Read rect: %r", value)
        return value

    def write_rect(self, value: Rectangle[int]) -> None:
        """
        Write a :attr:`.RECT` to :attr:`.stream`.

        :param value: The value to write, as a :class:`~lihzahrd.terraria.utils.structures.rectangle.Rectangle` of :class:`int`.
        """
        log.debug("Writing rect: %r", value)
        self.write(self.RECT, tuple(value))

    def read_uleb128(self) -> int:
        """
        Read a `ULEB128`_ from :attr:`.stream`.

        :return: The read value, as a :class:`int`.

        .. _ULEB128: https://en.wikipedia.org/wiki/LEB128#Unsigned_LEB128
        """
        times = 0
        value = 0
        more = True
        while more:
            byte = self.read_byte()
            shifted_byte = (byte & 0b0111_1111) << (7 * times)
            times += 1
            value += shifted_byte
            more = bool(byte & 0b1000_0000)
        log.debug("Read uleb128: %r", value)
        return value

    def write_uleb128(self, value: int) -> None:
        """
        Write a `ULEB128`_ to :attr:`.stream`.

        :param value: The value to write, as a :class:`int`.

        .. _ULEB128: https://en.wikipedia.org/wiki/LEB128#Unsigned_LEB128
        """
        log.debug("Writing uleb128: %r", value)
        if value == 0:
            self.write_byte(0)
        else:
            while value > 0:
                byte = value & 0b0111_1111
                value >>= 7
                if value > 0:
                    byte |= 0b1000_0000
                self.write_byte(byte)

    def read_bytes_count(self, count: int) -> bytes:
        """
        Read a fixed number of bytes from :attr:`.stream`.

        :param count: The number of bytes to read.
        :return: The read :class:`bytes`.
        """
        value = self.stream.read(count)
        log.debug("Read %r bytes: %r", count, value)
        return value

    def read_bytes_until(self, address: int | None) -> bytes:
        """
        Read bytes from :attr:`.stream` until the given address.

        :param address: The address to read bytes until.
        :return: The read :class:`bytes`.
        """
        cursor = self.stream.tell()
        if address is None:
            value = self.stream.read()
        else:
            size = address - cursor
            if size < 0:
                log.warning("Resulting size is negative, attempting to self-correct by assuming that it is 0.")
                size = 0
            value = self.stream.read(size)
        log.debug("Read bytes until address %r: %r", address, value)
        return value

    def write_bytes(self, value: bytes) -> None:
        """
        Write some :class:`bytes` to :attr:`.stream`.

        :param value: The :class:`bytes` to write.
        """
        log.debug("Writing bytes: %r", value)
        self.stream.write(value)

    def read_string_raw(self, count: int) -> str:
        """
        Read a fixed number of bytes into a ``latin1`` string.

        :param count: The number of bytes to read.
        :return: The read bytes, as a :class:`str` with ``latin1`` encoding.
        """
        value = self.read_bytes_count(count)
        return str(value, encoding="latin1")

    def write_string_raw(self, value: str) -> None:
        """
        Write a :class:`str` to :attr:`.stream`.

        .. warning::

            This does not write the size of the string!

        :param value: The :class:`str` to write.
        """
        log.debug("Writing string: %r", value)
        value = bytes(value, encoding="latin1")
        self.write_bytes(value)

    def read_string_variable(self) -> str:
        """
        Read a :class:`str` of variable length from :attr:`.stream`:

        #. First, :meth:`.read_uleb128` is called to determine the size of the string in bytes.
        #. Then, :meth:`.read_string_raw` is called to read the actual string.

        :return: The read :class:`str`.
        """
        size = self.read_uleb128()
        value = self.read_string_raw(size)
        log.debug("Read string_variable: %r", value)
        return value

    def write_string_variable(self, value: str) -> None:
        """
        Write a :class:`str` of variable length to :attr:`.stream`:

        #. First, the string is converted to :class:`bytes` using the ``latin1`` encoding.
        #. Then, the size of the string in bytes is written with :meth:`.write_uleb128`.
        #. Finally, the :class:`bytes` are written with :meth:`.write_bytes`.

        :param value: The :class:`str` to write.
        """

        log.debug("Writing string_variable: %r", value)
        data = bytes(value, encoding="latin1")
        self.write_uleb128(len(data))
        self.write_bytes(data)

    def read_uuid(self) -> uuid.UUID:
        """
        Read 16 bytes from :attr:`.stream`, and consider them an :class:`~uuid.UUID`.

        :return: The read :class:`~uuid.UUID`.
        """
        value = uuid.UUID(bytes=self.stream.read(16))
        log.debug("Read uuid: %r", value)
        return value

    def write_uuid(self, value: uuid.UUID) -> None:
        """
        Write the 16 bytes corresponding to the given :class:`~uuid.UUID` to :attr:`.stream`.

        :param value: The :class:`~uuid.UUID` to write.
        """

        log.debug("Writing uuid: %r", value)
        self.stream.write(value.bytes)

    def read_datetime(self) -> datetime:
        """
        Read a :attr:`.ULONG` from :attr:`.stream`, then convert it to a :class:`~datetime.datetime`, following the same algorithm C# uses.

        :return: The read :class:`~datetime.datetime`.

        .. seealso::

            - `System.DateTimeKind in the C# docs <https://learn.microsoft.com/en-us/dotnet/api/system.datetimekind>`_
            - `DateTime.FromBinary in the C# source <https://source.dot.net/#System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/DateTime.cs,1206>`_

        .. warning::

            Some precision might be lost due to how :class:`~datetime.timedelta` objects work in Python.

        """
        data = self.read_ulong()

        kind = data & 0xC000000000000000 >> 62

        # C# docs say from the beginning of the century, but it's actually from year 1 for some reason?
        match kind:
            case 0:
                log.debug("Datetime is of unspecified kind, assuming local")
                value = datetime(year=1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            case 1:
                log.debug("Datetime is UTC")
                value = datetime(year=1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc)
            case 2:
                log.debug("Datetime is local")
                value = datetime(year=1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            case _:
                raise ValueError("expected datetime kind to be 0, 1, or 2, was instead: ", kind)

        ticks = data & 0x3FFFFFFFFFFFFFFF

        seconds = ticks // 10_000_000
        microseconds = (ticks - (seconds * 10_000_000)) / 10

        value += timedelta(seconds=seconds, microseconds=microseconds)

        log.debug("Read datetime: %r", value)
        return value

    def write_datetime(self, value: datetime) -> None:
        """
        Convert the given :class:`~datetime.datetime` to a :attr:`.ULONG` using the same algorithm C# uses, then write it to :attr:`.stream`.

        :param value: The :class:`~datetime.datetime` to write.
        """
        log.debug("Writing datetime: %r", value)

        kind = 1 if value.tzinfo else 0

        base = datetime(
            year=1,
            month=1,
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
            tzinfo=value.tzinfo,
        )
        delta = value - base

        ticks = delta.microseconds * 10 + delta.seconds * 10_000_000 + delta.days * 864_000_000_000

        # Just make sure we do not overflow to flags
        ticks &= 0x3FFFFFFFFFFFFFFF

        # Set the kind if necessary
        ticks |= kind << 62

        self.write(self.ULONG, (ticks,))


__all__ = ("FileProcessor",)
