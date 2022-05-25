from textwrap import dedent
from models.car_functions import add_car, edit_car, remove_car, search_car
from models.customer_functions import add_customer, edit_customer, remove_customer, search_customer
from models.rental_functions import add_rental, return_rental
from controllers.user_input import integer_input, string_input
from models.csv_export import csv_export_customers, csv_export_cars, csv_export_rental_history
from models.json_export import json_export_customers, json_export_cars, json_export_rental_history
from models.import_data import import_customers, import_cars


# The main screen for the application
def main_menu(db_controller):
    print("Welcome to the Car-rental system!")
    exit_application = False

    while not exit_application:
        print(
            dedent(
                """
        MAIN MENU
        ---------------------------------------------------
        Please select an option by entering the corresponding number:
        1. Customers
        2. Cars
        3. Rentals
        4. Search
        5. Import data
        6. Export data
        7. Exit
        ---------------------------------------------------
        """
            )
        )

        # Makes sure that user inputs a number
        user_choice = integer_input("Enter your choice: ")

        # Makes sure the user enters a valid number
        if user_choice in range(1, 8):
            if user_choice == 7:
                exit_application = True
                print("Thank you for using the Car-rental system!")
            elif user_choice == 1:
                customer_menu(db_controller)
            elif user_choice == 2:
                car_menu(db_controller)
            elif user_choice == 3:
                rental_menu(db_controller)
            elif user_choice == 4:
                search_menu(db_controller)
            elif user_choice == 5:
                import_menu(db_controller)
            elif user_choice == 6:
                export_menu(db_controller)
        else:
            print("Your number is not in the menu range.")


# Submenu for doing changes to customers
def customer_menu(db_controller):
    exit_menu = False

    while not exit_menu:
        print(
            dedent(
                """
        CUSTOMER MENU
        ---------------------------------------------------
        What do you want to do with customers?
        1. Add new customer
        2. Edit existing customer
        3. Remove customer
        4. Return to main menu
        ---------------------------------------------------
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
                add_customer(db_controller)
            elif user_choice == 2:
                edit_customer(db_controller)
            elif user_choice == 3:
                remove_customer(db_controller)
        else:
            print("Your number is not in the menu range.")


# Submenu for doing changes to cars
def car_menu(db_controller):
    exit_menu = False

    while not exit_menu:
        print(
            dedent(
                """
        CAR MENU
        ---------------------------------------------------
        What do you want to do with cars?
        1. Add new car
        2. Edit existing car
        3. Remove car
        4. Return to main menu
        ---------------------------------------------------
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
def rental_menu(db_controller):
    exit_menu = False

    while not exit_menu:
        print(
            dedent(
                """
        RENTAL MENU
        ---------------------------------------------------
        What do you want to do with rentals?
        1. Assign a car to a customer
        2. Return a rented car
        3. Return to main menu
        ---------------------------------------------------
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
                add_rental(db_controller)
            elif user_choice == 2:
                return_rental(db_controller)
        else:
            print("Your number is not in the menu range.")


def search_menu(db_controller):
    exit_menu = False

    while not exit_menu:
        print(
            dedent(
                """
        SEARCH MENU
        ---------------------------------------------------
        What do you want to search for?
        1. Customers
        2. Cars
        3. Go back.
        ---------------------------------------------------
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
                print("Searching for customers...")
                search_query = string_input("Please type your search query here: ")
                search_customer(db_controller, search_query)
            elif user_choice == 2:
                print("Searching for cars...")
                search_query = string_input("Please type your search query here: ")
                search_car(db_controller, search_query)
        else:
            print("Your number is not in the menu range.")

# Submenu for importing data
def import_menu(db_controller):
    exit_menu = False

    while not exit_menu:
        print(
            dedent(
                """
        IMPORT MENU
        ---------------------------------------------------
        What do you want to import?
        1. Customers
        2. Cars
        3. Go back
        ---------------------------------------------------
        """
            )
        )

        # Makes sure that user inputs a number
        user_choice = integer_input("Enter your choice: ")

        # Makes sure the user enters a valid number
        if user_choice in range(1, 4):
            if user_choice == 3:
                exit_menu = True
            elif user_choice == 1:  # Import customers
                import_customers(db_controller)
            elif user_choice == 2:  # Import cars
                import_cars(db_controller)
        else:
            print("Your number is not in the menu range.")


# Submenu for exporting data
def export_menu(db_controller):
    exit_menu = False

    while not exit_menu:
        print(
            dedent(
                """
        EXPORT MENU
        ---------------------------------------------------
        Please select the format you wish to export to:
        1. CSV
        2. JSON
        3. Go back.
        ---------------------------------------------------
        """
            )
        )

        # Makes sure that user inputs a number
        user_choice = integer_input("Enter your choice: ")

        # Makes sure the user enters a valid number
        if user_choice in range(1, 4):
            if user_choice == 3:
                exit_menu = True

            # Submenu for exporting data to CSV
            elif user_choice == 1:
                exit_submenu = False
                while not exit_submenu:
                    print(
                        dedent(
                            """
                    EXPORT TO CSV
                    ---------------------------------------------------
                    What do you want to export?
                    1. Customers
                    2. Cars
                    3. Rental history
                    4. Go back.
                    ---------------------------------------------------
                    """
                        )
                    )

                    # Makes sure that user inputs a number
                    user_choice = integer_input("Enter your choice: ")

                    # Makes sure the user enters a valid number
                    if user_choice in range(1, 5):
                        if user_choice == 4:
                            exit_submenu = True
                        elif user_choice == 1:  # CUSTOMER EXPORT
                            csv_export_customers(db_controller)
                        elif user_choice == 2:  # CAR EXPORT
                            csv_export_cars(db_controller)
                        elif user_choice == 3:  # RENTAL HISTORY EXPORT
                            csv_export_rental_history(db_controller)
                    else:
                        print("Your number is not in the menu range.")

            # Submenu for exporting data to JSON
            elif user_choice == 2:
                exit_submenu = False
                while not exit_submenu:
                    print(
                        dedent(
                            """
                    EXPORT TO JSON
                    ---------------------------------------------------
                    What do you want to export?
                    1. Customers
                    2. Cars
                    3. Rental history
                    4. Go back.
                    ---------------------------------------------------
                    """
                        )
                    )

                    # Makes sure that user inputs a number
                    user_choice = integer_input("Enter your choice: ")

                    # Makes sure the user enters a valid number
                    if user_choice in range(1, 5):
                        if user_choice == 4:
                            exit_submenu = True
                        elif user_choice == 1:  # CUSTOMER EXPORT
                            json_export_customers(db_controller)
                        elif user_choice == 2:  # CAR EXPORT
                            json_export_cars(db_controller)
                        elif user_choice == 3:  # RENTAL HISTORY EXPORT
                            json_export_rental_history(db_controller)
                    else:
                        print("Your number is not in the menu range.")
        else:
            print("Your number is not in the menu range.")
