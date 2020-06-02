class Pylon:
    """Data pertaining to a Pylon (https://terraria.gamepedia.com/Pylons)"""

    def __init__(self, pylon: bool = True):
        self.pylon: bool = pylon

    def __repr__(self):
        return f"pylon={self.pylon}"
