import room_managament
import booking_management
import reports
import prints
import valid_inputs



def main() -> None:
    while True:
        prints.print_main_menu()
        user_choice = valid_inputs.get_valid_num("Choose an option: ")

        if user_choice == "1":
            room_managament.room_managament_menu()
        
        elif user_choice == "2":
            booking_management.booking_management_menu()

        elif user_choice == "3":
            reports.reports_menu()

        elif user_choice == "0":
            break
        
        else:
            print(f"{user_choice} is not an option")


if __name__ == "__main__":
    main()
