# Задание 1
def divide_2_numbers(x, y):
    if y == 0:
        return 'division by zero is undefined'
    else:
        return x / y


numerator = float(input('input numerator: '))
denominator = float(input('input denominator: '))
print(divide_2_numbers(numerator, denominator))

# Задание 2


def person_in_one_string(name, last_name, birth_year, city_of_living, phone_number, e_mail):
    print(f'Пользователя зовут {name} {last_name}, он родился в {birth_year}, живет в {city_of_living}.'
          f' Номер телефона: {phone_number}, e-mail: {e_mail}.')


user_first_name = input('input your first name: ')
user_last_name = input('input your last name: ')
user_birth_year = input('input your birth year: ')
user_city_of_living = input('input your city of living: ')
user_phone_number = input('input your phone number: ')
user_e_mail = input('input your e-mail:')
person_in_one_string(user_first_name, user_last_name, user_birth_year,
                     user_city_of_living, user_phone_number, user_e_mail)

# Задание 3


def sum_of_2_biggest_numbers_of_3():
    x = int(input('input first number:'))
    y = int(input('input second number: '))
    z = int(input('input third number: '))
    if x >= y or x >= z:
        if y >= z:
            return x + y
        elif z >= y:
            return x + z
    else:
        return y + z


print(sum_of_2_biggest_numbers_of_3())

# Задание 4


def negative_or_positive_power_of_number(number, power):
    denom = number
    if power < 0:
        for x in range(abs(power)-1):
            denom *= number
        result = 1 / denom
    elif power == 0:
        result = 1
    else:
        result = number
        for x in range(power-1):
            result *= number
    return result


user_number = float(input('input your number: '))
user_power = int(input('input your power: '))
print(negative_or_positive_power_of_number(user_number, user_power))

# Задание 5


def iterable_sum():
    check_output_need = sum_of_num = 0
    while 1:
        user_input = input("input numbers separated with space to sum them, input q for exit: ")
        user_input = user_input.split(" ")
        for user_elem in user_input:
            if user_elem == 'q':
                if check_output_need != sum_of_num:
                    print(sum_of_num)
                return
            else:
                sum_of_num += int(user_elem)
        print(sum_of_num)
        check_output_need = sum_of_num


iterable_sum()
# Задание 6
# a)


def to_upper_case_first_letter():
    user_string = input('input your word: ')
    output = user_string.capitalize()
    return output


print(to_upper_case_first_letter())
# b)


def to_upper_case_first_letter_every_word():
    user_string = input('input your words separated with space: ')
    output_list = []
    list_of_words = user_string.split(' ')
    for word in list_of_words:
        word = word.capitalize()
        output_list.append(word)
        output_string = ' '.join(output_list)
    return output_string


print(to_upper_case_first_letter_every_word())
