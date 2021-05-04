"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создаю случайный массив

max_index, max_el = 0, array[0]  # создаю переменные для макс и мин значений и их индексов
min_index, min_el = 0, array[0]

for i, el in enumerate(array):
    if el > max_el:
        max_index, max_el = i, el
    if el < min_el:
        min_index, min_el = i, el

print(f'изначальный массив: \n{array}')
array[max_index], array[min_index] = array[min_index], array[max_index]
print(f'после перемены первого минимального и максимального элемента местами: \n{array}')

