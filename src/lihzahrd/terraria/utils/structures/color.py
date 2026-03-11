# language=rst
"""
Submodule for color structures.
"""

from collections.abc import Iterator
from typing import overload, override


class ColorRGB:
    """
    An opaque 24-bit color.

    Can be created from RGB integers (0-255), from RGB floats (0.0-1.0), or from a hex code.

    Creating from RGB integers
    --------------------------

    RGB integers are converted to floats via ``component / 255``.

    .. warning::

        No checks are performed to make sure the components are within the expected ranges (``0`` - ``255``)!

    :param r: Red component.
    :param g: Green component.
    :param b: Blue component.

    Creating from RGB floats
    ------------------------

    RGB floats are stored directly in the structure, without being altered.

    .. warning::

        No checks are performed to make sure the components are within the expected ranges (``0.0`` - ``1.0``)!

    :param r: Red component.
    :param g: Green component.
    :param b: Blue component.

    Creating from hex code
    ----------------------

    Hex codes are converted to RGB floats via ``int(h[n:n+2], 16) / 255``.

    Trailing ``#`` are optionally stripped.

    .. warning::

        No checks are performed to make sure the hex code is valid!

    :param h: Hex color.

    Attributes and methods
    ----------------------
    """

    __slots__ = ("r", "g", "b")

    @overload
    def __init__(self, *, r: int, g: int, b: int) -> None: ...

    @overload
    def __init__(self, *, r: float, g: float, b: float) -> None: ...

    @overload
    def __init__(self, *, h: str) -> None: ...

    @override
    def __init__(self, *, r=None, g=None, b=None, h=None):
        self.r: float
        "The red component of the color."

        self.g: float
        "The green component of the color."

        self.b: float
        "The blue component of the color."

        if r is not None and g is not None and b is not None:
            if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
                self.r = r / 255
                self.g = g / 255
                self.b = b / 255

            elif isinstance(r, float) and isinstance(g, float) and isinstance(b, float):
                self.r = r
                self.g = g
                self.b = b

        elif h is not None:
            h = h.lstrip("#")
            if len(h) != 6:
                raise ValueError("h is not a hex color")
            self.r = int(h[0:2], 16) / 255
            self.g = int(h[2:4], 16) / 255
            self.b = int(h[4:6], 16) / 255

        else:
            raise ValueError(f"could not determine how to initialize {self.__class__.__qualname__}")

    @override
    def __repr__(self) -> str:
        r = self.r
        g = self.g
        b = self.b
        return f"{self.__class__.__qualname__}({r=}, {g=}, {b=})"

    def __iter__(self) -> Iterator[float]:
        """
        :return: :attr:`.r`, :attr:`.g`, and :attr:`.b` in order.
        """
        return iter((self.r, self.g, self.b))


__all__ = ("ColorRGB",)
