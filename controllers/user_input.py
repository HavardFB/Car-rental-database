def string_input(question):
    while True:
        try:
            user_input = str(input(question))
            return user_input
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")


def integer_input(question):
    while True:
        try:
            user_input = int(input(question))
            return user_input
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")


def plate_input(question):
    while True:
        try:
            user_input = str(input(question))
            if len(user_input) == 7:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")