from pathlib import Path

from lihzahrd.terraria.world import World

def test_deserialization():
    path = Path(__file__).parent / "The_Bugging_Zone.wld"
    world = World.create_from_file(str(path))
    print(f"{world!r}")
