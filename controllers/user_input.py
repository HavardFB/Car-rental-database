import re


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

# Needs regex
def plate_input(question):
    while True:
        try:
            user_input = str(input(question))
            if re.match(r"^[A-Z]{2}[0-9]{5}$", user_input):
                return user_input
            else:
                print("Please use the format: AB12345")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")