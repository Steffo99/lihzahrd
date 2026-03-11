# language=rst
"""
Submodule containing :class:`.TileEntity`.
"""

from logging import getLogger
from typing import Any

from lihzahrd.terraria.data.classenums.item_enum import ItemEnum
from lihzahrd.terraria.data.classmembers.item_base import ItemBase
from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.utils.structures.coordinates import Coordinates
from lihzahrd.terraria.world.tile_entities.dyed_stack_data import DyedStackData
from lihzahrd.terraria.world.tile_entities.food_plate_extra import FoodPlateExtra
from lihzahrd.terraria.world.tile_entities.hat_rack_extra import HatRackExtra
from lihzahrd.terraria.world.tile_entities.item_flask_extra import ItemFlaskExtra
from lihzahrd.terraria.world.tile_entities.item_frame_extra import ItemFrameExtra
from lihzahrd.terraria.world.tile_entities.kite_extra import KiteExtra
from lihzahrd.terraria.world.tile_entities.logic_sensor_extra import LogicSensorExtra
from lihzahrd.terraria.world.tile_entities.mannequin_extra import MannequinExtra
from lihzahrd.terraria.world.tile_entities.pylon_extra import PylonExtra
from lihzahrd.terraria.world.tile_entities.target_dummy_extra import TargetDummyExtra
from lihzahrd.terraria.world.tile_entities.tile_entity_data import TileEntityData
from lihzahrd.terraria.world.tile_entities.weapon_rack_extra import WeaponRackExtra


