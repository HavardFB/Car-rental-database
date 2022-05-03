from textwrap import dedent
from models.car_functions import add_car, edit_car, remove_car
from controllers.user_input import string_input, integer_input


# The main screen for the application
def main_menu(db_controller):
    print("Welcome to the Car-rental system!")
    exit_application = False

    while not exit_application:
        print(
            dedent(
                """
        Please select an option by entering the corresponding number:
        1. Customer
        2. Car
        3. Rental
        4. Import/export data
        5. Exit
        """
            )
        )

        # Makes sure that user inputs a number
        user_choice = integer_input("Enter your choice: ")

        # Makes sure the user enters a valid number
        if user_choice in range(1, 6):
            if user_choice == 5:
                exit_application = True
                print("Thank you for using the Car-rental system!")
            elif user_choice == 1:
                customer_menu()
            elif user_choice == 2:
                car_menu(db_controller)
            elif user_choice == 3:
                rental_menu()
            elif user_choice == 4:
                import_export_menu()
        else:
            print("Your number is not in the menu range.")


# Submenu for doing changes to customers
def customer_menu():
    exit_menu = False

    while not exit_menu:
        print(
            dedent(
                """
        What do you want to do with customers?
        1. Add new customer
        2. Edit existing customer
        3. Remove customer
        4. Return to main menu
        """
            )
        )

        # Makes sure that user inputs a number
        user_choice = integer_input("Enter your choice: ")

        # Makes sure the user enters a valid number
        if user_choice in range(1, 5):
            if user_choice == 4:
                exit_menu = True
            elif user_choice == 1:
                print("Adding customer...")
            elif user_choice == 2:
                print("Editing customer...")
            elif user_choice == 3:
                print("Removing customer...")
        else:
            print("Your number is not in the menu range.")


# Submenu for doing changes to cars
def car_menu(db_controller):
    exit_menu = False

    while not exit_menu:
        print(
            dedent(
                """
        What do you want to do with cars?
        1. Add new car
        2. Edit existing car
        3. Remove car
        4. Return to main menu
        """
            )
        )

        # Makes sure that user inputs a number
        user_choice = integer_input("Enter your choice: ")

        # Makes sure the user enters a valid number
        if user_choice in range(1, 5):
            if user_choice == 4:
                exit_menu = True
            elif user_choice == 1:
                add_car(db_controller)
            elif user_choice == 2:
                edit_car(db_controller)
            elif user_choice == 3:
                remove_car(db_controller)
        else:
            print("Your number is not in the menu range.")


# Submenu for doing changes to rentals
def rental_menu():
    exit_menu = False

    while not exit_menu:
        print(
            dedent(
                """
        What do you want to do with rentals?
        1. Assign a car to a customer
        2. Remove a car from a customer
        3. Return to main menu
        """
            )
        )

        # Makes sure that user inputs a number
        user_choice = integer_input("Enter your choice: ")

        # Makes sure the user enters a valid number
        if user_choice in range(1, 4):
            if user_choice == 3:
                exit_menu = True
            elif user_choice == 1:
                print("Adding rental...")
            elif user_choice == 2:
                print("Removing rental...")
        else:
            print("Your number is not in the menu range.")


# Submenu for importing and exporting data
def import_export_menu():
    exit_menu = False

    while not exit_menu:
        print(
            dedent(
                """
        Please select an option:
        1. Import data from CSV file
        2. Export data to CSV file
        3. Import data from JSON file
        4. Export data to JSON file
        5. Return to main menu
        """
            )
        )

        # Makes sure that user inputs a number
        user_choice = integer_input("Enter your choice: ")

        # Makes sure the user enters a valid number
        if user_choice in range(1, 6):
            if user_choice == 5:
                exit_menu = True
            elif user_choice == 1:
                print("Importing from CSV file...")
            elif user_choice == 2:
                print("Exporting from CSV file...")
            elif user_choice == 3:
                print("Importing from JSON file...")
            elif user_choice == 4:
                print("Exporting from JSON file...")
        else:
            print("Your number is not in the menu range.")
