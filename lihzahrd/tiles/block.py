import typing
from ..enums import BlockType
from .frameimportantdata import FrameImportantData
from .shape import Shape


class Block:
    """A block that has been placed in the world."""

    __slots__ = "type", "frame", "shape", "paint", "is_active"

    def __init__(self,
                 type_: BlockType,
                 shape: Shape = Shape.NORMAL,
                 frame: typing.Optional[FrameImportantData] = None,
                 paint: typing.Optional[int] = None,
                 is_active: bool = True):
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

    def __repr__(self):
        return f"Block(type_={repr(self.type)}, frame={self.frame}, paint={self.paint}, is_active={self.is_active})"
