"""Placeholder module for individual shots."""

class Shot:
    """Represents a single shot on a film roll."""

    def __init__(
        self,
        frame_number: int,
        description: str = "",
        aperture: str | None = None,
        shutter_speed: str | None = None,
        location: str | None = None,
    ) -> None:
        """Create a new :class:`Shot` instance.

        Parameters
        ----------
        frame_number:
            The frame number on the roll.
        description:
            Optional text describing the shot.
        aperture:
            The aperture used, e.g. ``"f/2.8"``.
        shutter_speed:
            The shutter speed used, e.g. ``"1/125"``.
        location:
            Where the shot was taken.
        """

        self.frame_number = frame_number
        self.description = description
        self.aperture = aperture
        self.shutter_speed = shutter_speed
        self.location = location
