# language=rst
"""
Submodule for :class:`.BlockBase`.
"""

from logging import getLogger

from lihzahrd.terraria.utils.structures.color import ColorRGB

from lihzahrd.terraria.data.classenums.block_enum import BlockEnum
from lihzahrd.terraria.data.enums.block_shape import BlockShapeEnum
from lihzahrd.terraria.data.enums.paint import PaintEnum
from lihzahrd.terraria.data.frameimportant_variant import FrameImportantVariant

log = getLogger(__name__)


class BlockBase(metaclass=BlockEnum, register=False):
    """
    The kind of Terraria block.

    All blocks inherit from this; it's a :term:`ClassMemberBase` for members of :class:`.BlockEnum`.

    It:

    - annotates the mandatory attributes that all blocks should have.
    - implements the :class:`.FrameImportantVariant` system for the :term:`ClassInstance`.

    :param frame: The ``uv`` sprite coordinates of this block's current animation frame, or :obj:`None` if the block is not frame important.
    :param shape: The shape the block has. Defaults to :obj:`BlockShapeEnum.NORMAL`, which is the full block.
    :param is_inactive: Whether the block has been deactivated by an actuator or not.
    :param paint: The paint that is applied to the block, or :obj:`None` if no paint is applied.
    :param is_illuminant: Whether the block has had Illuminant Coating applied to it and is therefore always full bright.
    :param is_echo: Whether the block has had Echo Coating applied to it and is therefore invisible.
    """

    __slots__ = (
        "_frame",
        "_frameimportant_variants_cache",
        "shape",
        "is_inactive",
        "paint",
        "is_illuminant",
        "is_echo",
    )

    ID: int
    "The ID of the tile."

    NAME: str
    "The default name of the :term:`ClassMember`."

    COLOR: ColorRGB | None = None
    "The default color of the :term:`ClassMember`."

    SOLID: bool = False
    "The default solidity of the :term:`ClassMember`."

    BLEND: bool = True
    "Unknown."

    MERGE: bool = True
    "Unknown."

    TRANSPARENT: bool = False
    "The default transparency (lets light through) of the :term:`ClassMember`."

    IS_STONE: bool = False
    "The default stone-ness of the :term:`ClassMember`."

    IS_GRASS: bool = False
    "The default grass-ness of the :term:`ClassMember`."

    EMIT_LIGHT_COLOR: ColorRGB | None = None
    "The default color of the light emitted by the :term:`ClassMember`, if any."

    FRAMEIMPORTANT_VARIANTS: tuple[FrameImportantVariant, ...]
    """
    Ordered :class:`tuple` of all :class:`.FrameImportantVariant` potentially applying to this tile, from the first to be tested, to the last.
    """

    def __init__(
        self,
        *,
        frame: tuple[int, int] | None = None,
        shape: BlockShapeEnum = BlockShapeEnum.NORMAL,
        is_inactive: bool = False,
        paint: PaintEnum = PaintEnum.NONE,
        is_illuminant: bool = False,
        is_echo: bool = False,
    ):
        self._frame: tuple[int, int] | None = frame
        "The sprite coordinates of this block's current animation frame, or :obj:`None` if the block is not frame important."

        self._frameimportant_variants_cache: tuple[FrameImportantVariant, ...] | None = None
        """
        A cache of the :class:`.FrameImportantVariant` that apply to this :term:`ClassInstance`. 
        
        If :obj:`None`, the cache has to be rebuilt.
        """

        self.shape: BlockShapeEnum = shape
        "The shape the block has."

        self.is_inactive: bool = is_inactive
        "Whether the block has been deactivated by an actuator or not."

        self.paint: PaintEnum = paint
        "The paint that is applied to the block."

        self.is_illuminant: bool = is_illuminant
        "Whether the block has had Illuminant Coating applied to it and is therefore always full bright."

        self.is_echo: bool = is_echo
        "Whether the block has had Echo Coating applied to it and is therefore invisible."

    def __repr__(self):
        return f"<{self.__class__.__qualname__}>"

    @property
    def frame(self) -> tuple[int, int] | None:
        """
        :return: The ``uv`` sprite coordinates of this block's current animation frame, or :obj:`None` if the block is not frame important.
        """
        return self._frame

    @frame.setter
    def frame(self, value: tuple[int, int] | None) -> None:
        """
        Update :attr:`_frame` and invalidate the :attr:`_frameimportant_variants_cache`.

        :param value: The new ``uv`` value of :attr:`_frame`.
        """
        self._frame = value

        log.debug("frame changed, clearing variants cache...")
        self._frameimportant_variants_cache = None

    @property
    def u(self) -> int | None:
        """
        The ``u`` sprite coordinate of this block's current animation frame, or :obj:`None` if the block is not frame important.
        """
        return self._frame[0] if self._frame is not None else None

    @property
    def v(self) -> int | None:
        """
        The ``v`` sprite coordinate of this block's current animation frame, or :obj:`None` if the block is not frame important.
        """
        return self._frame[1] if self._frame is not None else None

    def is_frameimportant(self) -> bool:
        """
        :return: Whether this :term:`ClassInstance` is FrameImportant, determined by whether :attr:`_u` and :attr:`_v` are set.
        """
        return self._frame is not None

    def _frameimportant_variants(self) -> tuple[FrameImportantVariant, ...]:
        """
        Update the :attr:`._frameimportant_variants_cache` if necessary, then return it.
        """
        if self._frameimportant_variants_cache is None:
            log.info("Recalculating variants...")
            self._frameimportant_variants_cache = tuple(
                filter(lambda variant: variant.evaluate(u=self.u, v=self.v), self.FRAMEIMPORTANT_VARIANTS)
            )
        return self._frameimportant_variants_cache

    def name(self) -> str:
        """
        :return: The name of this :term:`ClassInstance`.
        """
        for variant in self._frameimportant_variants():
            if variant.name is not None:
                return variant.name
        else:
            return self.NAME

    def color(self) -> ColorRGB | None:
        """
        :return: The color of this :term:`ClassInstance`.
        """
        for variant in self._frameimportant_variants():
            if variant.color is not None:
                return variant.color
        else:
            return self.COLOR

    def solid(self) -> bool:
        """
        :return: The solidity of this :term:`ClassInstance`.
        """
        for variant in self._frameimportant_variants():
            if variant.solid is not None:
                return variant.solid
        else:
            return self.SOLID

    def blend(self) -> bool:
        for variant in self._frameimportant_variants():
            if variant.blend is not None:
                return variant.blend
        else:
            return self.BLEND

    def merge(self) -> bool:
        for variant in self._frameimportant_variants():
            if variant.merge is not None:
                return variant.merge
        else:
            return self.MERGE

    def transparent(self) -> bool:
        """
        :return: The transparency (lets light through) of the :term:`ClassInstance`.
        """
        for variant in self._frameimportant_variants():
            if variant.transparent is not None:
                return variant.transparent
        else:
            return self.TRANSPARENT

    def is_stone(self) -> bool:
        """
        :return: The stone-ness of the :term:`ClassInstance`.
        """
        for variant in self._frameimportant_variants():
            if variant.is_stone is not None:
                return variant.is_stone
        else:
            return self.IS_STONE

    def is_grass(self) -> bool:
        """
        :return: The grass-ness of the :term:`ClassInstance`.
        """
        for variant in self._frameimportant_variants():
            if variant.is_grass is not None:
                return variant.is_grass
        else:
            return self.IS_GRASS

    def emit_light_color(self) -> ColorRGB | None:
        """
        :return: The color of the light emitted by the :term:`ClassInstance`, if any.
        """
        for variant in self._frameimportant_variants():
            if variant.emit_light_color is not None:
                return variant.emit_light_color
        else:
            return self.EMIT_LIGHT_COLOR


__all__ = ("BlockBase",)
