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
            # Updates rental table
            db_controller.execute.query(
                f"INSERT INTO rental (customer_id, car_id) VALUES (?, ?)", (customer_id, car_id)
            )
            # Updates availability car table
            db_controller.execute.query(
                f"UPDATE car SET available = 0 WHERE car_id = ?", (car_id,)
            )
            print(f"{car[0]} {car[1]} {car[2]} has been rented by {customer[0]} {customer[1]}.") # make model plate, first last name
            