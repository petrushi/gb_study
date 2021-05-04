# Задание 1
a = 'hello world'
b = 2
print(a)
print(b)
# Задание 2
print('следующая программа переведет секунды в чч:мм:сс')
seconds = int(input('введите время в секундах:'))
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))
# Задание 3
n = int(input('введите число n, программа посчитает сумму n + nn + nnn: '))
sum_of_n = n + 11 * n + 111 * n
print(f'сумма равна: {sum_of_n}')
# Задание 4
user_number = int(input('программа найдет самую большую цифру в числе: '))
temp = user_number
max_num = user_number % 10
while temp / 10 > 0:
    next_num = (temp // 10) % 10
    max_num = next_num if (max_num < next_num) else max_num
    temp //= 10
print(f'самое большая цифра в числе равна {max_num}')
# Задание 5
income = int(input('введите значение выручки: '))
cost = int(input('введите значение издержек: '))
if income == cost:
    print('ваша фирма в нуле')
elif cost > income:
    print('фирма сейчас терпит убыток')
else:
    print('фирма сейчас получает прибыль')
    profit = income - cost
    rentability = income / profit
    print(f'рентабильность фирмы равна {rentability}')
    employees = int(input('введите количетво работников фирмы:'))
    profit_per_employee = profit / employees
    print(f'Прибыль фирмы в расчете на одного сотрудника равна {profit_per_employee}')
#Задание 6
starting_length = int(input('введите расстояние, которое пробежал спортсмен в первый день: '))
goal = int(input('введите желаемое расстояние пробежки спортсмена: '))
today_length = starting_length
i = 1
while today_length < goal:
    print(f'{i} день - {today_length}')
    today_length += today_length / 100 * 10
    i += 1
print(f'{i} день - {today_length}')
print(f'на {i} день спортсмен достиг результата - не менее {goal} километров')
