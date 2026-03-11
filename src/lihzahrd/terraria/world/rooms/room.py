from logging import getLogger
from typing import Any

from lihzahrd.terraria.data.classenums.npc_enum import NPCEnum
from lihzahrd.terraria.data.classmembers.npc_base import NPCBase
from lihzahrd.terraria.utils.file_processor import FileProcessor

from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.utils.structures.coordinates import Coordinates
from lihzahrd.terraria.world.rooms.room_data import RoomData


class Room(PackPrimitive[RoomData]):
    """
    :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` to process a room assigned to an NPC in a Terraria world.
    """

    _LOG = getLogger(__name__)

    @classmethod
    def _validate(cls, value: RoomData, **kwargs: Any) -> None:
        pass

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> RoomData:
        kind = fp.read_int()
        npc_class: type[NPCBase] = NPCEnum.INDEXES["ID"][kind]

        return RoomData(
            npc=npc_class,
            position=Coordinates(
                x=fp.read_int(),
                y=fp.read_int(),
            ),
        )

    @classmethod
    def _write(cls, fp: FileProcessor, value: RoomData, **kwargs: Any) -> None:
        fp.write_int(value.npc.ID)
        fp.write_int(value.position.x)
        fp.write_int(value.position.y)
