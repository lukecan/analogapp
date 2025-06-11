import argparse
import json
import os
from .roll import FilmRoll
from .shot import Shot

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data.json')

def load_rolls():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    rolls = []
    for entry in data:
        roll = FilmRoll(entry['name'])
        for s in entry.get('shots', []):
            roll.add_shot(
                Shot(
                    s['frame_number'],
                    s.get('description', ''),
                    aperture=s.get('aperture'),
                    shutter_speed=s.get('shutter_speed'),
                    location=s.get('location'),
                )
            )
        rolls.append(roll)
    return rolls

def save_rolls(rolls):
    data = []
    for roll in rolls:
        data.append({
            'name': roll.name,
            'shots': [
                {
                    'frame_number': s.frame_number,
                    'description': s.description,
                    'aperture': s.aperture,
                    'shutter_speed': s.shutter_speed,
                    'location': s.location,
                }
                for s in roll.list_shots()
            ],
        })
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def create_roll(args):
    rolls = load_rolls()
    rolls.append(FilmRoll(args.name))
    save_rolls(rolls)
    print(f"Created roll '{args.name}'")

def add_shot(args):
    rolls = load_rolls()
    for roll in rolls:
        if roll.name == args.roll:
            roll.add_shot(
                Shot(
                    args.frame,
                    args.description,
                    aperture=args.aperture,
                    shutter_speed=args.shutter,
                    location=args.location,
                )
            )
            save_rolls(rolls)
            print(f"Added frame {args.frame} to roll '{args.roll}'")
            return
    print(f"Roll '{args.roll}' not found")

def list_rolls(_args):
    rolls = load_rolls()
    if not rolls:
        print("No rolls available")
        return
    for roll in rolls:
        print(f"{roll.name}: {len(roll.list_shots())} shots")

def list_shots(args):
    rolls = load_rolls()
    for roll in rolls:
        if roll.name == args.roll:
            if not roll.list_shots():
                print("No shots recorded")
                return
            for shot in roll.list_shots():
                desc = f" - {shot.description}" if shot.description else ""
                print(f"{shot.frame_number}{desc}")
            return
    print(f"Roll '{args.roll}' not found")

def build_parser():
    parser = argparse.ArgumentParser(description="Manage film rolls and shots")
    sub = parser.add_subparsers(dest='command', required=True)

    new_roll = sub.add_parser('create-roll', help='Create a new film roll')
    new_roll.add_argument('name')
    new_roll.set_defaults(func=create_roll)

    add = sub.add_parser('add-shot', help='Add a shot to a film roll')
    add.add_argument('roll', help='Roll name')
    add.add_argument('frame', type=int, help='Frame number')
    add.add_argument('description', help='Shot description')
    add.add_argument('--aperture')
    add.add_argument('--shutter')
    add.add_argument('--location')
    add.set_defaults(func=add_shot)

    lr = sub.add_parser('list-rolls', help='List all film rolls')
    lr.set_defaults(func=list_rolls)

    ls = sub.add_parser('list-shots', help='List shots for a roll')
    ls.add_argument('roll')
    ls.set_defaults(func=list_shots)
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
