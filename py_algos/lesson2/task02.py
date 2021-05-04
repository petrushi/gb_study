"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
Блок-схемы 
https://drive.google.com/file/d/17XxgkIj-a5s72BuBFPH_Es85psMPJHPe/view?usp=sharing
"""


def even_odd(x, even=0, odd=0):
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
    if x < 10:
        print(f'четные цифры: {even}, нечетные цифры: {odd}')
        return even, odd
    else:
        return even_odd(x // 10, even, odd)


num = int(input('введите натуральное число: '))
even_odd(num)
