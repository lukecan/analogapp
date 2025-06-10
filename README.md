# analogapp

`analogapp` is a small project for tracking film rolls and the shots taken on them. It aims to help photographers organize information about their analog photography workflow.

## Purpose

The goal of the project is to provide an easy way to store details about each film roll and to log notes about individual shots. Having all of this data in one place makes it simpler to look back at previous sessions and learn from past experiences.

## Setup

1. Clone the repository.
   ```bash
   git clone https://example.com/analogapp.git
   cd analogapp
   ```
2. Install the dependencies.
   ```bash
   pip install -r requirements.txt
   ```

## Features

- **Film roll management** &ndash; record the film type, ISO, and other relevant information for each roll.
- **Shot tracking** &ndash; log details for every frame such as aperture, shutter speed, location, and notes.

## Usage

Below is a small example showing how to create a film roll and add a shot with
additional metadata:

```python
from roll import FilmRoll
from shot import Shot

roll = FilmRoll("Vacation Roll")
roll.add_shot(
    Shot(
        1,
        "Sunrise at the beach",
        aperture="f/11",
        shutter_speed="1/60",
        location="Bali",
    )
)
```

### Running the web app

Start a local server after installing the dependencies:

```bash
python3 -m flask --app src.app run
```

## Contributing

Contributions are welcome! Please open an issue to discuss ideas or bugs before submitting a pull request. Keep commits focused and include tests or examples when adding new functionality.
