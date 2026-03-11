import logging
import random
import sys
import uuid
from datetime import datetime

from lihzahrd.terraria.data.classmembers.blocks import Wood
from lihzahrd.terraria.data.classmembers.walls import WoodWall
from lihzahrd.terraria.data.enums.paint import PaintEnum
from lihzahrd.terraria.world.tiles.tile import Tile
from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.world.world import PackWorld

logging.basicConfig(level=20, format="%(asctime)s | %(name)56s | %(levelname)8s | %(message)s", stream=sys.stderr)


def main():
    with open("tests/lihzahrd/terraria/world/Honey_of_Privacy.wld", "rb") as stream:
        packer = FileProcessor(stream)
        result = PackWorld.read(packer, strict=True)
        world = result.instance

    world.header.name.value = "The Garas"
    world.footer.name.value = world.header.name.value
    world.header.uuid.value = uuid.uuid4()
    world.header.id.value = random.randrange(FileProcessor.INT_MIN, FileProcessor.INT_MAX + 1)
    world.footer.id.value = world.header.id.value
    world.header.created_on.value = datetime.fromisoformat("1900-01-01T00:00:00+00:00")

    world.tiles[:, :] = Tile()
    world.tiles[:, 300:301] = Tile(
        block=Wood(paint=PaintEnum.SKY_BLUE, is_illuminant=True),
    )
    world.tiles[:, 301:1200] = Tile(
        block=Wood(paint=PaintEnum.SKY_BLUE, is_illuminant=True),
        wall=WoodWall(paint=PaintEnum.SKY_BLUE),
    )

    with open("The_Garas.wld", "wb") as stream:
        packer = FileProcessor(stream)
        world.write(packer, strict=False)


if __name__ == "__main__":
    main()
