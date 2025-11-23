from typing import Self

from .difficulty import Difficulty
from ..version import Version
from ..worldversionedpackable import WorldVersionedPackable
from ...utils import FilePacker


class Challenges(WorldVersionedPackable):
    def __init__(
            self,
            difficulty_: Difficulty,
            drunk_world_: bool = False,
            for_the_worthy_: bool = False,
            tenth_anniversary_: bool = False,
            the_constant_: bool = False,
            bee_world_: bool = False,
            upside_down_: bool = False,
            trap_world_: bool = False,
            zenith_world_: bool = False,
    ):
        self.difficulty: Difficulty = difficulty_
        """
        The difficulty level the world is in.
        
        Note that the displayed difficulty level is altered by the for-the-worthy challenge flag.
        """

        self.drunk_world: bool = drunk_world_
        """If the world was created with the `Drunk world <https://terraria.wiki.gg/wiki/Secret_world_seeds#Drunk_world>`_ seed."""

        self.for_the_worthy: bool = for_the_worthy_
        """If the world was created with the `For the worthy <https://terraria.wiki.gg/wiki/Secret_world_seeds#For_the_worthy>`_ seed."""

        self.tenth_anniversary: bool = tenth_anniversary_
        """If the world was created with the `Celebrationmk10 <https://terraria.wiki.gg/wiki/Secret_world_seeds#Celebrationmk10>` seed."""

        self.the_constant: bool = the_constant_
        """If the world was created with `The Constant <https://terraria.wiki.gg/wiki/Secret_world_seeds#The_Constant>`_ seed."""

        self.bee_world: bool = bee_world_
        """If the world was created with the `Not the bees <https://terraria.wiki.gg/wiki/Secret_world_seeds#Not_the_bees>`_ seed."""

        self.upside_down: bool = upside_down_
        """If the world was created with the `Don't dig up <https://terraria.wiki.gg/wiki/Secret_world_seeds#Don't_dig_up>`_ seed."""

        self.trap_world: bool = trap_world_
        """If the world was created with the `No traps <https://terraria.wiki.gg/wiki/Secret_world_seeds#No_traps>`_ seed."""

        self.zenith_world: bool = zenith_world_
        """If the world was created with the `Get fixed boi <https://terraria.wiki.gg/wiki/Secret_world_seeds#Get_fixed_boi>`_ seed."""

    def __repr__(self) -> str:
        difficulty_ = self.difficulty
        drunk_world_ = self.drunk_world
        for_the_worthy_ = self.for_the_worthy
        tenth_anniversary_ = self.tenth_anniversary
        the_constant_ = self.the_constant
        bee_world_ = self.bee_world
        upside_down_ = self.upside_down
        trap_world_ = self.trap_world
        zenith_world_ = self.zenith_world
        return f"{self.__class__.__qualname__}({difficulty_=}, {drunk_world_=}, {for_the_worthy_=}, {tenth_anniversary_=}, {the_constant_=}, {bee_world_=}, {upside_down_=}, {trap_world_=}, {zenith_world_=})"

    # Unreachable code inspection seems to be broken on this function.
    # noinspection PyUnreachableCode
    def displayed_difficulty(self) -> str:
        if self.for_the_worthy:
            match self.difficulty:
                case Difficulty.JOURNEY:
                    return "Journey"
                case Difficulty.CLASSIC:
                    return "Expert"
                case Difficulty.EXPERT:
                    return "Master"
                case Difficulty.MASTER:
                    return "Legendary"
                case _:
                    return "Unknown"
        else:
            match self.difficulty:
                case Difficulty.JOURNEY:
                    return "Journey"
                case Difficulty.CLASSIC:
                    return "Classic"
                case Difficulty.EXPERT:
                    return "Expert"
                case Difficulty.MASTER:
                    return "Master"
                case _:
                    return "Unknown"

    def __str__(self):
        result = f"{self.difficulty} Mode"
        if self.drunk_world:
            result += ", Drunk World"
        if self.for_the_worthy:
            result += ", For The Worthy"
        if self.tenth_anniversary:
            result += ", Tenth Anniversary"
        if self.the_constant:
            result += ", The Constant"
        if self.bee_world:
            result += ", Bee World"
        if self.upside_down:
            result += ", Upside Down"
        if self.trap_world:
            result += ", Trap World"
        if self.zenith_world:
            result += ", Zenith World"
        return result

    def serialize(self, f: FilePacker, *, v: Version) -> None:
        self.difficulty.serialize(f, v=v)
        f.write_boolean(self.drunk_world)
        f.write_boolean(self.for_the_worthy)
        f.write_boolean(self.tenth_anniversary)
        f.write_boolean(self.the_constant)
        f.write_boolean(self.bee_world)
        f.write_boolean(self.upside_down)
        f.write_boolean(self.trap_world)
        f.write_boolean(self.zenith_world)

    @classmethod
    def deserialize(cls, f: FilePacker, *, v: Version) -> Self:
        difficulty_ = Difficulty.deserialize(f, v=v)
        drunk_world_ = f.read_boolean()
        for_the_worthy_ = f.read_boolean()
        tenth_anniversary_ = f.read_boolean()
        the_constant_ = f.read_boolean()
        bee_world_ = f.read_boolean()
        upside_down_ = f.read_boolean()
        trap_world_ = f.read_boolean()
        zenith_world_ = f.read_boolean()
        return cls(
            difficulty_=difficulty_,
            drunk_world_=drunk_world_,
            for_the_worthy_=for_the_worthy_,
            tenth_anniversary_=tenth_anniversary_,
            the_constant_=the_constant_,
            bee_world_=bee_world_,
            upside_down_=upside_down_,
            trap_world_=trap_world_,
            zenith_world_=zenith_world_,
        )


__all__ = (
    "Challenges",
)
