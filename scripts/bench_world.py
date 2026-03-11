from io import BytesIO
from timeit import timeit

from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.world.world import PackWorld


def main():
    file = open("tests/lihzahrd/terraria/world/Restful_Heart.wld", "rb")
    packer_read = FileProcessor(file)
    result_read = PackWorld.read(packer_read, strict=True)
    world = result_read.instance
    stream = BytesIO()
    packer_write = FileProcessor(stream)
    result_write = world.write(packer_write, strict=True)


if __name__ == "__main__":
    NUMBER = 1
    time = timeit(stmt="main()", globals=globals(), number=NUMBER)
    print(time / NUMBER)
