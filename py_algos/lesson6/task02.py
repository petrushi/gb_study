"""
Решение с помощью односимвольных строк(убедился, что в Python нет char)
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
is_summing = 'n'  # прибавлять элементы или нет
is_max_happened = 'n'
is_min_happened = 'n'
for el in rnd_tuple:
    if is_summing == 'y':  # если встречался мин или макс элемент, складываю следующий
        sum_between += el
    if el == min_ and is_min_happened == 'n':
        is_summing = 'y' if is_summing == 'n' else 'n'
        is_min_happened = 'y'
    if el == max_ and is_max_happened == 'n':
        is_summing = 'y' if is_summing == 'n' else 'n'
        is_max_happened = 'y'
    if is_min_happened == 'y' and is_max_happened == 'y':
        sum_between -= el
        break

print(f'массив: {rnd_tuple}')
print(f'минимальный элемент - {min_}, максимальный элемент - {max_}')
print(f'сумма элементов между первыми наименьшим и наибольшим элементами: {sum_between}')


