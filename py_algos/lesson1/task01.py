"""
Ссылка на б/с:
https://drive.google.com/file/d/11V-nY832AX18Kvy-ScOanHgp-P6dgiVz/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

x = int(input('Введите положительное трехзначное целое число: '))

units = x % 10
tens = x // 10 % 10
hundreds = x // 100
s = units + tens + hundreds
m = units * tens * hundreds

print(f'Сумма цифр числа равна {s}, произведение - {m}')
