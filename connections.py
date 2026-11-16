from pathlib import Path
import json

ROOMS_PATH = Path(__file__).parent / "rooms.json"
BOOKING_PATH = Path(__file__).parent / "bookings.json"


def load_rooms() -> list[dict]:
    try:
        with open(ROOMS_PATH, "r") as json_file:
            rooms = json.load(json_file)
        return rooms
    except json.decoder.JSONDecodeError:
        return []


def dump_rooms(rooms: list[dict]) -> None:
    with open(ROOMS_PATH, "w") as json_file:
        json.dump(rooms, json_file, indent=4)


def load_bookings() -> list[dict]:
    try:
        with open(BOOKING_PATH, "r") as json_file:
            bookings = json.load(json_file)
        return bookings
    except json.decoder.JSONDecodeError:
        return []


def dump_bookings(bookings: list[dict]) -> None:
    with open(BOOKING_PATH, "w") as json_file:
        json.dump(bookings, json_file, indent=4)
        