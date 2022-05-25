from controllers.user_input import string_input
from controllers.user_input import integer_input
from controllers.user_input import plate_input


def add_car(db_controller):
    make = string_input("Enter the make of the car (leave blank to cancel): ")
    if make is None:
        return
    model = string_input("Enter the model of the car (leave blank to cancel): ")
    if model is None:
        return
    plate = plate_input("Enter the plate of the car (leave blank to cancel): ")
    if plate is None:
        return
    year = integer_input("Enter the year of the car (leave blank to cancel): ")
    if year is None:
        return
    color = string_input("Enter the color of the car (leave blank to cancel): ")
    if color is None:
        return
    mileage = integer_input("Enter the mileage of the car (leave blank to cancel): ")
    if mileage is None:
        return

    # Inserting data this way to ensure fields are inserted as data and not commands
    db_controller.execute_query(
        f"INSERT INTO car (make, model, plate, year, color, mileage) VALUES (?, ?, ?, ?, ?, ?)",
        (make, model, plate, year, color, mileage),
    )


# Normally cars shouldn't be edited, but this function allows for editing all the fields of the car in case it gets
# a new paint job, a new plate or something was wrong with the initial input when adding the car.
def edit_car(db_controller):
    if list_cars(db_controller) == -10:
        return

    while True:
        car_id = integer_input(
            "Enter the ID of the car you want to edit (leave blank to cancel): "
        )
        if car_id is None:
            return
        else:
            # First check if it exists
            car = db_controller.execute_single_read_query(
                f"SELECT make, model, plate FROM car WHERE car_id = ?", (car_id,)
            )
            if car is None:
                print("There is no car with that ID.")
            else:
                make = string_input(
                    "Enter the new make of the car (leave blank to cancel): "
                )
                if make is None:
                    return
                model = string_input(
                    "Enter the new model of the car (leave blank to cancel): "
                )
                if model is None:
                    return
                plate = plate_input(
                    "Enter the new plate of the car (leave blank to cancel): "
                )
                if plate is None:
                    return
                year = integer_input(
                    "Enter the new year of the car (leave blank to cancel): "
                )
                if year is None:
                    return
                color = string_input(
                    "Enter the new color of the car (leave blank to cancel): "
                )
                if color is None:
                    return
                mileage = integer_input(
                    "Enter the new mileage of the car (leave blank to cancel): "
                )
                if mileage is None:
                    return

                # Updates the car table
                db_controller.execute_query(
                    f"UPDATE car SET make = ?, model = ?, plate = ?, "
                    f"year = ?, color = ?, mileage = ? WHERE car_id = ?",
                    (make, model, plate, year, color, mileage, car_id),
                )
                # Updates the rental table with new car_plate
                db_controller.execute_query(
                    f"UPDATE rental SET car_plate = ? WHERE car_id = ?", (plate, car_id)
                )
                return


def remove_car(db_controller):
    if list_cars(db_controller) == -10:
        return

    while True:
        car_id = integer_input(
            "Enter the ID of the car you want to remove (leave blank to cancel): "
        )
        if car_id is None:
            return
        else:
            # First check if it exists
            car = db_controller.execute_single_read_query(
                f"SELECT make, model, plate, year FROM car WHERE car_id = ?", (car_id,)
            )
            if car is None:
                print("There is no car with that ID.")
                return
            # Checks if the car is rented
            elif (
                db_controller.execute_single_read_query(
                    f"SELECT car_id FROM car WHERE car_id = ? AND available = 1",
                    (car_id,),
                )
                is None
            ):
                print(
                    "The car is currently rented. It has to be returned before it can be removed."
                )
                return
            else:
                # Deletes the car from the car table
                db_controller.execute_query(
                    f"DELETE FROM car WHERE car_id = ?", (car_id,)
                )
                print(
                    f"Deleted {car[3]} model {car[0]} {car[1]}, {car[2]}."
                )  # year, make, model, plate
                # Deletes the history from the rental table to keep the database clean.
                db_controller.execute_query(
                    f"DELETE FROM rental WHERE car_id = ?", (car_id,)
                )
                return


def list_cars(db_controller):
    cars = db_controller.execute_read_query(
        f"SELECT car_id, make, model, plate, year, color, mileage FROM car", ()
    )
    if cars:
        print("Owned cars:")
        print("---------------------------------------------------")
        print("ID\t| Make | Model | Plate | Year | Color | Mileage")
        for car in cars:
            print(f"{car[0]}\t{car[1]} {car[2]} {car[3]} {car[4]} {car[5]} {car[6]}")
        print("---------------------------------------------------")
    else:
        print("There is no cars in the database.")
        return -10


def list_available_cars(db_controller):
    cars = db_controller.execute_read_query(
        f"SELECT car_id, make, model, plate FROM car WHERE available = 1", ()
    )
    if cars:
        print("Available cars: ")
        print("---------------------------------------------------")
        print("ID\t| Make | Model | Plate")
        for car in cars:
            print(f"{car[0]}\t{car[1]} {car[2]} {car[3]}")
        print("---------------------------------------------------")
    else:
        print("There are no available cars.")
        return -10


# This is not a very efficient way to search (everything is partial search), but considering this program is for
# a small car rental company it is highly unlikely the database will get extremely large. Therefore the user is
# prioritized and the program will allow partial searches for more results.
def search_car(db_controller, search_query):
    cars = db_controller.execute_read_query(
        f"SELECT car_id, make, model, plate, year, color, mileage, available FROM car "
        f"WHERE make LIKE ('%' || ? || '%') OR model LIKE ('%' || ? || '%') OR plate LIKE ('%' || ? || '%') OR "
        f"color LIKE ('%' || ? || '%') OR year LIKE ('%' || ? || '%') OR mileage LIKE ('%' || ? || '%')",
        (search_query, search_query, search_query, search_query, search_query, search_query)
    )
    if len(cars) == 0:
        print("Match not found.")
        return
    else:
        print("Match found:")
        print("---------------------------------------------------")
        print("ID | Make Model | Plate | Year | Color | Mileage | Available")
        available = ""
        for car in cars:
            if car[7] == 1:
                available = "Yes"
            elif car[7] == 0:
                available = "No"
            print(
                f"{car[0]}: {car[1]} {car[2]} | {car[3]} | {car[4]} | {car[5]} | {car[6]} | {available}"
            )
        print("---------------------------------------------------")
        return
