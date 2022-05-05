from controllers.user_input import integer_input

def add_rental(db_controller):
    customer_id = integer_input("Enter the customer's ID: ")
    # First check if customer exists
    customer = db_controller.execute_single_read_query(
        f"SELECT first_name, last_name FROM customer WHERE customer_id = ?", (customer_id,)
    )
    if customer is None:
        print("There is no customer with that ID")
    else:
        car_id = integer_input("Enter the car's ID: ")
        # Then check if car exists
        car = db_controller.execute_single_read_query(
            f"SELECT make, model, plate FROM car WHERE car_id = ?", (car_id,)
        )
        if car is None:
            print("There is no car with that ID.")
        else:
            pass