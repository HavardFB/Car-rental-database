import sqlite3
import models.database_queries as queries


class DatabaseController:
    # Initial setup of the database
    def __init__(self, path):
        try:
            self.connection = sqlite3.connect(path)
            print(f"Established connection to database.")
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(e)

        # Makes sure the tables are created/exist
        if self.connection is not None:
            try:
                self.cursor.execute(queries.create_cars_table)
                self.cursor.execute(queries.create_customers_table)
                print("Tables loaded successfully.")
            except sqlite3.Error as e:
                print(e)
        else:
            print("Error! No database connection.")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error occurred while executing query: {e}")

    def execute_read_query(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error occurred while executing query: {e}")

    def execute_single_read_query(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error occurred while executing query: {e}")

    def close_connection(self):
        self.connection.close()
        print("Connection to database closed.")
