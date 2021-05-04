"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создаю случайный массив

if len(array) < 2:
    print('в массиве нет двух элементов')
else:  # далее условие, чтобы при длине 2 в первой переменной был наименьший эл., а во второй равный или больше
    first_min_el, second_min_el = (array[0], array[1]) if array[0] <= array[1] else (array[1], array[0])

    for el in array[2:]:
        if el < first_min_el:
            if first_min_el < second_min_el:
                second_min_el = first_min_el
            first_min_el = el
        elif el < second_min_el:
            second_min_el = el

    print(f'массив: {array}')
    print(f'наименьший элемент: {first_min_el}, второй наименьший: {second_min_el}')

