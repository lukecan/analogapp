"""Simple Tkinter GUI for managing film rolls and shots."""

from __future__ import annotations

import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

from .roll import FilmRoll
from .shot import Shot

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data.json")


def load_rolls() -> list[FilmRoll]:
    """Load film rolls from ``DATA_FILE``."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    rolls = []
    for entry in data:
        roll = FilmRoll(entry["name"])
        for s in entry.get("shots", []):
            roll.add_shot(
                Shot(
                    s["frame_number"],
                    s.get("description", ""),
                    aperture=s.get("aperture"),
                    shutter_speed=s.get("shutter_speed"),
                    location=s.get("location"),
                )
            )
        rolls.append(roll)
    return rolls


def save_rolls(rolls: list[FilmRoll]) -> None:
    """Save film rolls to ``DATA_FILE``."""
    data = []
    for roll in rolls:
        data.append(
            {
                "name": roll.name,
                "shots": [
                    {
                        "frame_number": s.frame_number,
                        "description": s.description,
                        "aperture": s.aperture,
                        "shutter_speed": s.shutter_speed,
                        "location": s.location,
                    }
                    for s in roll.list_shots()
                ],
            }
        )
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("AnalogApp")
        self.rolls: list[FilmRoll] = load_rolls()

        self.roll_list = tk.Listbox(self, width=25)
        self.roll_list.pack(side="left", fill="both", expand=True)
        self.roll_list.bind("<<ListboxSelect>>", self.show_shots)

        self.shot_list = tk.Listbox(self, width=50)
        self.shot_list.pack(side="left", fill="both", expand=True)

        btn_frame = tk.Frame(self)
        btn_frame.pack(side="bottom", fill="x")

        tk.Button(btn_frame, text="Add Roll", command=self.add_roll).pack(
            side="left", expand=True, fill="x"
        )
        tk.Button(btn_frame, text="Add Shot", command=self.add_shot).pack(
            side="left", expand=True, fill="x"
        )

        self.refresh_rolls()

    def refresh_rolls(self) -> None:
        self.roll_list.delete(0, tk.END)
        for roll in self.rolls:
            self.roll_list.insert(tk.END, roll.name)

    def show_shots(self, _event=None) -> None:
        self.shot_list.delete(0, tk.END)
        index = self.roll_list.curselection()
        if not index:
            return
        roll = self.rolls[index[0]]
        for shot in roll.list_shots():
            desc = f"Frame {shot.frame_number}"
            if shot.description:
                desc += f": {shot.description}"
            self.shot_list.insert(tk.END, desc)

    def add_roll(self) -> None:
        name = simpledialog.askstring("Add Roll", "Roll name:")
        if not name:
            return
        self.rolls.append(FilmRoll(name))
        save_rolls(self.rolls)
        self.refresh_rolls()

    def add_shot(self) -> None:
        index = self.roll_list.curselection()
        if not index:
            messagebox.showinfo("No Roll Selected", "Please select a roll first.")
            return
        roll = self.rolls[index[0]]
        frame = simpledialog.askinteger("Frame number", "Frame number:")
        if frame is None:
            return
        desc = simpledialog.askstring("Description", "Shot description:")
        aperture = simpledialog.askstring("Aperture", "Aperture (optional):")
        shutter = simpledialog.askstring("Shutter speed", "Shutter speed (optional):")
        location = simpledialog.askstring("Location", "Location (optional):")
        roll.add_shot(
            Shot(
                frame,
                desc or "",
                aperture=aperture or None,
                shutter_speed=shutter or None,
                location=location or None,
            )
        )
        save_rolls(self.rolls)
        self.show_shots()


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
