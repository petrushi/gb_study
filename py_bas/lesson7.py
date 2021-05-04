""" Задание 1
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join('%d' % el for el in line) for line in self.matrix])

    def __add__(self, other):
        mat_sum = []
        for i in range(len(self.matrix)):
            mat_sum_line = []
            for j in range(len(self.matrix[0])):
                mat_sum_line.append(self.matrix[i][j] + other.matrix[i][j])
            mat_sum.append(mat_sum_line)
        return Matrix(mat_sum)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(matrix_1.matrix)
print(matrix_1)
print(matrix_2.matrix)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2
print(matrix_3.matrix)
print(matrix_3)
""" Задание 2
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, value):
        self.__name = value

    @abstractmethod
    def fabric_expense(self):
        pass

    @property
    def name(self):
        return self.__name


class Coats(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    def fabric_expense(self):
        return self.v/6.5 + 0.5


class Suits(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    def fabric_expense(self):
        return 2 * self.h + 0.3


coat = Coats('yellow coat', 1.56)
suit = Suits('black suit', 0.5)
print(coat.name)
print(coat.fabric_expense())
print(suit.name)
print(suit.fabric_expense())
print(f'total expense is {coat.fabric_expense() + suit.fabric_expense()}')
""" Задание 3
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cells:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return self.amount - other.amount
        else:
            raise ValueError('should pe positive')

    def __mul__(self, other):
        return self.amount * other.amount

    def __truediv__(self, other):
        return self.amount // other.amount

    def make_order(self, row):
        order = ''
        i = self.amount
        while i > row:
            order += '*' * row + '\n'
            i -= row
        order += '*' * i
        print(order)
"""" Функция, которая бы принимала количество рядов, а не ячеек в ряду(невнимательно прочитал)
    def make_order(self, lines):
        order = ''
        i = self.amount
        while i > self.amount // lines:
            order += '*' * (self.amount // lines) + '\n'
            i -= self.amount // lines
        print(order + ('*' * (self.amount % lines)))
"""
cells_1 = Cells(12)
cells_2 = Cells(5)
cells_3 = cells_1 + cells_2
print(cells_3)
print(cells_1 - cells_2)
print(cells_1 / cells_2)
cells_1.make_order(5)
cells_3 = Cells(15)
cells_3.make_order(5)
