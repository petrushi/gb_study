"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

a = input('Введите букву английского алфавита: ')
b = input('Введите другую букву английского алфавита: ')

a_pos = ord(a) - 96
b_pos = ord(b) - 96
inner_chars = abs(a_pos - b_pos) - 1

print(f'Ваша первая буква стоит на {a_pos} месте в алфавите, ваша вторая буква на {b_pos} месте')
print(f'Между ними букв - {inner_chars}')
