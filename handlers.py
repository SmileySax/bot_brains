from aiogram import Dispatcher, types
from create_bot import dp, Bot
from db import DB_connection
from classes import User, Object, Booking
from controller import UserController, ObjectController, BookingController


user_dict = {'name': 'Andrey',
             'role': 'student',
             'campus': 'msk',
             'login': 'hbombur',
             'tg_id': 282235964}
user_dict2 = {'type': 'meeting_room',
              'name': 'meeting_room1',
              'description': 'nice',
              'image_path': 'https://www.booking.com/hotel/cy/the-room.ru.html',
              'campus': 'msk',
              'stage': 2,
              'room': 217}
user_dict3 = {'user_id': 1,
              'object_id': 1,
              'start_time': '2022-08-19 13:00',
              'end_time': '2022-08-19 14:00',
              'status': 'active'}

u = UserController()
o = ObjectController()
b = BookingController()


async def data_base_query_book(mess:types.Message):
    db_name = 'Тест'
    b.create(user_dict3)
    conn = DB_connection.create_connection(b.db_name)
    # conn.execute("INSERT INTO Bookings (user_id, object_id, start_time, end_time, status) \
    #                  VALUES (1, 1, '2022-08-19 13:00', '2022-08-19 14:00', 'not active')")
    cursor = conn.cursor()
    answer = cursor.execute(f'SELECT * FROM Bookings')
    res = answer.fetchall()
    for result in res:
        await mess.answer(text=str(result))
    conn.close()


async def data_base_query_objects(mess:types.Message):
    o.create(user_dict2)
    conn = DB_connection.create_connection(o.db_name)
    # conn.execute("INSERT INTO Objects (type, name, description, image_path, campus, stage, room) \
    #              VALUES ('meeting_room', 'meeting_room1', 'nice', \
    #              'https://www.booking.com/hotel/cy/the-room.ru.html', 'msk', 2, 217)")
    cursor = conn.cursor()
    answer = cursor.execute(f'SELECT * FROM Objects WHERE id = 1')
    res = answer.fetchall()
    for result in res:
        await mess.answer(text=str(result))
    conn.close()

async def data_base_query_users(mess: types.Message):
    #print("user_dict types tg_id : ", type(user_dict['tg_id']))
    # conn.execute(f"INSERT INTO Users  VALUES ('Andrey', 'student', 'msk', 'hbombur', {mess.from_user.id})")
    u.create(user_dict)
    conn = DB_connection.create_connection(u.db_name)
    cursor = conn.cursor()
    answer = cursor.execute(f"SELECT * FROM Users WHERE tg_id = {user_dict['tg_id']}")
    res = answer.fetchall()
    print (f'res = {res}')
    for result in res:
        await mess.answer(text=str(result))
    conn.close()

async def data_base_query_all(mess: types.Message):
    #print("user_dict types tg_id : ", type(user_dict['tg_id']))
    # conn.execute(f"INSERT INTO Users  VALUES ('Andrey', 'student', 'msk', 'hbombur', {mess.from_user.id})")
    l = u.checkReg(282235964)
    # for book in l:
    #     print(book.id, book.end_time)
    if l:
        print (l.id)

async def data_base_del_user(mess: types.Message):
    #print("user_dict types tg_id : ", type(user_dict['tg_id']))
    # conn.execute(f"INSERT INTO Users  VALUES ('Andrey', 'student', 'msk', 'hbombur', {mess.from_user.id})")
    u.delete(1)
    conn = DB_connection.create_connection(u.db_name)
    cursor = conn.cursor()
    answer = cursor.execute(f"SELECT * FROM Users")
    res = answer.fetchall()
    print (f'res = {res}')
    for result in res:
        await mess.answer(text=str(result))
    conn.close()


def register_handlers_bot(dp: Dispatcher):
    dp.register_message_handler(data_base_query_users, commands=['u'])
    dp.register_message_handler(data_base_query_objects, commands=['o'])
    dp.register_message_handler(data_base_query_book, commands=['b'])
    dp.register_message_handler(data_base_query_all, commands=['all'])
    dp.register_message_handler(data_base_del_user, commands=['du'])