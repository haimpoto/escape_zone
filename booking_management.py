import connections
import prints
import valid_inputs
from datetime import datetime, time


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

        elif user_choice == "7":
            bookings = connections.load_bookings()
            user_booking_id = int(valid_inputs.get_valid_num("Enter booking id: "))
            bookings = cancell_booking_by_id(bookings, user_booking_id)
            if bookings:
                connections.dump_bookings(bookings)
                print("The booking is cancelled")


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




# def convert_datetime_to_str(date: datetime) -> str:
#     pass
# def convert_str_to_datetime(str_date: str) -> datetime:
#     return datetime.strptime(str_date, "%Y-%m-%d")
