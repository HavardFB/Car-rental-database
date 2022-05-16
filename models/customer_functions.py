from controllers.user_input import name_input
from controllers.user_input import string_input
from controllers.user_input import phone_input
from controllers.user_input import year_input
from controllers.user_input import integer_input


def add_customer(db_controller):
    first_name = name_input("Enter first name (leave blank to cancel): ")
    if first_name is None:
        return
    last_name = name_input("Enter last name (leave blank to cancel): ")
    if last_name is None:
        return
    email = string_input(
        "Enter email (leave blank to cancel): "
    )  # Not using regex for email, too many email conventions to consider
    if email is None:
        return
    phone = phone_input("Enter phone number (leave blank to cancel): ")
    if phone is None:
        return
    birth_year = year_input("Enter birth year (leave blank to cancel): ")
    if birth_year is None:
        return

    # Inserting this way to prevent injection
    db_controller.execute_query(
        f"INSERT INTO customer (first_name, last_name, email, phone_number, birth_year) "
        f"VALUES (?, ?, ?, ?, ?)",
        (first_name, last_name, email, phone, birth_year),
    )


def edit_customer(db_controller):
    list_customers(db_controller)
    while True:
        customer_id = integer_input("Enter customer ID (leave blank to cancel): ")
        if customer_id is None:
            return
        # First check if it exists
        customer = db_controller.execute_single_read_query(
            f"SELECT first_name, last_name FROM customer WHERE customer_id = ?", (customer_id,)
        )

        if customer is None:
            print("There is no customer with that ID")
        else:
            first_name = name_input("Enter new first name (leave blank to cancel): ")
            if first_name is None:
                return
            last_name = name_input("Enter new last name (leave blank to cancel): ")
            if last_name is None:
                return
            email = string_input("Enter new email (leave blank to cancel): ")
            if email is None:
                return
            phone = phone_input("Enter new phone number (leave blank to cancel): ")
            if phone is None:
                return
            birth_year = year_input("Enter new birth year (leave blank to cancel): ")
            if birth_year is None:
                return

            # Updates database
            db_controller.execute_query(
                f"UPDATE customer SET first_name = ?, last_name = ?, email = ?, phone_number = ?, "
                f"birth_year = ? WHERE customer_id = ?",
                (first_name, last_name, email, phone, birth_year, customer_id),
            )
            return


def remove_customer(db_controller):
    list_customers(db_controller)
    while True:
        customer_id = integer_input("Enter customer ID (leave blank to cancel): ")
        if customer_id is None:
            return
        else:
            # First check if it exists
            customer = db_controller.execute_single_read_query(
                f"SELECT first_name, last_name FROM customer WHERE customer_id = ?", (customer_id,)
            )
            if customer is None:
                print("There is no customer with that ID")
            else:
                db_controller.execute_query(
                    f"DELETE FROM customer WHERE customer_id = ?", (customer_id,)
                )
                print(
                    f"Customer {customer[0]} {customer[1]} has been removed"
                )  # first_name and last_name
                return


def list_customers(db_controller):
    customers = db_controller.execute_read_query(
        "SELECT customer_id, first_name, last_name FROM customer", ()
    )
    if customers:
        print("Customers:")
        print("ID | Name")
        for customer in customers:
            print(f"{customer[0]}: {customer[1]} {customer[2]}")
    else:
        print("There are no customers")
        return -10
