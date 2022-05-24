import csv
from models.date import get_date
from os.path import exists

def csv_export_customers(db_controller, file_name):
    # Sets default file name
    if file_name is None:
        file_name = "customers-" + str(get_date()) + ".csv"
    else:
        file_name += ".csv"

    file_path = "exports/" + file_name

    if exists(file_path):
        print("ERROR: File with that name already exists!")
        return -11
    else:
        header = ["first_name", "last_name", "email", "phone_number", "birth_year"]

        # Opens the file and writes the rows to the file
        with open(file_path, "w+", encoding="UTF8", newline="") as file:
            # Uses the csv writer from CSV module
            writer = csv.writer(file)
            writer.writerow(header)
            # Selects the relevant columns from the table
            for customer in db_controller.execute_read_query("SELECT first_name, last_name, email, phone_number, birth_year FROM customer", ()):
                writer.writerow(customer)


def csv_export_cars(db_controller, file_name):
    # Sets default file name
    if file_name is None:
        file_name = "cars-" + str(get_date()) + ".csv"
    else:
        file_name += ".csv"

    file_path = "exports/" + file_name

    if exists(file_path):
        print("ERROR: File with that name already exists!")
        return -11
    else:
        header = ["make", "model", "plate", "year", "color", "mileage"]

        # Opens the file and writes the rows to the file
        with open(file_path, "w+", encoding="UTF8", newline="") as file:
            # Uses the csv writer from CSV module
            writer = csv.writer(file)
            writer.writerow(header)
            # Selects the relevant columns from the table
            for car in db_controller.execute_read_query("SELECT make, model, plate, year, color, mileage FROM car", ()):
                writer.writerow(car)


def csv_export_rental_history(db_controller, file_name):
    # Sets default file name
    if file_name is None:
        file_name = "rental_history-" + str(get_date()) + ".csv"
    else:
        file_name += ".csv"

    file_path = "exports/" + file_name

    if exists(file_path):
        print("ERROR: File with that name already exists!")
        return -11
    else:
        header = ["rental_date", "return_date", "customer_last_name", "customer_phone_number", "car_plate"]

        # Opens the file and writes the rows to the file
        with open(file_path, "w+", encoding="UTF8", newline="") as file:
            # Uses the csv writer from CSV module
            writer = csv.writer(file)
            writer.writerow(header)
            # Selects the relevant columns from the table
            for rental in db_controller.execute_read_query("SELECT rental_date, return_date, customer_last_name, customer_phone_number, car_plate FROM rental WHERE return_date IS NOT NULL", ()):
                writer.writerow(rental)