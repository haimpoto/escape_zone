def print_main_menu() -> None:
    print("""
===============================
🔞        Escape Zone       🔞
===============================


welcome to escape zone system.
you hane some options


1. Room management
2. Booking management
3. Statas
0. Exit
"""
)   
    return


def print_room_managment_menu() -> None:
    print("""
---------room managment---------

1. Show room by id
2. Show all rooms
3. Append room
4. Appdate room
5. Enabling/disabling room
0. Exit
"""
)
    return


def print_booking_managament_menu() -> None:
    print("""
---------booking managment---------

1. Show booking by id
2. Show booking by customer
3. Show booking by date
4. Show all bookings
5. Create a new booking
6. Update booking
7. Cancell booking
""")
    return


def print_room(room: dict) -> None:
    print()
    print(f"room id: {room.get("room_id", "error")}, room name: {room.get("name", "error")}, difficulty: {room.get("difficulty", "error")}")
    print(f"duration: {room.get("duration", "error")}, min players {room.get("min_players", "error")},  max players: {room.get("max_players", "error")}")
    print(f"price per player: {room.get("price_per_player", "error")}, is active: {room.get("is_active", "error")}")



def print_rooms(rooms: list[dict]) -> None:
    if not rooms:
        print("There is not rooms")
    for room in rooms:
        print()
        print(f"room id: {room.get("room_id", "error")}, room name: {room.get("name", "error")}, difficulty: {room.get("difficulty", "error")}")
        print(f"duration: {room.get("duration", "error")}, min players {room.get("min_players", "error")},  max players: {room.get("max_players", "error")}")
        print(f"price per player: {room.get("price_per_player", "error")}, is active: {room.get("is_active", "error")}")


def print_bookings(bookings: list[dict]) -> None:
    if not bookings:
        print("There is not bookings")
    for booking in bookings:
        print()
        print(f"booking id: {booking.get("booking_id", "error")}, customer name: {booking.get("customer_name", "error")}, room id: {booking.get("room_id", "error")}")
        print(f"booking date: {booking.get("booking_date", "error")}, start_time: {booking.get("start_time", "error")}, players: {booking.get("players", "error")}")
        print(f"total price: {booking.get("total_price")}, status: {booking.get("status", "error")}, cancellation fee: {booking.get("cancellation_fee", "error")}")
