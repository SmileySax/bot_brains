import sqlite3
from sqlite3 import Error
import os
import create_db


def check_db(file_name):
    return os.path.exists(file_name)


class   DB_connection():
    def create_connection(db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            print("DB_connection / db_file", type(db_file))
            if check_db(db_file):
                conn = sqlite3.connect(db_file)
                print("step 1\n")
            else:
                conn = create_db.create_db(db_file)
                print("step 2\n")
            print(sqlite3.version)
        except Error as e:
            print(e)
        return conn
