# Задание 1
'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
import time
class TrafficLight:
    __color = ['red', 'yellow', 'green', 'yellow']
    # можно удалить последний элемент, если должен быть порядок красный-желтый-зеленый, красный-желтый-зеленый...


    def running(self):
        i = 0 #count for testing
        while True:
            for el in self.__color:
                print(el)
                if el == 'yellow':
                    time.sleep(2)
                elif el == 'red':
                    time.sleep(7)
                elif el == 'green':
                    time.sleep(4)
            i += 1
            if i > 3:
                break


traffic_light = TrafficLight()
traffic_light.running()
# Задание 2
'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road:

    
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def asphaltMassCalc(self):
        thickness = 5
        mass_for_cm_thick_per_m = 25
        asphalt_mass = int(self._length) * int(self._width) * mass_for_cm_thick_per_m * thickness / 1000
        print(f'mass of asphalt is {asphalt_mass} t')


road = Road(5000, 20)
road.asphaltMassCalc()
# Задание 3
'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage' : wage, 'bonus' : bonus}


class Position(Worker):


    def get_full_name(self):
        print(f'full name - {self.name} {self.surname}')

    
    def get_total_income(self):
        total = self._income.get('wage') + self._income.get('bonus') 
        print(f'total income - {total}')


worker1 = Position('Ivan', 'Petrov', 'admin', 30000, 10000)
worker1.get_full_name()
worker1.get_total_income()
worker2 = Position('Petr', 'Ivanov', 'cleaning', 35000, 9000)
worker2.get_full_name()
worker2.get_total_income()
# Задание 4
'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print(f'{self.name} started moving')
    

    def stop(self):
        print(f'{self.name} stopped moving')
    

    def turn(self, direction):
        print(f'{self.name} turned {direction}')


    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')


    def check_police(self):
        if self.is_police == True:
            print(f'{self.name} is police car')
        else:
            print(f'{self.name} is civil car')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police


    def show_speed(self):
        town_car_speed_limit = 60
        if self.speed > town_car_speed_limit:
            print(f'{self.name} is driving {self.speed - town_car_speed_limit} km/h above speed limit!')
        else:
            Car.show_speed(self)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    
    def climate_control(self):
        print('climate control is on')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police


    sirens = False


    def turn_sirens(self):
        if self.sirens == False:
            print(f'{self.name} turned sirens on')
            self.sirens = True
        else:
            print(f'{self.name} turned sirens off')
            self.sirens = False


    
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police


    def show_speed(self):
        work_car_speed_limit = 40
        if self.speed > work_car_speed_limit:
            print(f'{self.name} is driving {self.speed - work_car_speed_limit} km/h above speed limit!')
        else:
            Car.show_speed(self)


car1 = TownCar(80, 'black', 'Mazda')
car1.show_speed()
car1.stop()
car2 = WorkCar(45, 'orange', 'KAMAZ')
car2.show_speed()
car3 = TownCar(50, 'white', 'Lada')
car3.turn('left')
car3.show_speed()
car4 = PoliceCar(90, 'blue', 'BMW')
car4.check_police()
car4.turn_sirens()
car4.turn_sirens()
# Задание 5
'''
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('start draw')
    
class Pen(Stationery):


    def draw(self):
        print(f'start draw  with {self.title}')


class Pencil(Stationery):


    def draw(self):
        print(f'start draw  with {self.title}')


class Handle(Stationery):


    def draw(self):
        print(f'start draw  with {self.title}')


pencil = Pencil('pencil')
pencil.draw()
pen = Pen('pen')
pen.draw()
handle = Handle('handle')
handle.draw()
