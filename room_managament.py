import connections
import valid_inputs
import prints


def room_managament_menu():
    while True:
        prints.print_room_managment_menu()
        user_choice = valid_inputs.get_valid_num("Choose an option: ")

        if user_choice == "1":
            rooms = connections.load_rooms()
            user_room_id = int(valid_inputs.get_valid_num("Enter room id: "))
            the_room_location = find_room_by_id(rooms, user_room_id)
            if the_room_location is None:
                print("The room is not found")
                continue
            the_room = rooms[the_room_location]
            prints.print_room(the_room)

        elif user_choice == "2":
            rooms = connections.load_rooms()
            prints.print_rooms(rooms=rooms)

        elif user_choice == "3":
            add_new_room()

        elif user_choice == "4":
            rooms = connections.load_rooms()
            user_room_id = int(valid_inputs.get_valid_num("Enter room id: "))
            rooms = update_room_by_id(rooms, user_room_id)
            if rooms:
                connections.dump_rooms(rooms)
                print("The room is apdated")

        elif user_choice == "5":
            rooms = connections.load_rooms()
            user_room_id = int(valid_inputs.get_valid_num("Enter room id: "))
            rooms = enabling_and_disabling_room(rooms, user_room_id)
            if rooms:
                connections.dump_rooms(rooms)
                print("The room is apdated")
            else:
                print("The room is not found")

        elif user_choice == "0":
            break

        else:
            print(f"{user_choice} is not an option")


def find_room_by_id(rooms: list, user_room_id: int) -> int | None:
    room_location = -1
    for i, room in enumerate(rooms):
        room_id = int("".join(ch for ch in room["room_id"] if ch.isdigit()))
        if room_id == user_room_id:
            room_location = i
    if room_location == -1:
        return None
    print("The room is found:")
    return room_location
    

def add_new_room() -> None:
    rooms: list = connections.load_rooms()
    new_room_id = get_new_room_id(rooms)
    new_room_name = valid_inputs.get_valid_str("Enter room name: ")
    new_room_difficulty = get_new_room_difficulty()
    if not new_room_difficulty:
        print("Error: you need enter 1, 2 or 3")
        return
    new_room_duration = int(valid_inputs.get_valid_num("Enter duration: "))
    new_room_min_players = int(valid_inputs.get_valid_num("Enter minimun players: "))
    new_room_max_players = int(valid_inputs.get_valid_num("Enter maximun players: "))
    if new_room_max_players < new_room_min_players:
        print("Error: max players cano't be higher than min players")
        return
    new_room_price_per_player = int(valid_inputs.get_valid_num("Enter price per player: "))
    new_room = { "room_id": new_room_id, "name": new_room_name, "difficulty": new_room_difficulty, "duration": new_room_duration,
        "min_players": new_room_min_players, "max_players": new_room_max_players, "price_per_player": new_room_price_per_player, "is_active": True}
    rooms.append(new_room)
    connections.dump_rooms(rooms)
    print("The room is appended!")


def get_new_room_difficulty():
    user_room_difficulty = valid_inputs.get_valid_num("Enter difficulty (1 for Easy, 2 for Medium, 3 for Hard): ")
    if user_room_difficulty == "1":
        return "Easy"
    elif user_room_difficulty == "2":
        return "Medium"
    elif user_room_difficulty == "3":
        return "Hard"
    else:
        return None

    
def get_new_room_id(rooms: list) -> str:
    try:
        max_room_id = max(rooms, key=lambda room: int("".join(ch for ch in room["room_id"] if ch.isdigit())))["room_id"]
    except ValueError:
        return "R001"
    else:
        int_max_room_id = int("".join(ch for ch in max_room_id if ch.isdigit()))
        int_new_room_id = int_max_room_id + 1
        new_room_id = "R" + "0" * (3 - len(str(int_new_room_id))) + str(int_new_room_id)
        return new_room_id


def update_room_by_id(rooms: dict, user_room_id: int) -> list | None:
    room_location = find_room_by_id(rooms=rooms, user_room_id=user_room_id)
    if room_location is None:
        return
    the_room = rooms[room_location]
    prints.print_room(the_room)
    
    user_field_chenge = valid_inputs.get_valid_num("Enter field to chaing: (1 for name, 2 for difficulty, 3 for duration, 4 for min players, 5 for max players, 6 for price per player): ")

    if user_field_chenge == "1":
        the_room["name"] = valid_inputs.get_valid_str("Enter new room name: ")

    elif user_field_chenge == "2":
        new_room_difficulty = get_new_room_difficulty()
        if not new_room_difficulty:
            print("Error: you need enter 1, 2 or 3")
            return
        the_room["difficulty"] = new_room_difficulty

    elif user_field_chenge == "3":
        the_room["duration"] = int(valid_inputs.get_valid_num("Enter new duration: "))

    elif user_field_chenge == "4":
        new_room_min_players = int(valid_inputs.get_valid_num("Enter minimun players: "))
        if the_room["max_players"] < new_room_min_players:
            print("Error: max players cano't be higher than min players")
            return
        the_room["min_players"] = new_room_min_players
    
    elif user_field_chenge == "5":
        new_room_max_players = int(valid_inputs.get_valid_num("Enter naximun players: "))
        if new_room_max_players < the_room["min_players"]:
            print("Error: max players cano't be higher than min players")
            return
        the_room["max_players"] = new_room_max_players

    elif user_field_chenge == "6":
        the_room["price_per_player"] = int(valid_inputs.get_valid_num("Enter price per player: "))
    
    else:
        print(f"{user_field_chenge} is not an option")
        return

    rooms[room_location] = the_room
    return rooms
    
    
def enabling_and_disabling_room(rooms: list, user_room_id: int):
    room_location = find_room_by_id(rooms=rooms, user_room_id=user_room_id)
    if room_location is None:
        return
    the_room = rooms[room_location]
    if the_room["is_active"] is True:
        the_room["is_active"] = False
        print(f"The room {the_room["room_id"]} change to not active")
    else:
        the_room["is_active"] = True
        print(f"The room {the_room["room_id"]} change to active")
    prints.print_room(the_room)
    rooms[room_location] = the_room
    return rooms
    