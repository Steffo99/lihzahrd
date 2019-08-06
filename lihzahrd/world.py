import math
import struct


class Rect:
    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def __repr__(self):
        return f"Rect(left={self.left}, right={self.right}, top={self.top}, bottom={self.bottom})"


class World:
    @classmethod
    def create_from_file(cls, f):
        version = cls.int4(f)
        relogic = cls.string(f, 7)
        filetype = cls.byte(f)
        revision = cls.uint4(f)
        favorite = cls.uint8(f) != 0
        pointers = [cls.int4(f) for _ in range(cls.int2(f))]
        tileframeimportant_size = math.ceil(cls.int2(f) / 8)
        tileframeimportant = [cls.bool(f) for _ in range(tileframeimportant_size)]
        worldname = cls.string(f)
        worldid = cls.int4(f)
        # Not working from here on
        bounds = cls.rect(f)
        worldsize = (cls.int4(f), cls.int4(f))
        ...

    @staticmethod
    def bit(f):
        data = f.read(1)
        return (data & 0b1000_0000,
                data & 0b0100_0000,
                data & 0b0010_0000,
                data & 0b0001_0000,
                data & 0b0000_1000,
                data & 0b0000_0100,
                data & 0b0000_0010,
                data & 0b0000_0001)

    @staticmethod
    def bool(f):
        return struct.unpack("?", f.read(1))[0]

    @staticmethod
    def byte(f):
        return struct.unpack("B", f.read(1))[0]

    @staticmethod
    def int2(f):
        return struct.unpack("h", f.read(2))[0]

    @staticmethod
    def int4(f):
        return struct.unpack("i", f.read(4))[0]

    @staticmethod
    def uint4(f):
        return struct.unpack("I", f.read(4))[0]

    @staticmethod
    def int8(f):
        return struct.unpack("q", f.read(8))[0]

    @staticmethod
    def uint8(f):
        return struct.unpack("Q", f.read(8))[0]

    @staticmethod
    def single(f):
        return struct.unpack("f", f.read(4))[0]

    @staticmethod
    def double(f):
        return struct.unpack("d", f.read(8))[0]

    @staticmethod
    def rect(f):
        left, right, top, bottom = struct.unpack("iiii", f.read(16))
        return Rect(left, right, top, bottom)

    @staticmethod
    def string(f, size=None):
        if size is None:
            size = World.byte(f)
        return str(f.read(size), encoding="latin1")


if __name__ == "__main__":
    with open("sampleworld.wld", "rb") as f:
        w = World.create_from_file(f)
