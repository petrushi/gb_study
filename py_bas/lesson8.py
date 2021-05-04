""" Задание 1
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_day_month_year(cls, self):
        day = int(self.date[0:self.date.find('-')])
        month = int(self.date[self.date.find('-') + 1:self.date.rfind('-')])
        year = int(self.date[self.date.rfind('-') + 1:])
        return day, month, year

    @staticmethod
    def check_date_validity(self):
        if 0 < self.get_day_month_year(self)[0] < 32 \
            and 0 < self.get_day_month_year(self)[1] < 12 \
                and 0 < self.get_day_month_year(self)[2]:
            print('date is valid')
        else:
            print('input date is invalid!')


date1 = Date('12-3-1974')
print(date1.date)
print(date1.get_day_month_year(date1))
print(date1.check_date_validity(date1))
date2 = Date('32-03-2006')
print(date1.check_date_validity(date2))

""" Задание 2
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivideByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


denominator = input("input denominator: ")
divider = input("input divider")
try:
    denominator = float(denominator)
    divider = float(divider)
    if divider == 0:
        raise DivideByZero("you trying to divide by zero!")
except ValueError:
    print("input must be 2 numbers")
except DivideByZero as err:
    print(err)
else:
    print(f"answer is - {denominator/divider}")

""" Задание 3
Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class OnlyDigits(Exception):
    def __init__(self, *args):
        self.user_list = []
        while True:
            el = input('input number to add to list, stop to exit - ')
            if el == 'stop':
                print(self.user_list)
                break
            try:
                el = int(el)
                self.user_list.append(el)
                print(f'current list - {self.user_list} \n ')
            except ValueError:
                print('input must be number!')


list_1 = OnlyDigits()

""" Задания 4, 5, 6
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
родолжить работу над вторым заданием.

Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class OfficeWareHouse:
    def __init__(self, space):
        self.space = space


class OfficeEquipment:
    def __init__(self, name: str, price: int, amount: int):
        self.name = name
        self.price = price
        self.amount = amount
        self.info = {'name': self.name, 'price': self.price, 'amount': self.amount}
        self.total = []

    def space_left(self, other):
        return 500 - self.amount

    def total_cost(self):
        return self.price * self.amount

    def reception(self):
        try:
            name = input(f'Введите наименование ')
            price = int(input(f'Введите цену за ед '))
            amount = int(input(f'Введите количество '))
            unique = {'Модель устройства': name, 'Цена за ед': price, 'Количество': amount}
            self.info.update(unique)
            self.total.append({self.name:amount})
            print(f'Текущий список -\n {self.total}')
        except:
            return f'Ошибка ввода данных'


class Printers(OfficeEquipment):
    def __init__(self, name, price, amount, cartridges_left):
        super().__init__(name, price, amount)
        self.cartridges_left = cartridges_left

    def pages_able_to_print(self):
        return self.cartridges_left * 279


class Scanners(OfficeEquipment):
    def __init__(self, name, price, amount):
        super().__init__(name, price, amount)


class Xerox(OfficeEquipment):
    def __init__(self, name, price, amount):
        super().__init__(name, price, amount)


unit_1 = Printers('printer', 1500, 11, 15)
unit_2 = Scanners('scanner', 1000, 6)
unit_3 = Xerox('xerox', 1800, 4)
print(unit_1.name)
print(f'total cost of printers - {unit_1.total_cost()}')
unit_1.cartridges_left = 2
print(f'pages able to print - {unit_1.pages_able_to_print()}')
print(unit_1.reception())
print(unit_1.space_left(unit_1))
""" Задание 7
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
import re


class ComplexNumbers:
    def __init__(self, body):
        self.body = body
        numbers_list = re.findall(r'\d+', self.body)
        self.numbers = [int(x) for x in numbers_list]
        self.operators = re.findall(r'-', self.body)
        self.operators += re.findall(r'\+', self.body)
        if len(self.operators) == 2:
            self.real_part = -self.numbers[0]
        else:
            self.real_part = self.numbers[0]
        if self.operators[-1] == '+':
            self.imaginary_part = self.numbers[1]
        else:
            self.imaginary_part = - self.numbers[1]

    def __add__(self, other):
        r_result = self.real_part + other.real_part
        i_result = self.imaginary_part + other.imaginary_part

        if r_result == 0:
            return f'{i_result}i'
        elif i_result == 0:
            return r_result
        elif i_result < 0:
            return f'{r_result} - {abs(i_result)}i'
        else:
            return f'{r_result} + {i_result}i'

    def __mul__(self, other):
        r_result = (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part)
        i_result = (self.imaginary_part*other.real_part) + (other.imaginary_part*self.real_part)
        if r_result == 0:
            return f'{i_result}i'
        elif i_result == 0:
            return r_result
        elif i_result < 0:
            return f'{r_result} - {abs(i_result)}i'
        else:
            return f'{r_result} + {i_result}i'


z1 = ComplexNumbers('-2 - 3i')
z2 = ComplexNumbers('-3 - 2i')
z3 = ComplexNumbers('8 + 3i')
z4 = ComplexNumbers('3 + 8i')
z5 = ComplexNumbers('-5 + 5i')
z6 = ComplexNumbers('5 - 8i')
z7 = ComplexNumbers('8 - 3i')
z8 = ComplexNumbers('3 + 3i')
z10 = ComplexNumbers('2 + 3i')
z11 = ComplexNumbers('-1 + 1i')
print(z1 + z2)
print(z3 + z4)
print(z5 + z6)
print(z7 + z8)
z9 = ComplexNumbers(z1 + z2)
print(z9 + z3)
print(z10 * z11)
print(z4 * z5)
