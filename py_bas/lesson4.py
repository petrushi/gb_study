# Урок 4
# Задание 1

from sys import argv
script_name, pay_per_hour, hours, premium = argv


def calc_wage(pay_per_hour, hours, premium):
    wage = int(pay_per_hour) * int(hours) + int(premium)
    return wage


print(f"Заработная плата сотрудника составляет {calc_wage(pay_per_hour, hours, premium)}")

# Задание 2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[el] for el in range(1, len(my_list))
            if my_list[el]>my_list[el-1]
            ]
print(new_list)

#  Задание 3

#  считая, что "в пределах от 20 до 240" включает "240"
gen_list = [el for el in range(20, 241) if (el % 20 == 0 or el % 21 == 0)]
print(gen_list)

# Задание 4

test_freq = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
freq_list = [el for el in test_freq if test_freq.count(el) == 1]
print(freq_list)

# Задание 5

even_range = [el for el in range(100, 1001) if el % 2 == 0]
range_product = 1
for i in even_range:
    range_product = range_product * i
print(range_product)

# Задание 6

from itertools import count, cycle

# а)

start = int(input('input start number: '))
stop = int(input('input final number: '))
for el in count(start):
    if el > stop:
        break
    else:
        print(el)

# б)

i = 0
amount = int(input('input amount of iterations: '))
iterable_list = [1, 2, 3, 4, 5, 6, 7]
for el in cycle(iterable_list):
    if i >= amount:
        break
    print(el)
    i += 1
    
# Задание 7


def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    yield result


user_fact = int(input('input number for calculating factorial: '))
for number in fact(user_fact):
    print(f'!{user_fact} = {number}')
