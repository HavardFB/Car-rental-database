from controllers.user_input import integer_input
from models.customer_functions import list_customers
from models.car_functions import list_available_cars


def add_rental(db_controller):
    list_customers(db_controller)
    if list_customers(db_controller) == -10:
        return
    else:
        while True:
            customer_id = integer_input("Enter the customer's ID (leave blank to cancel): ")
            if customer_id is None:
                return
            # First check if customer exists
            customer = db_controller.execute_single_read_query(
                f"SELECT first_name, last_name FROM customer WHERE customer_id = ?", (customer_id,)
            )
            if customer is None:
                print("There is no customer with that ID")
            else:
                list_available_cars(db_controller)
                if list_available_cars(db_controller) == -10:
                    return
                else:
                    while True:
                        car_id = integer_input("Enter the car's ID (leave blank to cancel): ")
                        if car_id is None:
                            return

                        # Then checks if car exists and is available
                        car = db_controller.execute_single_read_query(
                            f"SELECT make, model, plate, available FROM car WHERE car_id = ?", (car_id,)
                        )
                        if car is None:
                            print("There is no car with that ID.")
                        elif car[3] == 0:
                            print("That car is not available.")
                        else:
                            # Updates rental table
                            db_controller.execute_query(
                                f"INSERT INTO rental (customer_id, car_id) VALUES (?, ?)", (customer_id, car_id)
                            )
                            # Updates availability car table
                            db_controller.execute_query(
                                f"UPDATE car SET available = 0 WHERE car_id = ?", (car_id,)
                            )
                            print(f"{car[0]} {car[1]} {car[2]} has been rented by {customer[0]} {customer[1]}.") # make model plate, first last name
                            return


def return_rental(db_controller):
    # Calls function to list all rentals and only continue if there are rentals to return
    if list_current_rentals(db_controller) == -20:
        return
    else:
        customer_id = integer_input("Enter the ID of the customer returning the car: ")
        # First check if customer exists
        customer = db_controller.execute_single_read_query(
            f"SELECT first_name, last_name FROM customer WHERE customer_id = ?", (customer_id,)
        )
        if customer is None:
            print("There is no customer with that ID")
        else:
            # Finds the rented car
            car = db_controller.execute_single_read_query(
                f"SELECT make, model, plate FROM car WHERE car_id = (SELECT car_id FROM rental WHERE customer_id = ?)",
                (customer_id,)
            )
            if car is None:
                print("There is no car associated with that customer.")
            else:
                print(f"{car[0]} {car[1]} {car[2]} rented by {customer[0]} {customer[1]} will be returned.")
                print("1. Yes")
                print("2. No")
                user_choice = integer_input("Enter your choice: ")
                if user_choice in range(1, 3):
                    if user_choice == 2:
                        return
                    else:
                        # Update availability car table
                        db_controller.execute_query(
                            f"UPDATE car SET available = 1 WHERE car_id = (SELECT car_id FROM rental WHERE customer_id = ?)",
                            (customer_id,)
                        )
                        # Remove car from rental table
                        db_controller.execute_query(
                            f"DELETE FROM rental WHERE customer_id = ?", (customer_id,)
                        )
                else:
                    print("Your number is not in the menu range.")


def list_available_cars(db_controller):
    cars = db_controller.execute_read_query(
        f"SELECT car_id, make, model, plate FROM car WHERE available = 1", ()
    )
    if cars is None:
        print("There are no available cars.")
    else:
        print("Available cars:")
        for car in cars:
            print(f"{car[0]} {car[1]} {car[2]} {car[3]}")  # car_id make model plate


# Not working properly
def list_current_rentals(db_controller):
    # List the current rentals in rental table, list the customer's id and last name and the car's id, model and plate
    rentals = db_controller.execute_read_query(
        f"SELECT rental_id, rental_date, customer_id, car_id FROM rental NATURAL JOIN car NATURAL JOIN customer", ()
    )
    if rentals is None:
        print("There are no current rentals.")
        return -20
    else:
        print("Current rentals:")
        for rental in rentals:
            print(f"ID: {rental[0]} {rental[1]} {rental[2]} has car ID: {rental[3]} {rental[4]} {rental[5]}")
            # customer_id first_name last_name car_id model plate
