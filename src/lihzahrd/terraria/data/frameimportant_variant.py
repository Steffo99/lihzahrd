# language=rst
"""
Module for :class:`.FrameImportantVariant`.

.. glossary::

    FrameImportant

        Terraria blocks can be *FrameImportant* or not.

        FrameImportant blocks have different attributes depending on the specific animation frame they currently are in.

        Information about their current animation frame is saved in the world file itself.

        This mechanism is used for various purposes:

        - storing what kind of weed is growing on grass, and changing its name and color if it's a Mushroom
        - storing the on-off state of :class:`lihzahrd.terraria.data.classmembers.blocks.Torch`, and using it to determine whether it emits light
        - storing the kind of :class:`lihzahrd.terraria.data.classmembers.blocks.Torch`, and using it to determine its color
        - ...

"""

import numbers

from lihzahrd.terraria.utils.structures.color import ColorRGB


class FrameImportantVariant:
    """
    A variant of a :term:`FrameImportant` block.

    An instance of this class represents a specific variant of a block, that means, the properties a block acquires if it's in a certain animation frame, and the conditions for them to apply.

    :attr:`.eq_u`, :attr:`.eq_v`, :attr:`.min_u`, :attr:`.min_v`, :attr:`.max_u`, :attr:`.max_v` represent conditions which must be fulfilled; the not-:obj:`None` ones are AND-ed together by :meth:`.evaluate`.

    :attr:`.name`, :attr:`.color`, :attr:`.solid`, :attr:`.blend`, :attr:`.merge`, :attr:`.transparent`, :attr:`.is_stone`, :attr:`.is_grass`, and :attr:`.emit_light_color` are properties, and if they are not :obj:`None`, they are applied to the block containing this variant.
    """

    def __init__(
        self,
        *,
        eq_u: numbers.Real | None = None,
        eq_v: numbers.Real | None = None,
        min_u: numbers.Real | None = None,
        min_v: numbers.Real | None = None,
        max_u: numbers.Real | None = None,
        max_v: numbers.Real | None = None,
        name: str | None = None,
        color: ColorRGB | None = None,
        solid: bool | None = None,
        blend: bool | None = None,
        merge: bool | None = None,
        transparent: bool | None = None,
        is_stone: bool | None = None,
        is_grass: bool | None = None,
        emit_light_color: ColorRGB | None = None,
    ) -> None:
        self.eq_u: numbers.Real | None = eq_u
        "The exact value ``u`` can have for this variant to apply, or :obj:`None` to skip this check."

        self.eq_v: numbers.Real | None = eq_v
        "The exact value ``u`` can have for this variant to apply, or :obj:`None` to skip this check."

        self.min_u: numbers.Real | None = min_u
        "The minimum value ``u`` can have for this variant to apply, or :obj:`None` to skip this check."

        self.min_v: numbers.Real | None = min_v
        "The minimum value ``v`` can have for this variant to apply, or :obj:`None` to skip this check."

        self.max_u: numbers.Real | None = max_u
        "The maximum value ``u`` can have for this variant to apply, or :obj:`None` to skip this check."

        self.max_v: numbers.Real | None = max_v
        "The maximum value ``v`` can have for this variant to apply, or :obj:`None` to skip this check."

        self.name: str | None = name
        "The name that the tile should take if this variant applies, or :obj:`None` to not alter it."

        self.color: ColorRGB | None = color
        "The color that the tile should take if this variant applies, or :obj:`None` to not alter it."

        self.solid: bool | None = solid
        "The solidity that the tile should take if this variant applies, or :obj:`None` to not alter it."

        self.blend: bool | None = blend
        "Unknown."

        self.merge: bool | None = merge
        "Unknown."

        self.transparent: bool | None = transparent
        "The transparency (letting light through) that the tile should take if this variant applies, or :obj:`None` to not alter it."

        self.is_stone: bool | None = is_stone
        "Whether this tile should count as stone if this variant applies, or :obj:`None` to not alter it."

        self.is_grass: bool | None = is_grass
        "Whether this tile should count as grass if this variant applies, or :obj:`None` to not alter it."

        self.emit_light_color: ColorRGB | None = emit_light_color
        "The color that the tile should take if this variant applies, or :obj:`None` to not alter it."

    def evaluate(self, u: numbers.Real | None = None, v: numbers.Real | None = None) -> bool:
        """
        Determine whether this variant should be applied or not.

        :param u: The u parameter of the block.
        :param v: The v parameter of the block.
        :return: Whether this variant should be applied or not.
        """
        result = True
        if self.eq_u is not None:
            result &= (u is not None) and (u == self.eq_u)
        if self.eq_v is not None:
            result &= (v is not None) and (v == self.eq_v)
        if self.min_u is not None:
            result &= (u is not None) and (u >= self.min_u)
        if self.min_v is not None:
            result &= (v is not None) and (v >= self.min_v)
        if self.max_u is not None:
            result &= (u is not None) and (u <= self.max_u)
        if self.max_v is not None:
            result &= (v is not None) and (v <= self.max_v)
        return result


__all__ = ("FrameImportantVariant",)
