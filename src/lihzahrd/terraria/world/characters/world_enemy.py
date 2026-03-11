from typing import Any

from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.utils.structures.coordinates import Coordinates
from lihzahrd.terraria.world.characters.world_enemy_data import WorldEnemyData


class WorldEnemy(PackPrimitive[WorldEnemyData]):
    """
    :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` to process a single persisted enemy in a Terraria world.

    .. tip::

        Enemies are usually persisted when they hold the player's dropped coins in Expert difficulty!

    """

    @classmethod
    def _validate(cls, value: WorldEnemyData, **kwargs: Any) -> None:
        pass

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> WorldEnemyData:
        kind = fp.read_int()
        position = Coordinates(x=fp.read_float(), y=fp.read_float())
        return WorldEnemyData(kind=kind, position=position)

    @classmethod
    def _write(cls, fp: FileProcessor, value: WorldEnemyData, **kwargs: Any) -> None:
        fp.write_int(value.kind)
        fp.write_float(value.position.x)
        fp.write_float(value.position.y)


__all__ = ("WorldEnemy",)
