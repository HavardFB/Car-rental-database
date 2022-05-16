import re


# For user input of generic string
def string_input(question):
    while True:
        try:
            user_input = str(input(question))
            # Blank input cancels the query
            if re.match(r"^[ \n\r]{0,8}$", user_input): # Allow for multiple spaces in case of accidental space input
                return None
            else:
                return user_input
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")


# For user input of generic integer
def integer_input(question):
    while True:
        try:
            user_input = str(input(question))
            # Blank input cancels the query
            if re.match(r"^[ \n\r]{0,8}$", user_input):  # Allow for multiple spaces in case of accidental space input
                return None
            else:
                return int(user_input)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")


# For user input of car plate number
def plate_input(question):
    while True:
        try:
            user_input = str(input(question))
            if re.match(
                r"^[A-Z]{2}[0-9]{5}$", user_input
            ):  # Check if the format is correct
                return user_input
            # Blank input cancels the query
            elif re.match(r"^[ \n\r]{0,8}$", user_input): # Allow for multiple spaces in case of accidental space input
                return None
            else:
                print("Please use the format: AB12345")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")


# For user input of names
def name_input(question):
    while True:
        try:
            user_input = str(input(question))
            if re.match(
                r"^[A-ZÆØÅ]{1}[a-zæøå]{1,30}$", user_input
            ):  # Check if the format is correct
                return user_input
            # Blank input cancels the query
            elif re.match(r"^[ \n\r]{0,8}$", user_input): # Allow for multiple spaces in case of accidental space input
                return None
            else:
                print("Please use the format: Aa")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")


# For user input of phone numbers
def phone_input(question):
    while True:
        try:
            user_input = str(input(question))
            if re.match(
                r"^(00|\+)[1-9][0-9 \-\(\)\.]{7,24}$", user_input
            ):  # Allows for a wide range of phone numbers
                return user_input # Will not format phone number into a standard format due to variations in every country
            # Blank input cancels the query
            elif re.match(r"^[ \n\r]{0,8}$", user_input): # Allow for multiple spaces in case of accidental space input
                return None
            elif not re.match(r"^(00|\+)", user_input):
                print("Please remember to add the country code.")
            else:
                print(
                    "Please try to use a common format. E.g. +4512345678, 0047 418 84 284, +47 (418 00 287)"
                )
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")


# For user input of years (e.g. 1999, 2015, 1962)
def year_input(question):
    while True:
        try:
            user_input = str(input(question))
            if re.match(
                    r"^[0-9]{4}$", user_input
            ):  # Check if the format is correct
                return int(user_input)
            # Blank input cancels the query
            elif re.match(r"^[ \n\r]{0,8}$", user_input): # Allow for multiple spaces in case of accidental space input
                return None
            else:
                print("Please use the format: 1234")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
