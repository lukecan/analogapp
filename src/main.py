"""Entry point for the analog app."""

from roll import FilmRoll
from shot import Shot


def main() -> None:
    """Simple demonstration of how modules might interact."""
    roll = FilmRoll("Test Roll")
    roll.add_shot(
        Shot(
            1,
            "First frame",
            aperture="f/5.6",
            shutter_speed="1/250",
            location="New York",
        )
    )
    print(f"Roll {roll.name} has {len(roll.list_shots())} shots.")


if __name__ == "__main__":
    main()
