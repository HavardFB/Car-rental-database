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
            file.write("id,first_name,last_name,email,phone_number,birth_year\n")
            customers = db_controller.execute_read_query("SELECT customer_id, first_name, last_name, email, phone_number, birth_year FROM customer", ())
            for customer in customers:
                file.write(str(customer[0]) + "," + customer[1] + "," + customer[2] + "," + customer[3] + "," + customer[4] + "," + str(customer[5]) + "\n")

