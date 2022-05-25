from controllers.user_input import integer_input, plate_input
from models.customer_functions import list_customers
from models.car_functions import list_available_cars
from models.date import get_date


def add_rental(db_controller):
    # Returns if there are no customers
    if list_customers(db_controller) == -10:
        return
    else:
        # Loops until valid input is given
        while True:
            customer_id = integer_input(
                "Enter the customer's ID (leave blank to cancel): "
            )
            # Returns on cancel
            if customer_id is None:
                return
            # First check if customer exists
            customer = db_controller.execute_single_read_query(
                f"SELECT first_name, last_name, phone_number FROM customer WHERE customer_id = ?",
                (customer_id)
            )
            if customer is None:
                print("There is no customer with that ID")
                continue
            else:
                # Returns if there are no available cars
                if list_available_cars(db_controller) == -10:
                    return
                else:
                    # Loops until valid input is given
                    while True:
                        car_id = integer_input(
                            "Enter the car's ID (leave blank to cancel): "
                        )
                        # Returns on cancel
                        if car_id is None:
                            return

                        # Retrieves car from database
                        car = db_controller.execute_single_read_query(
                            f"SELECT make, model, plate, available FROM car WHERE car_id = ?",
                            (car_id)
                        )
                        # Check if car exists
                        if car is None:
                            print("There is no car with that ID.")
                            continue
                        # Checks if it is available
                        elif car[3] == 0:
                            print("That car is not available.")
                            continue
                        else:
                            today = get_date()
                            # Updates rental table
                            db_controller.execute_query(
                                f"INSERT INTO rental (customer_id, car_id, customer_last_name, "
                                f"customer_phone_number, car_plate, rental_date) VALUES (?, ?, ?, ?, ?, ?)",
                                (
                                    customer_id,
                                    car_id,
                                    customer[1],
                                    customer[2],
                                    car[2],
                                    today
                                )
                            )
                            # Updates availability car table
                            db_controller.execute_query(
                                f"UPDATE car SET available = 0 WHERE car_id = ?", (car_id)
                            )
                            print(
                                f"{car[0]} {car[1]} {car[2]} has been rented by {customer[0]} {customer[1]}."
                            )  # make model plate, first last name
                            return


def return_rental(db_controller):
    # Calls function to list all rentals and only continue if there are rentals to return
    if list_current_rentals(db_controller) == -10:
        return
    else:
        # Loops until valid input is given
        while True:
            customer_id = integer_input(
                "Enter the ID of the customer returning the car (leave blank to cancel): "
            )
            # Returns if user want to cancel
            if customer_id is None:
                return
            else:
                # Gets customer from database
                customer = db_controller.execute_single_read_query(
                    f"SELECT first_name, last_name FROM customer WHERE customer_id = ?",
                    (customer_id)
                )
                # Checks if customer exists
                if customer is None:
                    print("There is no customer with that ID")
                    continue
                else:
                    # Finds the rented car(s)
                    cars = db_controller.execute_read_query(
                        f"SELECT make, model, plate FROM car WHERE car_id IN "
                        f"(SELECT car_id FROM rental WHERE customer_id = ?) AND available = 0",
                        (customer_id)
                    )
                    if len(cars) == 0:
                        print("There is no car associated with that customer.")
                        continue
                    else:
                        print(
                            f"{customer[0]} {customer[1]} has rented the following car(s):"
                        )
                        print("---------------------------------------------------")
                        print(f"Make | Model | Plate")
                        for car in cars:
                            print(f"{car[0]} {car[1]} {car[2]}")
                        print("---------------------------------------------------")

                        # Loop to keep asking for input until valid input is given (or user cancels)
                        while True:
                            plate_num = plate_input(
                                "Please enter the plate number of the car to be returned (leave blank to cancel): "
                            )
                            # Returns on cancel
                            if plate_num is None:
                                return
                            # Checks if the plate number belongs to a car rented by that customer
                            elif plate_num not in [car[2] for car in cars]:
                                print(
                                    "Customer has not rented a car with that plate number."
                                )
                            else:
                                # Selects the car that has the same plate number as the user input
                                car = db_controller.execute_single_read_query(
                                    f"SELECT car_id, mileage FROM car WHERE plate = ?", (plate_num)
                                )
                                if car is None:
                                    print(
                                        "There is no rented car with that plate number."
                                    )
                                    continue
                                else:
                                    print(
                                        f"Are you sure car with plate {plate_num} is being returned?"
                                    )
                                    print("1. Yes")
                                    print("2. No")
                                    user_choice = integer_input("Enter your choice: ")
                                    if user_choice in range(1, 3):
                                        if user_choice == 2:
                                            return
                                        else:
                                            # Updates the new mileage
                                            print("The cars old milage is: ", car[1])
                                            mileage = integer_input(
                                                "Please enter the new mileage: "
                                            )
                                            # Mileage has to be greater than the old mileage
                                            while mileage <= car[1]:
                                                print(
                                                    "You cannot enter a mileage that is less than the old mileage."
                                                )
                                                mileage = integer_input(
                                                    "Please enter the new mileage: "
                                                )

                                            today = get_date()

                                            # Update car table
                                            db_controller.execute_query(
                                                f"UPDATE car SET available = 1, mileage = ? WHERE car_id = ?",
                                                (mileage, car[0])
                                            )
                                            # Sets return date
                                            db_controller.execute_query(
                                                f"UPDATE rental SET return_date = ? "
                                                f"WHERE customer_id = ? AND car_id = ?",
                                                (today, customer_id, car[0])
                                            )
                                            return
                                    else:
                                        print("Your number is not in the menu range.")
                                        continue


def list_current_rentals(db_controller):
    # Retrieves rentals from database
    rentals = db_controller.execute_read_query(
        f"SELECT customer.customer_id, customer.last_name, car.car_id, car.make, car.model, car.plate "
        f"FROM customer, car, rental WHERE customer.customer_id = rental.customer_id "
        f"AND car.car_id = rental.car_id AND rental.return_date IS NULL", ()
    )
    # Returns -10 if there are no rentals
    if len(rentals) == 0:
        print("There are no rentals.")
        return -10
    else:
        print("CURRENT RENTALS: ")
        print("---------------------------------------------------")
        print("Customer ID | Last Name | Car ID | Make | Model | Plate")
        for rental in rentals:
            print(
                f"{rental[0]} | {rental[1]} {rental[2]} {rental[3]} {rental[4]} {rental[5]}"
            )
        print("---------------------------------------------------")
        return
