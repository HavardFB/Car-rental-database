from models.date import get_date
from os.path import exists

def csv_export_customers(db_controller, file_name):
    if file_name is None:
        file_name = "customers-" + str(get_date()) + ".csv"
    else:
        file_name += ".csv"

    file_path = "exports/" + file_name

    if exists(file_path):
        print("ERROR: File with that name already exists!")
        return -11
    else:
        # Opens the file and reads the columns into a customers list
        with open(file_path, "w+") as file:
            file.write("first_name,last_name,email,phone_number,birth_year\n")
            customers = db_controller.execute_read_query("SELECT first_name, last_name, email, phone_number, birth_year FROM customer", ())
            for customer in customers:
                file.write(customer[0] + "," + customer[1] + "," + customer[2] + "," + customer[3] + "," + str(customer[4]) + "\n")


def csv_export_cars(db_controller, file_name):
    if file_name is None:
        file_name = "cars-" + str(get_date()) + ".csv"
    else:
        file_name += ".csv"

    file_path = "exports/" + file_name

    if exists(file_path):
        print("ERROR: File with that name already exists!")
        return -11
    else:
        # Opens the file and reads the columns into a customers list
        with open(file_path, "w+") as file:
            file.write("make,model,plate,year,color,mileage\n")
            cars = db_controller.execute_read_query("SELECT make, model, plate, year, color, mileage FROM car", ())
            for car in cars:
                file.write(car[0] + "," + car[1] + "," + car[2] + "," + str(car[3]) + "," +car[4] + "," + str(car[5]) + "\n")
