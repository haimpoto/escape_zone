import connections
import prints
import valid_inputs


def booking_management_menu():
    while True:
        prints.print_booking_managament_menu()
        user_choice = valid_inputs.get_valid_num("Choose an option: ")
        
        if user_choice == "1":
            bookings = connections.load_bookings()
        
        elif user_choice == "2":
            pass

        elif user_choice == "4":
            bookings = connections.load_bookings()
            prints.print_bookings(bookings=bookings)

        elif user_choice == "0":
            break
        
        else:
            print(f"{user_choice} is not an option")


def find_booking_by_id() -> None:
    pass


