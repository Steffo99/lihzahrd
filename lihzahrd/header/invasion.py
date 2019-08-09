from .invasiontype import InvasionType


class Invasion:
    """Invasions (goblin army, pirates, martian madness...) related information."""

    def __init__(self, delay: int,
                 size: int,
                 type_: InvasionType,
                 position: float,
                 size_start: int):
        self.delay: int = delay
        self.size: int = size

        self.type: InvasionType = type_
        """The type of the current invasion (goblin army / pirates / martian madness...).

        If InvasionType.NONE, no invasion will be active in the world."""

        self.position: float = position
        self.size_start: int = size_start

    def __repr__(self):
        return f"WorldInvasion(delay={self.delay}, size={self.size}, type_={self.type}, position={self.position}," \
               f" size_start={self.size_start})"
