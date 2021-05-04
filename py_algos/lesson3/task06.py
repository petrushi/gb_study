"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создаю случайный массив

max_pos, max_el = 0, array[0]
min_pos, min_el = 0, array[0]
sum_between = 0

for i, el in enumerate(array):
    if el > max_el:
        max_pos, max_el = i, el
    if el < min_el:
        min_pos, min_el = i, el

print(f'массив: {array}')

if abs(max_pos - min_pos) < 2:
    print('между первым наибольшим и первым наименьшим элементами нет значений')
else:
    if min_pos < max_pos:
        for i in range(min_pos + 1, max_pos):
            sum_between += array[i]
    else:
        for i in range(max_pos + 1, min_pos):
            sum_between += array[i]
    print(f'сумма элементов между первыми наименьшим и наибольшим элементами: {sum_between}')
