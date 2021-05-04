"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict

QUARTERS = 4  # год разделен на 4 квартала
firms = defaultdict(list)
firms_amt = int(input('количество предприятий: '))

for i in range(firms_amt):
    f_name = input(f'введите название {i + 1}-го предприятия: ')

    for m in range(QUARTERS):
        qu_profit = int(input(f'прибыль за {m + 1}-й квартал: '))
        firms[f_name].append(qu_profit)
del f_name, qu_profit

avg_profit = sum(sum(q) for q in firms.values()) / firms_amt
above_average_firms, below_average_firms = [], []

for key, value in firms.items():
    firm_profit = sum(value)
    if firm_profit > avg_profit:
        above_average_firms.append(key)
    elif firm_profit < avg_profit:
        below_average_firms.append(key)
del firm_profit

print(f'Средняя прибыль всех предприятий за год: {round(avg_profit, 2)}')
print(f'Предприятия, чья прибыль больше средней: {", ".join(above_average_firms)}')
print(f'Предприятия, чья прибыль меньше средней: {", ".join(below_average_firms)}')
