"""Placeholder module for individual shots."""

class Shot:
    """Represents a single shot."""

    def __init__(self, frame_number: int, description: str = ""):
        self.frame_number = frame_number
        self.description = description
