from controllers.user_input import integer_input, plate_input
from models.customer_functions import list_customers
from models.car_functions import list_available_cars
from models.date import get_date


def add_rental(db_controller):
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
                            today = get_date()
                            # Updates rental table
                            db_controller.execute_query(
                                f"INSERT INTO rental (customer_id, car_id, rental_date) VALUES (?, ?, ?)", (customer_id, car_id, today)
                            )
                            # Updates availability car table
                            db_controller.execute_query(
                                f"UPDATE car SET available = 0 WHERE car_id = ?", (car_id,)
                            )
                            print(f"{car[0]} {car[1]} {car[2]} has been rented by {customer[0]} {customer[1]}.") # make model plate, first last name
                            return


def return_rental(db_controller):
    # Calls function to list all rentals and only continue if there are rentals to return
    if list_current_rentals(db_controller) == -10:
        return
    else:
        while True:
            customer_id = integer_input("Enter the ID of the customer returning the car (leave blank to cancel): ")
            if customer_id is None:
                return
            else:
                # First check if customer exists
                customer = db_controller.execute_single_read_query(
                    f"SELECT first_name, last_name FROM customer WHERE customer_id = ?", (customer_id,)
                )
                if customer is None:
                    print("There is no customer with that ID")
                else:
                    # Finds the rented car(s)
                    cars = db_controller.execute_read_query(
                        f"SELECT make, model, plate FROM car WHERE car_id IN (SELECT car_id FROM rental WHERE customer_id = ?)",
                        (customer_id,)
                    )
                    if len(cars) == 0:
                        print("There is no car associated with that customer.")
                    else:
                        print(f"{customer[0]} {customer[1]} has rented the following car(s):")
                        print(f"Make | Model | Plate")
                        for car in cars:
                            print(f"{car[0]} {car[1]} {car[2]}")

                        while True:
                            plate_num = plate_input("Please enter the plate number of the car to be returned (leave blank to cancel): ")
                            if plate_num is None:
                                return
                            else:
                                car_id = db_controller.execute_single_read_query(
                                    f"SELECT car_id FROM car WHERE plate = ?", (plate_num,)
                                )
                                if car_id is None:
                                    print("There is no rented car with that plate number.")
                                else:
                                    print(f"Are you sure car with plate {plate_num} is being returned?")
                                    print("1. Yes")
                                    print("2. No")
                                    user_choice = integer_input("Enter your choice: ")
                                    if user_choice in range(1, 3):
                                        if user_choice == 2:
                                            return
                                        else:
                                            today = get_date()
                                            # Update availability car table
                                            db_controller.execute_query(
                                                f"UPDATE car SET available = 1 WHERE car_id = (SELECT car_id FROM rental WHERE customer_id = ?)",
                                                (customer_id,)
                                            )
                                            # Sets return date
                                            db_controller.execute_query(
                                                f"UPDATE rental SET return_date = ? WHERE customer_id = ? AND car_id = ?",
                                                (today, customer_id, car_id[0])
                                            )
                                            return
                                    else:
                                        print("Your number is not in the menu range.")



def list_current_rentals(db_controller):
    rentals = db_controller.execute_read_query(
        f"SELECT customer.customer_id, customer.last_name, car.car_id, car.make, car.model, car.plate FROM customer, car, rental WHERE customer.customer_id = rental.customer_id AND car.car_id = rental.car_id AND rental.return_date IS NULL", ()
    )
    if len(rentals) == 0:
        print("There are no rentals.")
        return -10
    else:
        print("CURRENT RENTALS: ")
        print("Customer ID | Last Name | Car ID | Make | Model | Plate")
        for rental in rentals:
            print(f"{rental[0]} {rental[1]} {rental[2]} {rental[3]} {rental[4]} {rental[5]}")
        return
