class TargetDummy:
    """Data pertaining to a Target Dummy (https://terraria.gamepedia.com/Target_Dummy)"""

    def __init__(self, npc: int):
        # TODO: what's this?
        self.npc: int = npc

    def __repr__(self):
        return f"{self.__class__.__name__}(npc={self.npc})"
