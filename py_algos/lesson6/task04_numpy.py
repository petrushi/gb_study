"""
Так как bool подкласс int-а в python, он занимает много места. Решил использовать модуль numpy, где есть свой bool_,
занимающий 1 байт вместо 4(решение как в _02_02)
"""
from numpy import bool_
import random
import sys

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10
rnd_tuple = tuple(random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE))  # создаю случайный массив

max_ = rnd_tuple[0]
min_ = rnd_tuple[0]

for i in range(1, SIZE):
    if rnd_tuple[i] > max_:
        max_ = rnd_tuple[i]
    if rnd_tuple[i] < min_:
        min_ = rnd_tuple[i]

sum_between = 0
is_summing = bool_(False)  # прибавлять элементы или нет
is_max_happened = bool_(False)
is_min_happened = bool_(False)

for el in rnd_tuple:
    if is_summing:  # если встречался мин или макс элемент, складываю следующий
        sum_between += el
    if el == min_ and not is_min_happened:
        is_summing = not is_summing
        is_min_happened = bool_(True)
    if el == max_ and not is_max_happened:
        is_summing = not is_summing
        is_max_happened = bool_(True)
    if is_min_happened and is_max_happened:
        sum_between -= el
        break

print(f'массив: {rnd_tuple}')
print(f'минимальный элемент - {min_}, максимальный элемент - {max_}')
print(f'сумма элементов между первыми наименьшим и наибольшим элементами: {sum_between}')

