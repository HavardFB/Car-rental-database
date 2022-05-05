from controllers.user_input import string_input
from controllers.user_input import integer_input


def add_car(db_controller):
    make = string_input("Enter the make of the car: ")
    model = string_input("Enter the model of the car: ")
    plate = string_input("Enter the plate of the car: ")
    year = integer_input("Enter the year of the car: ")
    color = string_input("Enter the color of the car: ")
    mileage = integer_input("Enter the mileage of the car: ")

    # Inserting data this way to ensure fields are inserted as data and not commands
    db_controller.execute_query(
        f"INSERT INTO car (make, model, plate, year, color, mileage)VALUES (?, ?, ?, ?, ?, ?)",
        (make, model, plate, year, color, mileage)
    )


def edit_car(db_controller):
    car_id = integer_input("Enter the ID of the car you want to edit: ")
    # First check if it exists
    car = db_controller.execute_single_read_query(f"SELECT make, model, plate FROM car WHERE id = ?", (car_id,))
    if car is None:
        print("There is no car with that ID.")
    else:
        make = string_input("Enter the new make of the car: ")
        model = string_input("Enter the new model of the car: ")
        plate = string_input("Enter the new plate of the car: ")
        year = integer_input("Enter the new year of the car: ")
        color = string_input("Enter the new color of the car: ")
        mileage = integer_input("Enter the new mileage of the car: ")

        db_controller.execute_query(
            f"UPDATE car SET make = ?, model = ?, plate = ?, "
            f"year = ?, color = ?, mileage = ? WHERE id = ?",
            (make, model, plate, year, color, mileage, car_id)
        )


def remove_car(db_controller):
    car_id = integer_input("Enter the ID of the car you want to remove: ")
    # First check if it exists
    car = db_controller.execute_single_read_query(f"SELECT make, model, plate, year FROM car WHERE id = ?", (car_id,))
    if car is None:
        print("There is no car with that ID.")
    else:
        db_controller.execute_query(f"DELETE FROM car WHERE id = ?", (car_id,))
        print(f"Deleted {car[3]} model {car[0]} {car[1]}, {car[2]}.")    # year, make, model, plate
