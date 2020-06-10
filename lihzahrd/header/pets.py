import typing


class Pets:
    """Information about the Pet Licenses that were activated in the world."""

    def __init__(self,
                 cat: bool,
                 dog: bool,
                 bunny: bool):

        self.cat: bool = cat
        """Was the Cat License (https://terraria.gamepedia.com/Cat_License) ever activated?"""

        self.dog: int = dog
        """Was the Dog License (https://terraria.gamepedia.com/Dog_License) ever activated?"""

        self.bunny: float = bunny
        """Was the Bunny License (https://terraria.gamepedia.com/Bunny_License) ever activated?"""

    def __repr__(self):
        return f"{self.__class__.__qualname__}(cat={self.cat}, dog={self.dog}, bunny={self.bunny})"