class TileEntity(PackPrimitive[TileEntityData]):
    """
    Data about a single tile entity (item frame, mannequin, etc.) placed in a Terraria world.
    """

    _LOG = getLogger(__name__)

    class UnknownTileEntityError(PackPrimitive[TileEntityData].ReadError):
        """
        The tile entity could not be processed because its kind is unknown.

        If this happens, there's no way to determine the shape that extras
        """

        __slots__ = ("kind",)

        def __init__(self, kind: int):
            self.kind: int = kind

    @classmethod
    def _validate(cls, value: TileEntityData, **kwargs: Any) -> None:
        pass

    @classmethod
    def _read_stack(cls, fp: FileProcessor) -> ItemBase:
        item_class = ItemEnum.INDEXES["ID"][fp.read_short()]
        return item_class(prefix=fp.read_byte(), quantity=fp.read_short())

    @classmethod
    def _read(cls, fp: FileProcessor, **kwargs: Any) -> TileEntityData:
        kind = fp.read_byte()
        id_ = fp.read_int()
        position = Coordinates(
            x=fp.read_short(),
            y=fp.read_short(),
        )
        match kind:
            case 0:
                extra = TargetDummyExtra(character_index=fp.read_short())
            case 1:
                extra = ItemFrameExtra(item=cls._read_stack(fp))
            case 2:
                extra = LogicSensorExtra(kind=fp.read_byte(), enabled=fp.read_bool())
            case 3:
                (
                    has_helmet,
                    has_shirt,
                    has_pants,
                    has_accessory_1,
                    has_accessory_2,
                    has_accessory_3,
                    has_accessory_4,
                    has_accessory_5,
                ) = fp.read_bits()
                (
                    dyed_helmet,
                    dyed_shirt,
                    dyed_pants,
                    dyed_accessory_1,
                    dyed_accessory_2,
                    dyed_accessory_3,
                    dyed_accessory_4,
                    dyed_accessory_5,
                ) = fp.read_bits()
                pose = fp.read_byte()
                (
                    has_weapon,
                    has_mount,
                    dyed_mount,
                    _,
                    _,
                    _,
                    _,
                    _,
                ) = fp.read_bits()
                extra = MannequinExtra(
                    pose=pose,
                    helmet=DyedStackData(
                        item=(cls._read_stack(fp) if has_helmet else None),
                        dye=(cls._read_stack(fp) if dyed_helmet else None),
                    ),
                    shirt=DyedStackData(
                        item=(cls._read_stack(fp) if has_shirt else None),
                        dye=(cls._read_stack(fp) if dyed_shirt else None),
                    ),
                    pants=DyedStackData(
                        item=(cls._read_stack(fp) if has_pants else None),
                        dye=(cls._read_stack(fp) if dyed_pants else None),
                    ),
                    accessory_1=DyedStackData(
                        item=(cls._read_stack(fp) if has_accessory_1 else None),
                        dye=(cls._read_stack(fp) if dyed_accessory_1 else None),
                    ),
                    accessory_2=DyedStackData(
                        item=(cls._read_stack(fp) if has_accessory_2 else None),
                        dye=(cls._read_stack(fp) if dyed_accessory_2 else None),
                    ),
                    accessory_3=DyedStackData(
                        item=(cls._read_stack(fp) if has_accessory_3 else None),
                        dye=(cls._read_stack(fp) if dyed_accessory_3 else None),
                    ),
                    accessory_4=DyedStackData(
                        item=(cls._read_stack(fp) if has_accessory_4 else None),
                        dye=(cls._read_stack(fp) if dyed_accessory_4 else None),
                    ),
                    accessory_5=DyedStackData(
                        item=(cls._read_stack(fp) if has_accessory_5 else None),
                        dye=(cls._read_stack(fp) if dyed_accessory_5 else None),
                    ),
                    mount=DyedStackData(
                        item=(cls._read_stack(fp) if has_mount else None),
                        dye=(cls._read_stack(fp) if dyed_mount else None),
                    ),
                    weapon=(cls._read_stack(fp) if has_weapon else None),
                )
            case 4:
                extra = WeaponRackExtra(item=cls._read_stack(fp))
            case 5:
                (
                    has_left,
                    has_right,
                    dyed_left,
                    dyed_right,
                    _,
                    _,
                    _,
                    _,
                ) = fp.read_bits()
                extra = HatRackExtra(
                    right=DyedStackData(
                        item=(cls._read_stack(fp) if has_right else None),
                        dye=(cls._read_stack(fp) if dyed_right else None),
                    ),
                    left=DyedStackData(
                        item=(cls._read_stack(fp) if has_left else None),
                        dye=(cls._read_stack(fp) if dyed_left else None),
                    ),
                )
            case 6:
                extra = FoodPlateExtra(item=cls._read_stack(fp))
            case 7:
                extra = PylonExtra()
            case 8:
                extra = ItemFlaskExtra(item=cls._read_stack(fp))
            case 9:
                extra = KiteExtra(kind=fp.read_short())
            case _:
                cls._LOG.error("Unknown tile entity: %r", kind)
                raise cls.UnknownTileEntityError(kind=kind)

        return TileEntityData(id=id_, position=position, extra=extra)

    @classmethod
    def _write_stack(cls, fp: FileProcessor, stack: ItemBase) -> None:
        fp.write_short(stack.ID)
        fp.write_byte(stack.prefix if stack.prefix is not None else 0)
        fp.write_short(stack.quantity)

    @classmethod
    def _write(cls, fp: FileProcessor, value: TileEntityData, **kwargs: Any) -> None:
        fp.write_byte(value.kind())
        fp.write_int(value.id)
        fp.write_short(value.position.x)
        fp.write_short(value.position.y)
        match value.extra:
            case TargetDummyExtra(character_index):
                fp.write_short(character_index)
            case ItemFrameExtra(item):
                cls._write_stack(fp, stack=item)
            case LogicSensorExtra(kind, enabled):
                fp.write_byte(kind)
                fp.write_bool(enabled)
            case MannequinExtra(
                pose,
                helmet,
                shirt,
                pants,
                accessory_1,
                accessory_2,
                accessory_3,
                accessory_4,
                accessory_5,
                mount,
                weapon,
            ):
                fp.write_bits(
                    (
                        helmet.item is not None,
                        shirt.item is not None,
                        pants.item is not None,
                        accessory_1.item is not None,
                        accessory_2.item is not None,
                        accessory_3.item is not None,
                        accessory_4.item is not None,
                        accessory_5.item is not None,
                    )
                )
                fp.write_bits(
                    (
                        helmet.dye is not None,
                        shirt.dye is not None,
                        pants.dye is not None,
                        accessory_1.dye is not None,
                        accessory_2.dye is not None,
                        accessory_3.dye is not None,
                        accessory_4.dye is not None,
                        accessory_5.dye is not None,
                    )
                )
                fp.write_byte(pose)
                fp.write_bits(
                    (
                        weapon is not None,
                        mount.item is not None,
                        mount.dye is not None,
                        False,
                        False,
                        False,
                        False,
                        False,
                    )
                )
                if helmet.item is not None:
                    cls._write_stack(fp, stack=helmet.item)
                if helmet.dye is not None:
                    cls._write_stack(fp, stack=helmet.dye)
                if shirt.item is not None:
                    cls._write_stack(fp, stack=shirt.item)
                if shirt.dye is not None:
                    cls._write_stack(fp, stack=shirt.dye)
                if pants.item is not None:
                    cls._write_stack(fp, stack=pants.item)
                if pants.dye is not None:
                    cls._write_stack(fp, stack=pants.dye)
                if accessory_1.item is not None:
                    cls._write_stack(fp, stack=accessory_1.item)
                if accessory_1.dye is not None:
                    cls._write_stack(fp, stack=accessory_1.dye)
                if accessory_2.item is not None:
                    cls._write_stack(fp, stack=accessory_2.item)
                if accessory_2.dye is not None:
                    cls._write_stack(fp, stack=accessory_2.dye)
                if accessory_3.item is not None:
                    cls._write_stack(fp, stack=accessory_3.item)
                if accessory_3.dye is not None:
                    cls._write_stack(fp, stack=accessory_3.dye)
                if accessory_4.item is not None:
                    cls._write_stack(fp, stack=accessory_4.item)
                if accessory_4.dye is not None:
                    cls._write_stack(fp, stack=accessory_4.dye)
                if accessory_5.item is not None:
                    cls._write_stack(fp, stack=accessory_5.item)
                if accessory_5.dye is not None:
                    cls._write_stack(fp, stack=accessory_5.dye)
                if mount.item is not None:
                    cls._write_stack(fp, stack=mount.item)
                if mount.dye is not None:
                    cls._write_stack(fp, stack=mount.dye)
                if weapon is not None:
                    cls._write_stack(fp, stack=weapon)
            case WeaponRackExtra(item):
                cls._write_stack(fp, stack=item)
            case HatRackExtra(left, right):
                fp.write_bits(
                    (
                        left.item is not None,
                        right.item is not None,
                        left.dye is not None,
                        right.dye is not None,
                        False,
                        False,
                        False,
                        False,
                    )
                )
                if left.item is not None:
                    cls._write_stack(fp, stack=left.item)
                if left.dye is not None:
                    cls._write_stack(fp, stack=left.dye)
                if right.item is not None:
                    cls._write_stack(fp, stack=right.item)
                if right.dye is not None:
                    cls._write_stack(fp, stack=right.dye)
            case FoodPlateExtra(item):
                cls._write_stack(fp, stack=item)
            case PylonExtra(_):
                pass
            case ItemFlaskExtra(item):
                cls._write_stack(fp, stack=item)
            case KiteExtra(kind):
                fp.write_short(kind)
            case _:
                cls._LOG.error("Unknown tile entity: %r", value)
                raise TypeError("Could not determine kind of tile entity", value)


__all__ = ("TileEntity",)
