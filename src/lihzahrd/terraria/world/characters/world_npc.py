from logging import getLogger
from typing import Any

from lihzahrd.terraria.data.classenums.npc_enum import NPCEnum
from lihzahrd.terraria.data.classmembers.npc_base import NPCBase
from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.utils.structures.coordinates import Coordinates


class WorldNPC(PackPrimitive[NPCBase]):
    """
    :class:`lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` to process a NPC stores in a Terraria world.
    """

    _LOG = getLogger(__name__)

    class MissingVariationIndexError(PackPrimitive[NPCBase].ValidationError):
        """
        :attr:`NPCData.is_town_npc` is set, but :attr:`NPCData.variation_index` isn't.
        """

    @classmethod
    def _validate(cls, value: NPCBase, **kwargs: Any) -> None:
        if value.is_town_npc:
            if value.variation_index is None:
                raise cls.MissingVariationIndexError(value)

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> NPCBase:
        kind = fp.read_int()
        name = fp.read_string_variable()
        position = Coordinates(x=fp.read_float(), y=fp.read_float())
        is_homeless = fp.read_bool()
        home = Coordinates(x=fp.read_int(), y=fp.read_int())

        (
            is_town_npc,
            flag_1,
            flag_2,
            flag_3,
            flag_4,
            flag_5,
            flag_6,
            flag_7,
        ) = fp.read_bits()

        variation_index = fp.read_int() if is_town_npc else None
        homeless_despawn = fp.read_bool()

        npc_class = NPCEnum.INDEXES["ID"][kind]

        return npc_class(
            name=name,
            position=position,
            is_homeless=is_homeless,
            home=home,
            is_town_npc=is_town_npc,
            flag_1=flag_1,
            flag_2=flag_2,
            flag_3=flag_3,
            flag_4=flag_4,
            flag_5=flag_5,
            flag_6=flag_6,
            flag_7=flag_7,
            variation_index=variation_index,
            homeless_despawn=homeless_despawn,
        )

    @classmethod
    def _write(cls, fp: FileProcessor, value: NPCBase, **kwargs: Any) -> None:
        fp.write_int(value.ID)
        fp.write_string_variable(value.name)
        fp.write_float(value.position.x)
        fp.write_float(value.position.y)
        fp.write_bool(value.is_homeless)
        fp.write_int(value.home.x)
        fp.write_int(value.home.y)
        fp.write_bits(
            (
                value.is_town_npc,
                value.flag_1,
                value.flag_2,
                value.flag_3,
                value.flag_4,
                value.flag_5,
                value.flag_6,
                value.flag_7,
            )
        )
        if value.is_town_npc:
            fp.write_int(value.variation_index)
        fp.write_bool(value.homeless_despawn)


__all__ = ("WorldNPC",)
