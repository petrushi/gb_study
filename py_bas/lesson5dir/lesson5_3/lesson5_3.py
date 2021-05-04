with open('employees.txt', encoding='utf-8') as file:
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
