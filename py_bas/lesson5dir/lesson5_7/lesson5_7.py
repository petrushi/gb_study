# Задание 7
import json
with open('firms.txt', encoding='utf-8') as file:
    firms_count = 0
    profit_sum = 0
    firms_dict = {}
    average_profit_dict = {}
    final_list = []

    for line in file:
        firm_list = line.split(' ')
        profit = int(firm_list[2]) - int(firm_list[3])
        firms_dict[firm_list[0]] = profit
        if profit > 0:
            profit_sum += profit
            firms_count += 1
    average_profit_dict['average_profit'] = profit_sum / firms_count
    final_list.append(firms_dict)
    final_list.append(average_profit_dict)
    print(final_list)
    with open('firms.json', 'w') as create_file:
        json.dump(final_list, create_file)
