# Задание 1
with open('txt_files/empty_file.txt', 'w', encoding='utf-8') as file:
    while True:
        user_input = str(input('input data to write in file:'))
        if user_input == '':
            break
        file.write(user_input + '\n')
# Задание 2
with open('txt_files/text_file.txt') as file:
    lines = file.readlines()
    print(f'Количество строк в файле - {len(lines)}')
    i = 0
    while i < len(lines):
        symbols = len(lines[i])
        print(f'Количество символов в строке {i+1} - {symbols}')
        i += 1
# Задание 3
with open('txt_files/employees.txt', encoding='utf-8') as file:
     lines = file.readlines()
     list_lines = []
     low_employees = []
     total = 0
     i = 0
     while i < len(lines):
          list_lines.append(lines[i].split(' '))
          if int(list_lines[i][2]) < 20000:
               low_employees.append(list_lines[i][0])
          i +=1
     low_employees_string = ', '.join(low_employees)
     print(f'Сотрудники, у которых ЗП меньше 20000 - {low_employees_string}')
     for el in list_lines:
          total += int(el[2])
     print(f'Средняя величина доходов сотрудников - {total/len(lines)}')
# Задание 4
with open('txt_files/english_numbers.txt') as file:
    lines = file.readlines()
    ru_lines = []
    with open('txt_files/russian_numbers.txt', 'w') as ru_file:
        for el in lines:
            ru_lines.append(el.replace('One', 'Один')
            .replace('Two', 'Два')
            .replace('Three', 'Три')
            .replace('Four', 'Четыре')
            )
        ru_file.writelines(ru_lines)
# Задание 5
with open('txt_files/sum_numbers.txt', 'w') as file:
    user_input = input('input numbers separated with space:')
    file.write(user_input)
    nums_list = user_input.split(' ')
    total = 0
    for el in nums_list:
        try:
            user_num = int(el)
            total += user_num
        except:
            pass
    print(f'sum of numbers is {total}')
# Задание 6

def list_sum(num_list):
    total = 0
    for el in num_list:
        total += el
    return total


subject_dict = {}
with open('txt_files/subjects.txt', encoding='utf-8') as file:
    lines = file.readlines()
    for el in lines:
        subject_list = el.split(':')
        hours_string = subject_list[1]
        i = 0
        hours_list = []
        while i < len(hours_string):
            hours_int = ''
            el = hours_string[i]
            while '0' <= el <= '9':
                hours_int += el
                i+= 1
                if i < len(hours_string):
                    el = hours_string[i]
                else:
                    break
            i += 1
            if hours_int != '':
                hours_list.append(int(hours_int))
        
        subject_dict[subject_list[0]] = list_sum(hours_list)
    print(subject_dict)
    # Задание 7
import json
with open('txt_files/firms.txt', encoding='utf-8') as file:
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
