class Wires:
    def __init__(self,
                 red: bool = False,
                 green: bool = False,
                 blue: bool = False,
                 yellow: bool = False,
                 actuator: bool = False):
        self.red: bool = red
        self.green: bool = green
        self.blue: bool = blue
        self.yellow: bool = yellow
        self.actuator: bool = actuator

    def __repr__(self):
        return f"Wires(red={self.red}, green={self.green}, blue={self.blue}, yellow={self.yellow}, actuator={self.actuator})"