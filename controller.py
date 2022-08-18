from abc import ABC, ABCMeta, abstractmethod
from db import DB_connection
from classes import User, Booking, Object
import sqlite3


class AbstractController(ABC):
    db_name = 'Тест'

    @abstractmethod
    def create(self):
        raise NotImplementedError(f"Необходимо переопределить метод")

    @abstractmethod
    def getById(self, id):
        raise NotImplementedError(f"Необходимо переопределить метод")

    @abstractmethod
    def delete(self, Model):
        raise NotImplementedError(f"Необходимо переопределить метод")


class ObjectController(AbstractController):
    'Контроллер объектов'

    def getById(self, id):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM Objects WHERE id = {id}")
        object = Object(*cursor.fetchone())
        connect.close()
        return object

    def delete(self, Object):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        cursor.execute(f"DELETE FROM Users WHERE id = {Object.id}")
        connect.commit()
        connect.close()

    def create(self, object_data):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        cursor.execute(f"INSERT INTO Objects (type, name, description, image_path, campus, stage, room) VALUES ( \
            '{object_data['type']}', \
            '{object_data['name']}', \
            '{object_data['description']}', \
            '{object_data['image_path']}', \
            '{object_data['campus']}', \
            {object_data['stage']}, \
            {object_data['room']})")
        connect.commit()
        connect.close()


class UserController(AbstractController):
    'Контроллер пользователей'

    def getById(self, id):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM Users WHERE id = {id}")
        user = User(*cursor.fetchone())
        connect.close()
        return user

    def delete(self, user_id):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        cursor.execute(f"DELETE FROM Users WHERE id = {user_id}")
        connect.commit()
        connect.close()

    def create(self, user_data):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        cursor.execute(f"INSERT INTO Users (name, role, campus, login, tg_id) VALUES ( \
            '{user_data['name']}', \
            '{user_data['role']}', \
            '{user_data['campus']}', \
            '{user_data['login']}', \
            {user_data['tg_id']})")
        connect.commit()
        connect.close()

    def checkReg(self, tg_id):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        id = cursor.execute(f"SELECT id FROM Users WHERE tg_id = {tg_id}").fetchone()
        if not id:
            return None
        return self.getById(*id)


class BookingController(AbstractController):
    'Контроллер броней'
    def getById(self, id):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM Bookings WHERE id = {id}")
        booking = Booking(*cursor.fetchone())
        connect.close()
        return booking

    def delete(self, Booking):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        cursor.execute(f"UPDATE Bookings SET status = 'not active' WHERE id = {Booking.id} AND status = 'active'")
        connect.commit()
        connect.close()

    def create(self, book_data):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        cursor.execute(f"INSERT INTO Bookings (user_id, object_id, start_time, end_time, status) VALUES (\
            {book_data['user_id']}, \
            {book_data['object_id']}, \
            '{book_data['start_time']}', \
            '{book_data['end_time']}', \
            '{book_data['status']}')")
        connect.commit()
        connect.close()

    def getAllForUser(self, user_id):
        connect = DB_connection.create_connection(self.db_name)
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM Bookings WHERE user_id = {user_id} AND status = 'active'")
        all_book = cursor.fetchall()
        print(all_book)
        connect.close()
        bookings = []
        for book in all_book:
            bookings.append(Booking(*book))
        return bookings

    #   работает неправильно
    # def getAllAvailable(self, type, campus):
    #     connect = DB_connection.create_connection(self.db_name)
    #     cursor = connect.cursor()
    #     cursor.execute(f"SELECT * FROM Bookings WHERE type = {type} AND campus = {campus}")
    #     all_book = cursor.fetchall()
    #     connect.close()
    #     bookings = []
    #     for book in all_book:
    #         bookings.append(Booking(*book))
    #     return bookings
