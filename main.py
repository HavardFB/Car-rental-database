import sys

from view.menu_screens import main_menu
from controllers.database_controller import DatabaseController


if __name__ == "__main__":
    db_controller = DatabaseController(r"database\car-rental.db")
    main_menu(db_controller)
    db_controller.close_connection()
    sys.exit()
