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
2. There are currently no external dependencies. The repository ships with a simple command-line interface in `src/cli.py` and a basic Tkinter GUI in `src/gui.py`. Run either one with Python to manage rolls and shots.

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

### Command-line interface

The repository ships with a minimal CLI that stores data in `data.json`. Example usage:

```bash
# create a new roll
python -m src.cli create-roll Vacation

# add a shot to the roll
python -m src.cli add-shot Vacation 1 "Sunrise at the beach" --aperture f/11 \
    --shutter 1/60 --location Bali

# list recorded rolls
python -m src.cli list-rolls
```

### Graphical interface

A lightweight Tkinter-based GUI is available as well. It uses the same `data.json` file to persist information.

```bash
python -m src.gui
```

## Contributing

Contributions are welcome! Please open an issue to discuss ideas or bugs before submitting a pull request. Keep commits focused and include tests or examples when adding new functionality.
