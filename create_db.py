import os
import sqlite3
from sqlite3 import Error

create_users = 'CREATE TABLE IF NOT EXISTS Users (' \
               'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
               'name TEXT, role TEXT, campus TEXT, ' \
               'login TEXT, tg_id BIGINT)'

create_bookings = 'CREATE TABLE IF NOT EXISTS Bookings (' \
                  'id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
                  'user_id INTEGER, object_id INTEGER, ' \
                  'start_time DATETIME, end_time DATETIME, status TEXT)'

create_objects = 'CREATE TABLE IF NOT EXISTS Objects (' \
                 'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                 'type TEXT, name TEXT, description TEXT, ' \
                 'image_path TEXT, campus TEXT,' \
                 'stage INTEGER, room INTEGER)'


def create_db(db_file):
    """ create a database connection to a SQLite database """

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(create_users)
        conn.commit()
        cursor.execute(create_objects)
        conn.commit()
        cursor.execute(create_bookings)
        conn.commit()
    except Error as e:
        print(e)
    return conn

