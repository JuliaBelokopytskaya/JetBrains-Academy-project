'''Создать класс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
Создать список объектов. Вывести:
a)    список рейсов для заданного пункта назначения;
b)    список рейсов для заданного дня недели;.'''
class Airline:
    default_flight_id = '-'
    default_destination= 'No destination'
    default_aircraft_type= '-'
    default_lead_time = 'No time'
    default_days = '-'

    def __init__(self, id, point, type, time, day):
        self.__flight_id = id
        self.__destination = point
        self.__aircraft_type = type
        self.__lead_time= time
        self.__days= day
        # print('New object created!')

    def get_flight_id(self):
        return self.__flight_id 

    def get_destination(self):
        return self.__destination 

    def get_aircraft_type(self):
        return self.__aircraft_type

    def get_lead_time(self):
        return self.__lead_time

    def get_days(self):
        return self.__days
