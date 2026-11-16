import connections
import prints
import valid_inputs



def reports_menu() -> None:
    while True:
        prints.print_reports_menu()
        user_choice = valid_inputs.get_valid_num("Choose an option: ")

        if user_choice == "1":
            print(f"The active_bookings_quantity is {get_active_bookings_quantity()}")

        elif user_choice == "2":
            print(f"The cancelled_bookings_quantity is {get_cancelled_bookings_quantity()}")

        elif user_choice == "3":
            print(f"The total revenue fron active booking is {get_total_revenue_from_active_bookings()}")

        elif user_choice == "4":
             print(f"The total cancellation fees from cancelled bookings is {get_total_cancellation_fees_from_cancelled_bookings()}")

        elif user_choice == "5":
            popular_room, bookings = get_most_popular_room()
            print(f"The must popular room is: {popular_room} ({bookings} bookings)")

        elif user_choice == "6":
            for room, booking_num in get_number_of_bookings().items():
                print(f"{room}: {booking_num} bookings")

        elif user_choice == "0":
            break

        else:
            print(f"{user_choice} is not an option")


def get_active_bookings_quantity() -> int:
    bookings = connections.load_bookings()
    active_bookings_quantity = len([booking for booking in bookings if booking["status"] == "Active"])
    return active_bookings_quantity


def get_cancelled_bookings_quantity() -> int:
    bookings = connections.load_bookings()
    cancelled_bookings_quantity = len([booking for booking in bookings if booking["status"] == "Cancelled"])
    return cancelled_bookings_quantity


def get_total_revenue_from_active_bookings() -> int | float:
    bookings = connections.load_bookings()
    total_revenue = 0
    for booking in bookings:
        if booking["status"] == "Active":
            total_revenue += booking["total_price"]
    return total_revenue


def get_total_cancellation_fees_from_cancelled_bookings() -> int | float:
    bookings = connections.load_bookings()
    total_cancellation_fees = 0
    for booking in bookings:
        if booking["status"] == "Cancelled":
            total_cancellation_fees += booking["cancellation_fee"]
    return total_cancellation_fees
  

def get_number_of_bookings(only_active_rooms=False) -> dict:
    bookings = connections.load_bookings()
    number_of_bookings = {}
    for booking in bookings:
        if (not only_active_rooms) or booking["status"] == "Active":
            number_of_bookings[booking["room_id"]] = number_of_bookings.get(booking["room_id"], 0) + 1
    return number_of_bookings
        

def get_most_popular_room() -> tuple[str, int]:
    return max(get_number_of_bookings(only_active_rooms=True).items(), key=lambda items: items[1])
