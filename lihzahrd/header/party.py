import typing


class Party:
    """NPC Party related information."""
    def __init__(self,
                 thrown_by_party_center: bool,
                 thrown_by_npcs: bool,
                 cooldown: int,
                 partying_npcs: typing.List[int]):
        self.thrown_by_party_center: bool = thrown_by_party_center
        """If the party was started by right-clicking a Party Center."""

        self.thrown_by_npcs: bool = thrown_by_npcs
        """If the item was spontaneously thrown by NPCs."""

        self.cooldown: int = cooldown
        """How long a party cannot be started for."""

        self.partying_npcs: typing.List[int] = partying_npcs
        """The list of NPC IDs that threw the party."""

    def __repr__(self):
        return f"WorldParty(thrown_by_party_center={self.thrown_by_party_center}," \
               f" thrown_by_npcs={self.thrown_by_npcs}, cooldown={self.cooldown}, partying_npcs={self.partying_npcs})"

    @property
    def is_active(self):
        return self.thrown_by_party_center or self.thrown_by_npcs
