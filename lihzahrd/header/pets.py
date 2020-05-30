import typing

class Pets:
    """Pet related information"""
    def __init__(self,
                cat: bool,
                dog: bool,
                bunny: bool):
        self.cat: bool = cat
        """Has the cat been bought."""

        self.dog: int = dog
        """Has the cat been bought."""

        self.bunny: float = bunny
        """Has the bunny been bought."""

    def __repr__(self):
        return f"WorldPets(cat={self.cat}, dog={self.dog}, bunny={self.bunny})"
