from sys import exit as sys_exit
from view.menu_screens import main_menu
from controllers.database_controller import DatabaseController


if __name__ == "__main__":
    # Creates an instance of the DatabaseController
    db_controller = DatabaseController(r"database\car-rental.db")

    # Calls the main menu screen function
    main_menu(db_controller)

    # Exiting the program
    db_controller.close_connection()
    sys_exit()
