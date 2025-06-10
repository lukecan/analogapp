"""Placeholder module for film roll management."""

class FilmRoll:
    """Represents a roll of film."""

    def __init__(self, name: str):
        self.name = name
        self.shots = []

    def add_shot(self, shot: 'Shot') -> None:
        """Add a shot to the film roll."""
        self.shots.append(shot)

    def list_shots(self) -> list:
        """Return all shots on the film roll."""
        return self.shots
