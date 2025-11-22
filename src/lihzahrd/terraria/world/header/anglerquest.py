from .anglerquestfish import AnglerQuestFish


class AnglerQuest:
    """Information about today's Angler's quest."""

    def __init__(self, current_goal: AnglerQuestFish, completed_by: list[str]):
        self.current_goal: AnglerQuestFish = current_goal
        """The fish currently requested by the angler."""

        self.completed_by: list[str] = completed_by
        """A list of player names who completed the angler's quest today."""

    def __repr__(self):
        return f"WorldAnglersQuest(current_goal={self.current_goal}, completed_by={self.completed_by})"
