"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
import random

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создаю случайный массив

max_negative = None
pos = None

for i, el in enumerate(array):
    if max_negative is None:
        if el < 0:
            max_negative = el
            pos = i
    elif 0 > el > max_negative:
        max_negative = el
        pos = i

print(f'массив: {array}')
if max_negative is None:
    print('в массиве нет отрицательных элементов')
else:
    print(f'первое максимальное отрицательное число в массиве: {max_negative}, индекс равен: {pos}')
