from datetime import datetime, time, date
import connections
import prints
import valid_inputs
import room_managament



def booking_management_menu():
    while True:
        prints.print_booking_managament_menu()
        user_choice = valid_inputs.get_valid_num("Choose an option: ")
        
        if user_choice == "1":
            bookings = connections.load_bookings()
            user_booking_id = int(valid_inputs.get_valid_num("Enter booking id: "))
            the_booking_location = find_booking_by_id(bookings, user_booking_id)
            if the_booking_location is None:
                print("The booking is not found")
                continue
            print("The booking is found")
            the_booking = bookings[the_booking_location]
            prints.print_booking(the_booking)

        elif user_choice == "2":
            bookings = connections.load_bookings()
            user_booking_customer = valid_inputs.get_valid_str("Enter booding customer: ")
            the_booking_location = find_booking_by_customer(bookings, user_booking_customer)
            if the_booking_location is None:
                print("The booking is not found")
                continue
            print("The booking is found")
            the_booking = bookings[the_booking_location]
            prints.print_booking(the_booking)

        elif user_choice == "3":
            bookings = connections.load_bookings()
            user_date_year = valid_inputs.get_valid_num("Enter a yaer: ")
            user_date_month = valid_inputs.get_valid_num("Enter a month: ")
            user_date_day = valid_inputs.get_valid_num("Enter a day: ")
            the_booking_location = find_booking_by_str_date(bookings, user_date_year, user_date_month, user_date_day)
            if the_booking_location is None:
                print("The booking is not found")
                continue
            print("The booking is found")
            the_booking = bookings[the_booking_location]
            prints.print_booking(the_booking)

        elif user_choice == "4":
            bookings = connections.load_bookings()
            prints.print_bookings(bookings=bookings)

        elif user_choice == "5":
            pass

        elif user_choice == "7":
            bookings = connections.load_bookings()
            user_booking_id = int(valid_inputs.get_valid_num("Enter booking id: "))
            bookings = cancell_booking_by_id(bookings, user_booking_id)
            if bookings:
                connections.dump_bookings(bookings)
                print("The booking is cancelled")
            else:
                print("The booking is not found")

        elif user_choice == "0":
            break
        
        else:
            print(f"{user_choice} is not an option")


def find_booking_by_id(bookings: list, user_booking_id: int) -> int | None:
    bookig_location = -1
    for i, booking in enumerate(bookings):
        booking_id = int("".join(ch for ch in booking["booking_id"] if ch.isdigit()))
        if booking_id == user_booking_id:
            bookig_location = i
    if bookig_location == -1:
        return None
    return bookig_location


def find_booking_by_customer(bookings: list, user_booking_customer: int) -> int | None:
    booking_location = -1
    for i, booking in enumerate(bookings):
        if user_booking_customer.lower() in booking["customer_name"].lower():
            booking_location = i
    if booking_location == -1:
        return None
    return booking_location


def find_booking_by_str_date(bookings: list, year: str, month: str, day: str) -> int | None:
    booking_location = -1
    for i, booking in enumerate(bookings):
        if booking["booking_date"] == f"{year}-{month}-{day}":
            booking_location = i
    if booking_location == -1:
        return None
    return booking_location


def cancell_booking_by_id(bookings: list, user_booking_id: int):
    booking_location = find_booking_by_id(bookings, user_booking_id)
    if booking_location is None:
        return
    the_booking = bookings[booking_location]
    if the_booking["status"] == "Active":
        the_booking["status"] = "Cancelled"
    prints.print_booking(the_booking)
    bookings[booking_location] = the_booking
    return bookings
    

def create_booking(bookings: list):
    booking_id = get_new_booking_id()

    booking_customer_name = valid_inputs.get_valid_str("Enter costumer name: ")

    user_booking_room_id = valid_inputs.get_valid_num("Enter room id: ")
    user_booking_room = room_managament.find_room_by_id(rooms=connections.load_rooms(), user_room_id=int(user_booking_room_id))
    if not user_booking_room:
        print("Error: The room is not found")
        return None
    booking_room_id = f"R{user_booking_room_id.zfill(3)}"

    user_booking_date = get_user_date()
    if date.strptime(user_booking_date, "%Y%m%d") < date.today():
        print("Error: The date must be in the future")
        return None
    booking_date = user_booking_date


    user_booking_players_num = int(valid_inputs.get_valid_num("Enter players number: "))
    if user_booking_players_num > user_booking_room["duration"]:
        print("Error: The number of players exceeds the allowed number")
        return None
    booking_players_num = user_booking_players_num

    booking_total_price = get_booking_price(booking_players_num, user_booking_room, booking_date)





def get_new_booking_id(bookings: list) -> str:
    try:
        max_booking_id = max(bookings, key=lambda booking: int("".join(ch for ch in booking["booking_id"] if ch.isdigit())))["booking_id"]
    except ValueError:
        return "R001"
    else:
        int_max_booking_id = int("".join(ch for ch in max_booking_id if ch.isdigit()))
        int_new_booking_id = int_max_booking_id + 1
        new_booking_id = "R" + "0" * (3 - len(str(int_new_booking_id))) + str(int_new_booking_id)
        return new_booking_id


def get_user_date() -> str | None:
    user_year = valid_inputs.get_valid_num("Enter year (4 digits): ")
    if len(user_year) != 4:
        print("year must be 4 digits")
        return None
    user_month = valid_inputs.get_valid_num("Enter month (2 digits): ")
    if len(user_month) != 2:
        print("month must be 2 digits")
        return None
    user_day = valid_inputs.get_valid_num("Enter day (2 digits): ")
    if len(user_day) != 2:
        print("day must be 2 digits")
        return None
    return f"{user_year}-{user_month}-{user_day}"
    

def get_booking_price(players_num: int, room: dict, booking_date: str) -> int | float:
    total_price = room["price_per_player"] * players_num

    if players_num >= 7:
        total_price *= 0.85
    elif players_num >= 5:
        total_price *= 0.90

    if date.strptime(booking_date, "%Y%m%d").weekday() in {4, 5}:
        total_price *= 1.15
    
    
    

# def convert_datetime_to_str(date: datetime) -> str:
#     pass
# def convert_str_to_datetime(str_date: str) -> datetime:
#     return datetime.strptime(str_date, "%Y-%m-%d")
