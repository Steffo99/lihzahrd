class Rect:
    """Class delimining the bounds of a rectangle."""

    __slots__ = "left", "right", "top", "bottom"

    def __init__(self, left: int, right: int, top: int, bottom: int):
        self.left: int = left
        self.right: int = right
        self.top: int = top
        self.bottom: int = bottom

    def __repr__(self):
        return f"Rect(left={self.left}, right={self.right}, top={self.top}, bottom={self.bottom})"

    def to_tuple(self) -> tuple[int, int, int, int]:
        return self.left, self.right, self.top, self.bottom
