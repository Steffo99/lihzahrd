import enum


class PaintEnum(enum.IntEnum):
    """
    The color with which a block is painted.

    .. seealso::

        `Paint and coating IDs on the Official Terraria Wiki`_

    .. _Paint and coating IDs on the Official Terraria Wiki: https://terraria.wiki.gg/wiki/Paint_and_coating_IDs
    """

    NONE = 0
    "No paint."

    RED = 1
    "Red Paint."

    ORANGE = 2
    "Orange Paint."

    YELLOW = 3
    "Yellow Paint."

    LIME = 4
    "Lime Paint."

    GREEN = 5
    "Green Paint."

    TEAL = 6
    "Teal Paint."

    CYAN = 7
    "Cyan Paint."

    SKY_BLUE = 8
    "Sky blue Paint."

    BLUE = 9
    "Blue Paint."

    PURPLE = 10
    "Purple Paint."

    VIOLET = 11
    "Violet Paint."

    PINK = 12
    "Pink Paint."

    DEEP_RED = 13
    "Deep Red Paint."

    DEEP_ORANGE = 14
    "Deep Orange Paint."

    DEEP_YELLOW = 15
    "Deep Yellow Paint."

    DEEP_LIME = 16
    "Deep Lime Paint."

    DEEP_GREEN = 17
    "Deep Green Paint."

    DEEP_TEAL = 18
    "Deep Teal Paint."

    DEEP_CYAN = 19
    "Deep Cyan Paint."

    DEEP_SKY_BLUE = 20
    "Deep Sky Blue Paint."

    DEEP_BLUE = 21
    "Deep Blue Paint."

    DEEP_PURPLE = 22
    "Deep Purple Paint."

    DEEP_VIOLET = 23
    "Deep Violet Paint."

    DEEP_PINK = 24
    "Deep Pink Paint."

    BLACK = 25
    "Black Paint."

    WHITE = 26
    "White Paint."

    GRAY = 27
    "Gray Paint."

    BROWN = 28
    "Brown Paint."

    SHADOW = 29
    "Shadow Paint."

    NEGATIVE = 30
    "Negative Paint."

    _ILLUMINANT = 31
    """
    Old paint ID for Illuminant Coating.
    
    Illuminant coating is not part of paints anymore, as it can be applied separately from paint.
    
    :meta public:
    """

    def is_deep_paint(self) -> bool:
        """
        :return: Whether the paint is deep or not.
        """
        return self.name.startswith("DEEP")


__all__ = ("PaintEnum",)
