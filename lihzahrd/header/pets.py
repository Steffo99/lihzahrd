import typing


class Pets:
    """Pet related information"""
    def __init__(self,
                 cat: bool,
                 dog: bool,
                 bunny: bool):

        self.cat: bool = cat
        """Was the `Cat License <https://terraria.gamepedia.com/Cat_License>`_ ever activated?"""

        self.dog: int = dog
        """Was the `Dog License <https://terraria.gamepedia.com/Dog_License>`_ ever activated?"""

        self.bunny: float = bunny
        """Was the `Bunny License <https://terraria.gamepedia.com/Bunny_License>`_ ever activated?"""

    def __repr__(self):
        return f"{self.__class__.__qualname__}(cat={self.cat}, dog={self.dog}, bunny={self.bunny})"
