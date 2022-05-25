import sqlite3
import models.startup_database_queries as queries


class DatabaseController:
    # Initial setup of the database
    def __init__(self, path):
        try:
            self.connection = sqlite3.connect(path)
            print(f"Established connection to database.")
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(e)

        # Makes sure the tables are created/exists
        if self.connection is not None:
            try:
                self.cursor.execute(queries.create_car_table)
                self.cursor.execute(queries.create_customer_table)
                self.cursor.execute(queries.create_rental_table)
                print("Tables loaded successfully.")
            except sqlite3.Error as e:
                print(f"Error occurred while loading tables: {e}")
        else:
            print("Error! No database connection.")

    # Executes queries that requires change to the database
    def execute_query(self, query, args):
        try:
            self.cursor.execute(query, args)
            self.connection.commit()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error occurred while executing query: {e}")

    # Executes queries that does not require change to the database
    def execute_read_query(self, query, args):
        try:
            self.cursor.execute(query, args)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error occurred while executing query: {e}")

    # Execute a read only query that returns a single value
    def execute_single_read_query(self, query, args):
        try:
            self.cursor.execute(query, args)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error occurred while executing query: {e}")

    def close_connection(self):
        self.connection.close()
        print("Connection to database closed.")
