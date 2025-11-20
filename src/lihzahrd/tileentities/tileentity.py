from ..fileutils import Coordinates
from .targetdummy import TargetDummy
from .itemframe import ItemFrame
from .logicsensor import LogicSensor


class TileEntity:
    """A TileEntity, such as a Training Dummy, an Item Frame or a Logic Sensor."""

    __slots__ = "id", "position", "data"

    def __init__(self, id_: int, position: Coordinates, extra: TargetDummy|ItemFrame|LogicSensor):
        self.id: int = id_
        self.position: Coordinates = position
        self.data: TargetDummy|ItemFrame|LogicSensor = extra

    def __repr__(self):
        return f"<TileEntity {self.id} at {self.position} ({repr(self.data)})>"
