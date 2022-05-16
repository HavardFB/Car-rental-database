create_car_table = """ CREATE TABLE IF NOT EXISTS car (
                        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        make TEXT NOT NULL,
                        model TEXT NOT NULL,
                        plate TEXT NOT NULL,
                        year INTEGER NOT NULL,
                        color TEXT NOT NULL,
                        mileage INTEGER NOT NULL,
                        available BOOLEAN DEFAULT TRUE NOT NULL
                        );"""

create_customer_table = """ CREATE TABLE IF NOT EXISTS customer (
                        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone_number TEXT NOT NULL,
                        birth_year INTEGER NOT NULL
                        );"""

create_rental_table = """ CREATE TABLE IF NOT EXISTS rental (
                        rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        rental_date DATE,
                        return_date DATE,
                        customer_id INTEGER,
                        car_id INTEGER,
                        FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
                        FOREIGN KEY (car_id) REFERENCES car(car_id)
                        );"""
