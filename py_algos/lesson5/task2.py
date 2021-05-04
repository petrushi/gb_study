"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Написал только сложение
"""
from collections import deque

NUM_SYS = 16
hex_list = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
result = deque()
nxt = 0  # единицы, вышедшие в следующий разряд

a = deque(input('Введите число в шестнадцатеричной системе счисления: '))
b = deque(input('Введите второе число в шестнадцатеричной системе счисления: '))

while len(a) > 0 or len(b) > 0:
    if len(a) > 0:
        first_dig = a.pop()
    else:
        first_dig = 0
    if len(b) > 0:
        second_dig = b.pop()
    else:
        second_dig = 0
    if first_dig in hex_list:
        first_dig = hex_list[first_dig]
    if second_dig in hex_list:
        second_dig = hex_list[second_dig]
    res_dig = int(first_dig) + int(second_dig) + nxt
    if res_dig >= NUM_SYS:
        nxt = 1
        res_dig -= NUM_SYS
    else:
        nxt = 0
    if res_dig >= 10:  # если число больше 9, меняю его на ключ из словаря
        res_dig = list(hex_list.keys())[res_dig - 10]  # делаю лист из ключей, нахожу нужный по индексу
        # res_dig = list(hex_list.keys())[list(hex_list.values()).index(res_dig)] - вариант поиска по ключу
    result.appendleft(str(res_dig))

if nxt == 1:  # если единица вышла в следующий разряд
    result.appendleft(str(nxt))  # добавляю слева

print(f'Сумма чисел: {"".join(result)}')
