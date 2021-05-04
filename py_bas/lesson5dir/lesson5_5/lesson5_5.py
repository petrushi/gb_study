with open('numbers.txt', 'w') as file:
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
