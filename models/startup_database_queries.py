create_cars_table = """ CREATE TABLE IF NOT EXISTS cars (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        make TEXT NOT NULL,
                        model TEXT NOT NULL,
                        plate TEXT NOT NULL,
                        year INTEGER NOT NULL,
                        color TEXT NOT NULL,
                        mileage INTEGER NOT NULL
                        );"""

create_customers_table = """ CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone_number TEXT NOT NULL,
                        birth_year INTEGER NOT NULL
                        );"""