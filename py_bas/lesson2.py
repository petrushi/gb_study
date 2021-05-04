# Задание 1
my_list = ['three', 3.0, 3, True, (1, 2, 3)]
for el in my_list:
    print(type(el))
# Задание 2
user_string = input('input your list separated with space: ')
user_list = user_string.split(' ')
print(user_list)
length = len(user_list)
for i in range(0, length-1, 2):
    temp = user_list[i]
    user_list[i] = user_list[i+1]
    user_list[i+1] = temp
print(user_list)
# Задание 3
# решение через list
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
user_month = int(input('input your month from 1 to 12: '))
print('your month is', end=' ')
if user_month in winter:
    print('winter')
elif user_month in spring:
    print('spring')
elif user_month in summer:
    print('summer')
elif user_month in fall:
    print('fall')
else:
    print('error')
# решение через dict
year = {
    12: 'winter', 1: 'winter', 2: 'winter',
    3: 'spring', 4: 'spring', 5: 'spring',
    6: 'summer', 7: 'summer', 8: 'summer',
    9: 'fall', 10: 'fall', 11: 'fall'}
user_month = int(input('input your month from 1 to 12: '))
print('your month is', end=' ')
print(year.get(user_month))
# Задание 4
user_string = input('input your words separated with space:')
a = user_string.split(' ')
for ind, el in enumerate(a, 1):
    print(ind, el[:10])
# Задание 5
my_list = [7, 5, 3, 3, 2]
user_number = int(input('input your number to add to rating:'))
my_list.append(user_number)
my_list.sort(reverse=True)
print(my_list)
# Задание 6
x = int(input('input number of items(tuples): '))
y = int(input('input number of parameters: '))
k = 1
user_list = []
while k <= x:
    i = 0
    user_dict = {}
    while i < y:
        param = input('input key of parameter: ')
        user_value = input('input value of parameter: ')
        user_dict[param] = user_value
        i += 1
    item = (k, user_dict)
    user_list.append(item)
    print(user_list)
    k += 1
user_input_string = input('input keys on which will be based analysis(separated with space): ')
search = user_input_string.split(' ')
i = 0
analysis_dict = {}
while i < len(search):
    analysis_list = []
    for el in user_list:
        user_dict = el[1]
        a = user_dict.get(search[i])
        analysis_list.append(a)
        analysis_dict[search[i]] = analysis_list
    i += 1
print(analysis_dict)
