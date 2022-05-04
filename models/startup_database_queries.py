create_car_table = """ CREATE TABLE IF NOT EXISTS car (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        make TEXT NOT NULL,
                        model TEXT NOT NULL,
                        plate TEXT NOT NULL,
                        year INTEGER NOT NULL,
                        color TEXT NOT NULL,
                        mileage INTEGER NOT NULL,
                        availability INTEGER NOT NULL
                        );"""

create_customer_table = """ CREATE TABLE IF NOT EXISTS customer (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone_number TEXT NOT NULL,
                        birth_year INTEGER NOT NULL
                        );"""