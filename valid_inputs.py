def get_valid_num(massage: str) -> str:
    user_input = input(massage)
    while not user_input.strip().isdigit():
        print(f"Enter number, {user_input} is invalid choice")
        user_input = input(massage)
    return user_input


def get_valid_str(massage: str) -> str:
    user_input = input(massage)
    while not user_input.strip():
        user_input = input(massage)
    return user_input
    