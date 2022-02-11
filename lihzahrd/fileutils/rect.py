class Rect:
    """Class delimining the bounds of a rectangle."""

    __slots__ = "left", "right", "top", "bottom"

    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def __repr__(self):
        return f"Rect(left={self.left}, right={self.right}, top={self.top}, bottom={self.bottom})"
