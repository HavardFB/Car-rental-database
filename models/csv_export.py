import csv
from models.date import get_date
from os.path import exists
from controllers.user_input import string_input


def csv_export_customers(db_controller):
    while True:
        file_name = string_input("Please enter the filename without extensions (or press enter to use default name): ")

        # Sets default file name
        if file_name is None:
            file_name = "customers-" + str(get_date()) + ".csv"
        # Adds .csv extension
        else:
            file_name += ".csv"

        file_path = "exports/" + file_name

        if exists(file_path):
            print("ERROR: File with that name already exists! Please try another name.")
            continue
        else:
            header = ["first_name", "last_name", "email", "phone_number", "birth_year"]

            try:
                # Opens the file and writes the rows to the file
                with open(file_path, "w+", encoding="UTF8", newline="") as file:
                    # Uses the csv writer from CSV module
                    writer = csv.writer(file)
                    writer.writerow(header)
                    # Selects the relevant columns from the table
                    for customer in db_controller.execute_read_query("SELECT first_name, last_name, email, phone_number, birth_year FROM customer", ()):
                        writer.writerow(customer)
                print("Successfully exported to file " + file_name)
                return
            except Exception:
                print(f"ERROR {Exception}: Something went wrong while writing to the file!")
                return


def csv_export_cars(db_controller):
    while True:
        file_name = string_input("Please enter the filename without extensions (or press enter to use default name): ")

        # Sets default file name
        if file_name is None:
            file_name = "cars-" + str(get_date()) + ".csv"
        # Adds .csv extension
        else:
            file_name += ".csv"

        file_path = "exports/" + file_name

        if exists(file_path):
            print("ERROR: File with that name already exists!")
            continue
        else:
            header = ["make", "model", "plate", "year", "color", "mileage"]

            try:
                # Opens the file and writes the rows to the file
                with open(file_path, "w+", encoding="UTF8", newline="") as file:
                    # Uses the csv writer from CSV module
                    writer = csv.writer(file)
                    writer.writerow(header)
                    # Selects the relevant columns from the table
                    for car in db_controller.execute_read_query("SELECT make, model, plate, year, color, mileage FROM car", ()):
                        writer.writerow(car)
                print("Successfully exported to file " + file_name)
                return
            except Exception:
                print(f"ERROR {Exception}: Something went wrong while writing to the file!")
                return


def csv_export_rental_history(db_controller):
    while True:
        file_name = string_input("Please enter the filename without extensions (or press enter to use default name): ")

        # Sets default file name
        if file_name is None:
            file_name = "rental_history-" + str(get_date()) + ".csv"
        # Adds .csv extension
        else:
            file_name += ".csv"

        file_path = "exports/" + file_name

        if exists(file_path):
            print("ERROR: File with that name already exists!")
            continue
        else:
            header = ["rental_date", "return_date", "customer_last_name", "customer_phone_number", "car_plate"]

            try:
                # Opens the file and writes the rows to the file
                with open(file_path, "w+", encoding="UTF8", newline="") as file:
                    # Uses the csv writer from CSV module
                    writer = csv.writer(file)
                    writer.writerow(header)
                    # Selects the relevant columns from the table
                    for rental in db_controller.execute_read_query("SELECT rental_date, return_date, customer_last_name, customer_phone_number, car_plate FROM rental WHERE return_date IS NOT NULL", ()):
                        writer.writerow(rental)
                print("Successfully exported to file " + file_name)
                return
            except Exception:
                print(f"ERROR {Exception}: Something went wrong while writing to the file!")
                return
