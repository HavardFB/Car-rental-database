import json
from models.date import get_date
from os.path import exists


def json_export_customers(db_controller, file_name):
    if file_name is None:
        file_name = "customers-" + str(get_date()) + ".json"
    else:
        file_name = file_name + ".json"

    file_path = "exports/" + file_name

    if exists(file_path):
        print("ERROR: File with that name already exists!")
        return -11
    else:
        with open(file_path, "w+", encoding="UTF8") as file:
            # List to contain the customers
            customers = []

            # Appends all customers to the list
            for customer in db_controller.execute_read_query("SELECT first_name, last_name, email, phone_number, birth_year FROM customer", ()):
                customers.append({"first_name": customer[0], "last_name": customer[1], "email": customer[2], "phone_number": customer[3], "birth_year": customer[4]})

            # Writes the dictionary to the file
            json_object = json.dumps(customers, indent=4, ensure_ascii=False)
            file.write(json_object)


def json_export_cars(db_controller, file_name):
    if file_name is None:
        file_name = "cars-" + str(get_date()) + ".json"
    else:
        file_name = file_name + ".json"

    file_path = "exports/" + file_name

    if exists(file_path):
        print("ERROR: File with that name already exists!")
        return -11
    else:
        with open(file_path, "w+", encoding="UTF8") as file:
            # List to contain the cars
            cars = []

            # Appends all cars to the list
            for car in db_controller.execute_read_query("SELECT make, model, plate, year, color, mileage FROM car", ()):
                cars.append({"make": car[0], "model": car[1], "plate": car[2], "year": car[3], "color": car[4], "mileage": car[5]})

            # Writes the dictionary to the file
            json_object = json.dumps(cars, indent=4, ensure_ascii=False)
            file.write(json_object)


def json_export_rental_history(db_controller, file_name):
    if file_name is None:
        file_name = "rental_history-" + str(get_date()) + ".json"
    else:
        file_name = file_name + ".json"

    file_path = "exports/" + file_name

    if exists(file_path):
        print("ERROR: File with that name already exists!")
        return -11
    else:
        with open(file_path, "w+", encoding="UTF8") as file:
            # List to contain the rental history
            rental_history = []

            # Appends all rental history to the list
            for rental in db_controller.execute_read_query("SELECT rental_date, return_date, customer_last_name, customer_phone_number, car_plate FROM rental WHERE return_date IS NOT NULL", ()):
                rental_history.append({"rental_date": rental[0], "return_date": rental[1], "customer_last_name": rental[2], "customer_phone_number": rental[3], "car_plate": rental[4]})

            # Writes the dictionary to the file
            json_object = json.dumps(rental_history, indent=4, ensure_ascii=False)
            file.write(json_object)