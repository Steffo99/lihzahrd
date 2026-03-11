# language=rst
"""
Submodule containing :class:`.WorldTiles`.
"""

from itertools import pairwise
from logging import getLogger
from typing import Any, override, Literal

from jinja2.nodes import Literal
from numpy import ndarray, zeros, roll, argwhere, save, load
from numpy.dtypes import BoolDType, IntDType

from lihzahrd.terraria.world.tiles.array_dtype import TILE_DTYPE
from lihzahrd.terraria.utils.file_processor import FileProcessor
from lihzahrd.terraria.utils.pack.primitive.op.collection import OpCollection
from lihzahrd.terraria.utils.pack.primitive.primitive import PackPrimitive
from lihzahrd.terraria.world.frame_important.world_frame_important import WorldFrameImportant
from lihzahrd.terraria.world.header.world_size import WorldSize


class WorldTiles(OpCollection[ndarray[tuple[int, int], Any]], PackPrimitive[ndarray[tuple[int, int], Any]]):
    """
    :class:`~lihzahrd.terraria.utils.pack.primitive.primitive.PackPrimitive` of the tiles present in a world.

    Internally, it's represented by a 2-dimensional :class:`numpy.ndarray` of the :obj:`~lihzahrd.terraria.world.tiles.array_dtype.TILE_DTYPE`.
    """

    _LOG = getLogger(__name__)

    def __repr__(self):
        return f"<{self.__class__.__qualname__}: {self.value.size} total tiles>"

    @classmethod
    @override
    def _validate(cls, value: ndarray[tuple[int, int], Any], **kwargs: Any) -> None:
        size: WorldSize = kwargs["size"]
        _frame_important: WorldFrameImportant = kwargs["frame_important"]

        if value.shape[0] != size.value.x:
            raise cls.InvalidShapeError(value)
        if value.shape[1] != size.value.y:
            raise cls.InvalidShapeError(value)

    @classmethod
    def _read_batch_to_ndarray(
        cls,
        fp: FileProcessor,
        data: ndarray[tuple[int], Any],
        *,
        frame_important: WorldFrameImportant,
    ) -> int:
        """
        Read a batch of tiles to the given 1-dimensional :class:`numpy.ndarray`.

        The tiles are written to the array starting from offset 0 and ending at an unknown offset, determined by the read ``repeat`` value.

        The ``repeat`` value, or the number of read tiles, is then returned.

        :param fp: The :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor` to read tiles from.
        :param data: The :class:`numpy.ndarray` to write tiles into.
        :param frame_important: The value of :class:`~lihzahrd.terraria.world.frame_important.world_frame_important.WorldFrameImportant` to use to determine which blocks have associated UV values, and which don't.
        :return: The number of read tiles (``repeat`` value).
        :meta public:
        """
        (
            has_more_flags,
            has_block,
            has_wall,
            liquid_id_0,
            liquid_id_1,
            has_extended_block_id,
            repeat_is_u8,
            repeat_is_u16,
        ) = fp.read_bits()

        (
            has_more_flags,
            has_red_wire,
            has_green_wire,
            has_blue_wire,
            block_shape_0,
            block_shape_1,
            block_shape_2,
            _,
        ) = (
            fp.read_bits() if has_more_flags else FileProcessor.INT_TO_BITS[0]
        )

        (
            has_more_flags,
            has_actuator,
            block_is_inactive,
            block_is_painted,
            wall_is_painted,
            has_yellow_wire,
            has_extended_wall_id,
            liquid_id_2,
        ) = (
            fp.read_bits() if has_more_flags else FileProcessor.INT_TO_BITS[0]
        )

        (
            _,
            block_is_echo,
            wall_is_echo,
            block_is_illuminant,
            wall_is_illuminant,
            _,
            _,
            _,
        ) = (
            fp.read_bits() if has_more_flags else FileProcessor.INT_TO_BITS[0]
        )

        # Read block
        block_id: int = 0
        block_u: int = 0
        block_v: int = 0
        block_paint: int = 0
        block_shape: int = 0
        if has_block:
            # Read block ID
            if has_extended_block_id:
                block_id = fp.read_ushort()
            else:
                block_id = fp.read_byte()
            # Read block frame UV
            if frame_important[block_id]:
                block_u = fp.read_ushort()
                block_v = fp.read_ushort()
            # Correct block_id
            block_id += 1
            # Read block paint
            if block_is_painted:
                block_paint = fp.read_byte() + 1
            # Determine block shape
            block_shape: int = (block_shape_2 << 2) + (block_shape_1 << 1) + block_shape_0

        # Read wall
        wall_id: int = 0
        wall_paint: int = 0
        if has_wall:
            # Read wall ID byte 0
            wall_id = fp.read_byte() + 1
            # Read wall paint
            if wall_is_painted:
                wall_paint = fp.read_byte() + 1

        # Process liquid
        liquid_id: int = (liquid_id_2 << 2) + (liquid_id_1 << 1) + liquid_id_0
        liquid_volume: int = 0
        if liquid_id:
            # Read liquid volume
            liquid_volume = fp.read_byte()

        # Read wall ID byte 1
        if has_extended_wall_id:
            wall_id += fp.read_byte() << 8

        # Read repeat amount
        repeat: int = 1
        if repeat_is_u16:
            repeat = fp.read_ushort() + 1
        elif repeat_is_u8:
            repeat = fp.read_byte() + 1

        data[0:repeat] = (
            block_id,
            block_u,
            block_v,
            block_shape,
            block_is_inactive,
            block_paint,
            block_is_illuminant,
            block_is_echo,
            wall_id,
            wall_paint,
            wall_is_illuminant,
            wall_is_echo,
            liquid_id,
            liquid_volume,
            has_red_wire,
            has_green_wire,
            has_blue_wire,
            has_yellow_wire,
            has_actuator,
        )

        return repeat

    @classmethod
    def _read_column_to_ndarray(
        cls,
        fp: FileProcessor,
        data: ndarray[tuple[int], Any],
        *,
        frame_important: WorldFrameImportant,
    ) -> None:
        """
        Read a column of tiles to the given 1-dimensional :class:`numpy.ndarray`.

        The tiles are written to the array from start to end, and are read from the :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor` until the array has no more room.

        :param fp: The :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor` to read tiles from.
        :param data: The :class:`numpy.ndarray` to write tiles into.
        :param frame_important: The value of :class:`~lihzahrd.terraria.world.frame_important.world_frame_important.WorldFrameImportant` to use to determine which blocks have associated UV values, and which don't.
        :meta public:
        """
        rows_count = data.shape[0]
        index_y = 0

        while index_y < rows_count:
            view = data.view()[index_y:]
            index_y += cls._read_batch_to_ndarray(fp=fp, data=view, frame_important=frame_important)

    @classmethod
    def _read_matrix_to_ndarray(
        cls, fp: FileProcessor, data: ndarray[tuple[int, int], Any], *, frame_important: WorldFrameImportant
    ) -> None:
        """
        Read the whole tile matrix to the given 2-dimensional :class:`numpy.ndarray`.

        For each column of the matrix, :meth:`_read_column_to_ndarray` is called to fill it.

        :param fp: The :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor` to read tiles from.
        :param data: The :class:`numpy.ndarray` to write tiles into.
        :param frame_important: The value of :class:`~lihzahrd.terraria.world.frame_important.world_frame_important.WorldFrameImportant` to use to determine which blocks have associated UV values, and which don't.
        :meta public:
        """
        column_count = data.shape[0]

        for x in range(column_count):
            if x % 100 == 0:
                cls._LOG.info("Reading column: %r / %r", x, column_count)
            else:
                cls._LOG.debug("Reading column: %r / %r", x, column_count)
            view = data.view()[x]
            cls._read_column_to_ndarray(fp=fp, data=view, frame_important=frame_important)

    @classmethod
    @override
    def _read(cls, fp: FileProcessor, **kwargs) -> ndarray[tuple[int, int], Any]:
        size: WorldSize = kwargs["size"]
        frame_important: WorldFrameImportant = kwargs["frame_important"]
        cache_path: str = kwargs.get("cache_path", None)

        use_cache = cache_path is not None

        try:
            cache_file = open(cache_path, "rb") if use_cache else None

        except FileNotFoundError:
            cache_file = None

        try:
            if use_cache and cache_file:
                data = load(cache_file, allow_pickle=False)
            else:
                # noinspection PyTypeChecker
                data: ndarray[tuple[int, int], Any] = zeros(
                    shape=tuple(size.value),
                    dtype=TILE_DTYPE,
                )
                cls._read_matrix_to_ndarray(fp=fp, data=data, frame_important=frame_important)
                if use_cache:
                    cache_file = open(cache_path, "wb") if use_cache else None
                    save(cache_file, data, allow_pickle=False)
            return data

        finally:
            try:
                # noinspection PyUnboundLocalVariable
                if cache_file:
                    # noinspection PyUnboundLocalVariable
                    cache_file.close()
            except NameError:
                pass

    @classmethod
    def _create_difference_matrix(cls, value: ndarray[tuple[int, int], Any]) -> ndarray[tuple[int, int], BoolDType]:
        """
        Given a tile matrix, create a new boolean matrix where the true values indicate which tiles mark the start of a new tile batch.

        :param value: The :class:`numpy.ndarray` to use for the computation.
        :return: The resulting matrix.
        :meta public:
        """
        # Roll down 1 block the tile matrix
        shifted_value = roll(value, shift=1, axis=1)
        # Remove the tiles that overflowed from the roll
        shifted_value[:, 0] = 0
        # Compare each tile with the one that was rolled up
        result = value != shifted_value
        # Always consider the first tile of a column a new one
        result[:, 0] = True
        return result

    @classmethod
    def _create_tile_batches(
        cls,
        value: ndarray[tuple[int, int], Any],
    ) -> list[tuple[ndarray[tuple[Literal[1]], Any], ndarray[tuple[Literal[1]], IntDType]]]:
        """
        Given a tile matrix, return a :class:`list` of tile batches.

        The first element of each :class:`tuple` is the tile scalar to write, still in :class:`numpy.ndarray` format, and the second element is how many times the tile is repeated vertically.

        :param value: The :class:`numpy.ndarray` to use for the computation.
        :return: The resulting :class:`list` of :class:`tuple`.
        :meta public:
        """
        difference = cls._create_difference_matrix(value)

        value_flat = value.flatten()
        difference_flat = difference.flatten()

        result: list[tuple[ndarray[tuple[Literal[1]], Any], ndarray[tuple[Literal[1]], Any]]] = []

        differences_at = argwhere(difference_flat)
        for difference_at, next_difference_at in pairwise(differences_at):
            tile = value_flat[difference_at]
            repeat = next_difference_at - difference_at
            result.append((tile, repeat))

        result.append((value_flat[-1], value_flat.shape[0] - differences_at[-1]))
        return result

    @classmethod
    def _write_tile_batch(
        cls,
        fp: FileProcessor,
        batch: tuple[ndarray[tuple[Literal[1]], Any], ndarray[tuple[Literal[1]], IntDType]],
        *,
        frame_important: WorldFrameImportant,
    ) -> None:
        """
        Write a single batch of tiles to the given :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor`.

        :param fp: The :class:`~lihzahrd.terraria.utils.file_processor.FileProcessor` to write tiles to.
        :param batch: The batch of tiles to write, in the form of a :class:`tuple` returned by :meth:`_create_tile_batches`.
        :param frame_important: The value of :class:`~lihzahrd.terraria.world.frame_important.world_frame_important.WorldFrameImportant` to use to determine which blocks have associated UV values, and which don't.
        :meta public:
        """
        tile = batch[0]

        repeat = batch[1].item()

        block_id = tile["block_id"].item()
        if has_block := bool(block_id):
            block_id -= 1
        has_extended_block_id = block_id >= 256 if has_block else False

        block_u = tile["block_u"].item()
        block_v = tile["block_v"].item()
        block_shape = tile["block_shape"].item()
        block_inactive = tile["block_inactive"].item()
        block_paint = tile["block_paint"].item()
        block_illuminant = tile["block_illuminant"].item()
        block_echo = tile["block_echo"].item()

        wall_id = tile["wall_id"].item()
        if has_wall := bool(wall_id):
            wall_id -= 1
        has_extended_wall_id = wall_id >= 256 if has_wall else False

        wall_paint = tile["wall_paint"].item()
        wall_illuminant = tile["wall_illuminant"].item()
        wall_echo = tile["wall_echo"].item()

        liquid_id = tile["liquid_id"].item()
        liquid_volume = tile["liquid_volume"].item()

        wire_red = tile["wire_red"].item()
        wire_green = tile["wire_green"].item()
        wire_blue = tile["wire_blue"].item()
        wire_yellow = tile["wire_yellow"].item()
        wire_actuator = tile["wire_actuator"].item()

        repeat_is_u8 = 1 < repeat <= FileProcessor.BYTE_MAX
        repeat_is_u16 = FileProcessor.BYTE_MAX < repeat <= FileProcessor.USHORT_MAX

        flags4: tuple[bool, bool, bool, bool, bool, bool, bool, bool] = (
            False,
            block_echo,
            wall_echo,
            block_illuminant,
            wall_illuminant,
            False,
            False,
            False,
        )
        has_flags4 = any(flags4)

        flags3: tuple[bool, bool, bool, bool, bool, bool, bool, bool] = (
            has_flags4,
            wire_actuator,
            block_inactive,
            bool(block_paint),
            bool(wall_paint),
            wire_yellow,
            has_extended_wall_id,
            bool(liquid_id & 0b0000_0100),
        )
        has_flags3 = any(flags3)

        flags2: tuple[bool, bool, bool, bool, bool, bool, bool, bool] = (
            has_flags3,
            wire_red,
            wire_green,
            wire_blue,
            bool(block_shape & 0b0000_0001),
            bool(block_shape & 0b0000_0010),
            bool(block_shape & 0b0000_0100),
            False,
        )
        has_flags2 = any(flags2)

        flags1: tuple[bool, bool, bool, bool, bool, bool, bool, bool] = (
            has_flags2,
            has_block,
            has_wall,
            bool(liquid_id & 0b0000_0001),
            bool(liquid_id & 0b0000_0010),
            has_extended_block_id,
            repeat_is_u8,
            repeat_is_u16,
        )

        fp.write_bits(flags1)
        if has_flags2:
            fp.write_bits(flags2)
        if has_flags3:
            fp.write_bits(flags3)
        if has_flags4:
            fp.write_bits(flags4)

        if has_block:
            if has_extended_block_id:
                fp.write_ushort(block_id)
            else:
                fp.write_byte(block_id)

            if frame_important[block_id]:
                fp.write_ushort(block_u)
                fp.write_ushort(block_v)

            if block_paint:
                fp.write_byte(block_paint)

        if has_wall:
            fp.write_byte(wall_id & 0x00_FF)

            if wall_paint:
                fp.write_byte(wall_paint)

        if liquid_id:
            fp.write_byte(liquid_volume)

        if has_extended_wall_id:
            fp.write_byte((wall_id & 0xFF_00) >> 8)

        if repeat_is_u16:
            fp.write_ushort(repeat - 1)
        elif repeat_is_u8:
            fp.write_byte(repeat - 1)

    @classmethod
    @override
    def _write(cls, fp: FileProcessor, value: ndarray[tuple[int, int], Any], **kwargs: Any) -> None:
        frame_important: WorldFrameImportant = kwargs["frame_important"]

        batches = cls._create_tile_batches(value)
        batches_count = len(batches)

        for index, batch in enumerate(batches):
            if index % 10000 == 0:
                cls._LOG.info("Writing batch: %r / %r", index, batches_count)
            else:
                cls._LOG.debug("Writing batch: %r / %r", index, batches_count)
            cls._write_tile_batch(fp, batch, frame_important=frame_important)

    class InvalidShapeError(PackPrimitive[ndarray[tuple[Any, Any], Any]].ValidationError):
        """
        The shape of the underlying :class:`numpy.ndarray` does not match the given world size.
        """


__all__ = (
    "TILE_DTYPE",
    "WorldTiles",
)
