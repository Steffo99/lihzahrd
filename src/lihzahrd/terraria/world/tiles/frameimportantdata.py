class FrameImportantData:
    """Frame data of FrameImportant blocks.

    Some blocks share the same type and texture of other blocks (ex: banners), so they store some texture data inside
    the save file."""

    __slots__ = "frame_x", "frame_y"

    def __init__(self, frame_x, frame_y):
        self.frame_x: int = frame_x
        self.frame_y: int = frame_y

    def __repr__(self):
        return f"FrameImportantData(frame_x={self.frame_x}, frame_y={self.frame_y})"
