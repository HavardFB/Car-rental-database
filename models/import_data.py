import csv
import json
from controllers.user_input import string_input


def import_customers(db_controller):
    # Loops until user enters a valid input
    while True:
        file_name = string_input(
            "Enter the exact file name with extensions (press enter to cancel): "
        )

        # Returns on cancel
        if file_name is None:
            return

        file_path = "imports/" + file_name

        # List to contain the customers
        customers = []
        # List of phone numbers in database to check for duplicates (phone numbers are unique)
        db_customers = db_controller.execute_read_query(
            "SELECT phone_number FROM customer", ()
        )
        # CSV IMPORT
        if file_name.endswith(".csv"):
            # Try, Except to catch file not found error
            try:
                # Opens file for reading with CSV module
                with open(file_path, "r", encoding="UTF8") as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=",")
                    # Appends the rows to the customers list
                    for row in csv_reader:
                        customers.append(row)

                # Finds the duplicates in the phone numbers.Uses list() to keep the original order of the list
                # otherwise the indexes would change due to removed duplicates
                for customer in list(customers):
                    for db_customer in db_customers:
                        if customer["phone_number"] == db_customer[0]:
                            customers.remove(customer)
                            break

                if len(customers) == 0:
                    print("No new customers found.")
                    return

                # Inserts the customers into the database
                for customer in customers:
                    db_controller.execute_query(
                        "INSERT INTO customer (first_name, last_name, email, phone_number, birth_year) "
                        "VALUES (?, ?, ?, ?, ?)",
                        (
                            customer["first_name"],
                            customer["last_name"],
                            customer["email"],
                            customer["phone_number"],
                            customer["birth_year"]
                        )
                    )
                print("Customers imported successfully")
                return
            except FileNotFoundError:
                print("File not found")

        # JSON IMPORT
        elif file_name.endswith(".json"):
            # Try Except to catch file not found error
            try:
                # Opens file for reading with JSON module
                with open(file_path, "r", encoding="UTF8") as json_file:
                    # Loads the file into a list
                    customers = json.load(json_file)

                # Finds the duplicates in the phone numbers.Uses list() to keep the original order of the list
                # otherwise the indexes would change due to removed duplicates
                for customer in list(customers):
                    for db_customer in db_customers:
                        if customer["phone_number"] == db_customer[0]:
                            customers.remove(customer)
                            break

                if len(customers) == 0:
                    print("No new customers found.")
                    return

                # Inserts the customers into the database
                for customer in customers:
                    db_controller.execute_query(
                        "INSERT INTO customer (first_name, last_name, email, phone_number, birth_year) "
                        "VALUES (?, ?, ?, ?,?)",
                        (
                            customer["first_name"],
                            customer["last_name"],
                            customer["email"],
                            customer["phone_number"],
                            customer["birth_year"]
                        )
                    )
                print("Customers imported successfully")
                return
            except FileNotFoundError:
                print("File not found")

        else:
            print("File type not supported.")


def import_cars(db_controller):
    while True:
        file_name = string_input(
            "Enter the exact file name with extensions (press enter to cancel): "
        )

        # Returns on cancel
        if file_name is None:
            return

        file_path = "imports/" + file_name

        # List to contain the cars
        cars = []
        # List of car plates that already exist in the database to check for duplicates
        db_cars = db_controller.execute_read_query("SELECT plate FROM car", ())
        # CSV IMPORT
        if file_name.endswith(".csv"):
            # Try Except to catch file not found error
            try:
                # Open file for reading with CSV module
                with open(file_path, "r", encoding="UTF8") as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=",")
                    # Appends the rows to the cars list
                    for row in csv_reader:
                        cars.append(row)

                # Finds the duplicates in the car plates. Uses list() to keep the original order of the list
                for car in list(cars):
                    for db_car in db_cars:
                        if car["plate"] == db_car[0]:
                            cars.remove(car)
                            break

                if len(cars) == 0:
                    print("No new cars to import")
                    return

                # Inserts the cars into the database
                for car in cars:
                    db_controller.execute_query(
                        "INSERT INTO car (make, model, plate, year, color, mileage) "
                        "VALUES (?, ?, ?, ?, ?, ?)",
                        (
                            car["make"],
                            car["model"],
                            car["plate"],
                            car["year"],
                            car["color"],
                            car["mileage"]
                        )
                    )
                print("Cars imported successfully")
                return
            except FileNotFoundError:
                print("File not found")

        # JSON IMPORT
        elif file_name.endswith(".json"):
            # Try Except to catch file not found error
            try:
                # Opens file for reading with JSON module
                with open(file_path, "r", encoding="UTF8") as json_file:
                    # Loads the json file into the list
                    cars = json.load(json_file)

                # Finds the duplicates in the car plates. Uses list() to keep the original order of the list
                for car in list(cars):
                    for db_car in db_cars:
                        if car["plate"] == db_car[0]:
                            cars.remove(car)
                            break

                if len(cars) == 0:
                    print("No new cars to import")
                    return

                # Inserts the cars into the database
                for car in cars:
                    db_controller.execute_query(
                        "INSERT INTO car (make, model, plate, year, color, mileage) "
                        "VALUES (?, ?, ?, ?, ?, ?)",
                        (
                            car["make"],
                            car["model"],
                            car["plate"],
                            car["year"],
                            car["color"],
                            car["mileage"]
                        )
                    )
                print("Cars imported successfully")
                return
            except FileNotFoundError:
                print("File not found")

        else:
            print("File type not supported.")


# I have chosen not to implement a function to import rental history, because in my opinion history is best
# saved in exported csv or json files, and not in the database itself.
