import logging
from pathlib import Path

from bs4 import BeautifulSoup

from lihzahrd._generate.terraria.tiles_generator import TilesGenerator

MODULE_ROOT: Path = Path(__file__).parent
PACKAGE_ROOT: Path = MODULE_ROOT.parent.parent

DATA_PATH: Path = MODULE_ROOT / "data.xml"

CODE_PATH = PACKAGE_ROOT / "terraria" / "data" / "classmembers"
TILES_CODE = CODE_PATH / "blocks.py"
ITEMS_CODE = CODE_PATH / "items.py"
NPCS_CODE = CODE_PATH / "npcs.py"
PREFIXES_CODE = CODE_PATH / "prefixes.py"
WALLS_CODE = CODE_PATH / "walls.py"


def main():
    logging.basicConfig(level=30, format="%(asctime)s | %(name)56s | %(levelname)8s | %(message)s")
    with open(DATA_PATH) as file:
        soup = BeautifulSoup(file, features="lxml-xml")
        generator = TilesGenerator(soup=soup)
        with open(TILES_CODE, mode="w") as code:
            tiles = generator.generate_blocks()
            code.write(tiles)
        with open(WALLS_CODE, mode="w") as code:
            items = generator.generate_walls()
            code.write(items)
        with open(NPCS_CODE, mode="w") as code:
            items = generator.generate_npcs()
            code.write(items)
        with open(PREFIXES_CODE, mode="w") as code:
            items = generator.generate_prefixes()
            code.write(items)
        with open(ITEMS_CODE, mode="w") as code:
            items = generator.generate_items()
            code.write(items)


if __name__ == "__main__":
    main()
