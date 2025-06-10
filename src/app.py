"""Simple Flask web app for managing film rolls and shots."""

from __future__ import annotations

from flask import Flask, jsonify, request

from .roll import FilmRoll
from .shot import Shot

app = Flask(__name__)

# In-memory storage of film rolls.
rolls: dict[str, FilmRoll] = {}


@app.post("/rolls")
def create_roll() -> tuple[dict[str, str], int]:
    """Create a new film roll."""
    data = request.get_json(force=True)
    name = data.get("name")
    if not name:
        return {"error": "name required"}, 400
    if name in rolls:
        return {"error": "roll already exists"}, 400
    rolls[name] = FilmRoll(name)
    return {"message": f"Roll {name} created"}, 201


@app.get("/rolls")
def list_rolls() -> list[str]:
    """List all film rolls."""
    return jsonify([roll.name for roll in rolls.values()])


@app.post("/rolls/<roll_name>/shots")
def add_shot(roll_name: str) -> tuple[dict[str, str], int]:
    """Add a shot to the specified roll."""
    roll = rolls.get(roll_name)
    if roll is None:
        return {"error": "roll not found"}, 404

    data = request.get_json(force=True)
    frame_number = data.get("frame_number")
    if frame_number is None:
        return {"error": "frame_number required"}, 400

    shot = Shot(
        frame_number,
        data.get("description", ""),
        data.get("aperture"),
        data.get("shutter_speed"),
        data.get("location"),
    )
    roll.add_shot(shot)
    return {"message": "shot added"}, 201


@app.get("/rolls/<roll_name>/shots")
def list_shots(roll_name: str):
    """List shots for a given roll."""
    roll = rolls.get(roll_name)
    if roll is None:
        return {"error": "roll not found"}, 404

    return jsonify([shot.__dict__ for shot in roll.list_shots()])


if __name__ == "__main__":
    app.run(debug=True)
