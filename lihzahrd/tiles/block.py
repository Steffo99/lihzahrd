import typing
from .blocktype import BlockType
from .frameimportantdata import FrameImportantData


class Block:
    def __init__(self,
                 type_: BlockType,
                 frame: typing.Optional[FrameImportantData],
                 paint: typing.Optional[int],
                 is_active: bool = True):
        self.type: BlockType = type_
        self.frame: typing.Optional[FrameImportantData] = frame
        self.paint: typing.Optional[int] = paint
        self.is_active: bool = is_active

    def __repr__(self):
        return f"Block(type_={repr(self.type)}, frame={self.frame}, paint={self.paint}, is_active={self.is_active})"
