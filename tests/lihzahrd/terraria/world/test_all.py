from logging import getLogger

from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.world.world import PackWorld

log = getLogger(__name__)


def test_rw(fp_wld_read: FileProcessor):
    tile_cache_path = f"{fp_wld_read.stream.name}.out.npy"
    new_world_path = f"{fp_wld_read.stream.name}.out.wld"

    result = PackWorld.read(fp_wld_read, strict=True)
    assert result.valid
    world = result.instance
    assert isinstance(world, PackWorld)

    with open(new_world_path, "wb") as stream:
        packer = FileProcessor(stream)
        result = world.write(packer, strict=True)
        assert result.valid
