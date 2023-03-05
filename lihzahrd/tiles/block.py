import typing
from ..enums import BlockType
from .frameimportantdata import FrameImportantData
from .shape import Shape


class Block:
    """A block that has been placed in the world."""

    __slots__ = "type", "frame", "shape", "paint", "is_active", "is_illuminant", "is_echo"

    def __init__(
        self,
        type_: BlockType,
        shape: Shape = Shape.NORMAL,
        frame: typing.Optional[FrameImportantData] = None,
        paint: typing.Optional[int] = None,
        is_active: bool = True,
        is_illuminant: bool = False,
        is_echo: bool = False,
    ):
        self.type: BlockType = type_
        """The type of the block (dirt, stone, ...)."""

        self.frame: typing.Optional[FrameImportantData] = frame
        """The framedata of the block, if present."""

        self.shape: Shape = shape
        """The shape of the block, is changed with an hammer."""

        self.paint: typing.Optional[int] = paint
        """The paint color of a block."""

        self.is_active: bool = is_active
        """If the block is solid or can be passed through because of an Actuator."""

        self.is_illuminant: bool = is_illuminant
        """If the block had Illuminant Coating applied, and is unaffected by lighting."""

        self.is_echo: bool = is_echo
        """If the block had Echo Coating applied, and is invisible."""

    def __repr__(self):
        return f"Block(type_={repr(self.type)}, frame={self.frame}, shape={self.shape}, paint={self.paint}, is_active={self.is_active}, is_illuminant={self.is_illuminant}, is_echo={self.is_echo})"
