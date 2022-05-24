import csv
import json
from controllers.user_input import string_input


def import_customers(db_controller):
    file_name = string_input("Enter the exact file name (with extension): ")
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
        # Try Except to catch file not found error
        try:
            # Opens file for reading with CSV module
            with open(file_path, "r", encoding="UTF8") as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=",")
                # Appends the rows to the customers list
                for row in csv_reader:
                    customers.append(row)

                # Finds the duplicates in the phone numbers
                for customer in list(customers):
                    for db_customer in db_customers:
                        if customer["phone_number"] == db_customer[0]:
                            customers.remove(customer)
                            break

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
                            customer["birth_year"],
                        ),
                    )
                print("Customers imported successfully")
        except FileNotFoundError:
            print("File not found")
            
    # JSON IMPORT
    elif file_name.endswith(".json"):
        pass
    else:
        print("File type not supported.")


def import_cars(db_controller):
    pass


def import_rental_history(db_controller):
    pass
