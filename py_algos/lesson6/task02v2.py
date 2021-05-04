"""
Почти такое же решение как _02, но с boolean
"""
import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
rnd_tuple = tuple(random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE))  # создаю случайный массив

max_ = rnd_tuple[0]
min_ = rnd_tuple[0]

for i in range(1, SIZE):
    if rnd_tuple[i] > max_:
        max_ = rnd_tuple[i]
    if rnd_tuple[i] < min_:
        min_ = rnd_tuple[i]

sum_between = 0
is_summing = False  # прибавлять элементы или нет
is_max_happened = False  # был ли максимальный
is_min_happened = False  # был ли минимальный

for el in rnd_tuple:
    if is_summing:  # если встречался мин или макс элемент, складываю следующий
        sum_between += el
    if el == min_ and not is_min_happened:
        is_summing = not is_summing
        is_min_happened = True
    if el == max_ and not is_max_happened:
        is_summing = not is_summing
        is_max_happened = True
    if is_min_happened and is_max_happened:
        sum_between -= el
        break

print(f'массив: {rnd_tuple}')
print(f'минимальный элемент - {min_}, максимальный элемент - {max_}')
print(f'сумма элементов между первыми наименьшим и наибольшим элементами: {sum_between}')


