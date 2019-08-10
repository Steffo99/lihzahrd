import typing
from .walltype import WallType


class Wall:
    def __init__(self, type_: WallType, paint: typing.Optional[int]):
        self.type: WallType = type_
        self.paint: typing.Optional[int] = paint
