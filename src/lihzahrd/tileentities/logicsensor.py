class LogicSensor:
    """Data pertaining to a Logic Sensor (https://terraria.gamepedia.com/Sensors)."""

    __slots__ = "logic_check", "enabled"

    def __init__(self, logic_check: int, enabled: bool):
        self.logic_check: int = logic_check
        self.enabled: bool = enabled

    def __repr__(self):
        return f"LogicSensor(logic_check={self.logic_check}, enabled={self.enabled})"
