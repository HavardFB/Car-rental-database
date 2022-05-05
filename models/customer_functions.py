from controllers.user_input import name_input
from controllers.user_input import string_input
from controllers.user_input import phone_input
from controllers.user_input import year_input
from controllers.user_input import integer_input


def add_customer(db_controller):
    first_name = name_input("Enter first name: ")
    last_name = name_input("Enter last name: ")
    email = string_input(
        "Enter email: "
    )  # Not using regex for email, extremely many conventions for emails
    phone = phone_input("Enter phone number: ")
    birth_year = year_input("Enter birth year: ")

    # Inserting this way to prevent injection
    db_controller.execute_query(
        f"INSERT INTO customer (first_name, last_name, email, phone_number, birth_year) "
        f"VALUES (?, ?, ?, ?, ?)",
        (first_name, last_name, email, phone, birth_year),
    )


def edit_customer(db_controller):
    customer_id = integer_input("Enter customer ID: ")
    # First check if it exists
    customer = db_controller.execute_single_read_query(
        f"SELECT first_name, last_name FROM customer WHERE id = ?", (customer_id,)
    )
    if customer is None:
        print("There is no customer with that ID")
    else:
        first_name = name_input("Enter new first name: ")
        last_name = name_input("Enter new last name: ")
        email = string_input("Enter new email: ")
        phone = phone_input("Enter new phone number: ")
        birth_year = year_input("Enter new birth year: ")

        # Updates database
        db_controller.execute_query(
            f"UPDATE customer SET first_name = ?, last_name = ?, email = ?, phone_number = ?, "
            f"birth_year = ? WHERE id = ?",
            (first_name, last_name, email, phone, birth_year, customer_id),
        )


def remove_customer(db_controller):
    customer_id = integer_input("Enter customer ID: ")
    # First check if it exists
    customer = db_controller.execute_single_read_query(
        f"SELECT first_name, last_name FROM customer WHERE id = ?", (customer_id,)
    )
    if customer is None:
        print("There is no customer with that ID")
    else:
        db_controller.execute_query(
            f"DELETE FROM customer WHERE id = ?", (customer_id,)
        )
        print(
            f"Customer {customer[0]} {customer[1]} has been removed"
        )  # first_name and last_name
