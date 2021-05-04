"""
Задание 6 из урока 3
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
Информация о моей системе:
Python 3.8.5
[GCC 9.3.0] on linux
64 разряда

Мое первое решение:
"""
import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создаю случайный массив

max_pos, max_el = 0, array[0]
min_pos, min_el = 0, array[0]

for i, el in enumerate(array):
    if el > max_el:
        max_pos, max_el = i, el
    if el < min_el:
        min_pos, min_el = i, el

if abs(max_pos - min_pos) < 2:
    print('между первым наибольшим и первым наименьшим элементами нет значений')
else:
    sum_between = 0
    if min_pos < max_pos:
        for k in range(min_pos + 1, max_pos):
            sum_between += array[k]
    else:
        for k in range(max_pos + 1, min_pos):
            sum_between += array[k]

    print(f'массив: {array}')
    print(f'минимальный элемент - {min_el}, максимальный элемент - {max_el}')
    print(f'сумма элементов между первыми наименьшим и наибольшим элементами: {sum_between}')
