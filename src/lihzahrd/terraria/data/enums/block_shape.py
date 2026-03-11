from enum import IntEnum
from typing import Self


class BlockShapeEnum(IntEnum):
    """
    The `shape`_ of a block, changed by hammering it.

    The directions refer to the missing slope corner.

    .. _shape: https://terraria.wiki.gg/wiki/Hammers#Slopes_and_half-blocks
    """

    NORMAL = 0
    "Block isn't sloped."

    TOP_HALF = 1
    "The top half of the block is missing."

    TOP_RIGHT = 2
    "The top right corner of the block is missing."

    TOP_LEFT = 3
    "The top left corner of the block is missing."

    BOTTOM_RIGHT = 4
    "The bottom right corner of the block is missing."

    BOTTOM_LEFT = 5
    "The bottom left corner of the block is missing."

    @classmethod
    def from_bits(cls, bit2: bool, bit1: bool, bit0: bool) -> Self:
        """
        Create a new :class:`.BlockShape` from tile bits.

        .. admonition:: Example

            .. code-block:: python

                >>> BlockShapeEnum.from_bits(True, False, False)
                <BlockShape.BOTTOM_RIGHT: 4>

            .. code-block:: python

                >>> BlockShapeEnum.from_bits(False, False, False)
                <BlockShape.NORMAL: 0>

        :param bit2: The ``flags2[6]`` bit.
        :param bit1: The ``flags2[5]`` bit.
        :param bit0: The ``flags2[4]`` bit.
        :return: The corresponding :class:`.BlockShape`.
        """
        value = bit2 * 4 + bit1 * 2 + bit0
        return cls(value)

    def to_bits(self) -> tuple[bool, bool, bool]:
        """
        Convert the :class:`.BlockShape` to the corresponding bits :class:`tuple`.

        .. admonition:: Example

            .. code-block:: python

                >>> BlockShapeEnum.BOTTOM_RIGHT.to_bits()
                (True, False, False)

            .. code-block:: python

                >>> BlockShapeEnum.NORMAL.to_bits()
                (False, False, False)

        :return: The resulting :class:`tuple` of bits, with, in order, ``flags2[6]``, ``flags2[5]``, and ``flags2[4]``.
        """
        return (
            bool((self.value & 0b100) >> 2),
            bool((self.value & 0b010) >> 1),
            bool(self.value & 0b001),
        )


__all__ = ("BlockShapeEnum",)
