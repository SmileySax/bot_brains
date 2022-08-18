from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self, id):
        self.id = id

    # @abstractmethod
    # def book_met(self):
    #     raise NotImplementedError(f"Необходимо переопределить метод")
    #
    # @abstractmethod
    # def get_booking(self):
    #     raise NotImplementedError("Необходимо переопределить метод")
    #
    # @abstractmethod
    # def del_booking(self):
    #     raise NotImplementedError("Необходимо переопределить метод")
    #
    # @abstractmethod
    # def get_object_list(self):
    #     raise NotImplementedError("Необходимо переопределить метод")


class User(Model):
    def __init__(self, id, name, role, campus, login, tg_id):
        super().__init__(id)
        self.name = name
        self.role = role
        self.campus = campus
        self.login = login
        self.tg_id = tg_id

    # def book_met(self):
    #     pass
    #
    # def get_booking(self):
    #     pass
    #
    # def del_booking(self):
    #     pass
    #
    # def get_object_list(self):
    #     pass


class Object(Model):
    def __init__(self, id, type_room, description, image_path, campus, floor, room):
        super().__init__(id)
        self.type_room = type_room
        self.description = description
        self.image_path = image_path
        self.campus = campus
        self.floor = floor
        self.room = room


class Booking(Model):
    def __init__(self, id, user_id, object_id, start_time, end_time, status):
        super().__init__(id)
        self.user_id = user_id
        self.object_id = object_id
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

