from timeit import timeit
from cProfile import run
from math import sqrt
"""
Попробовал использовать больше булевых типов и отказаться от списка. Получилось очень медленно.
"""


def nth_prime(n):
    """
    Программа находит n-ное простое число без формирования списка простых чисел.
    """
    if n == 1:
        return 2
    else:
        ith_prime = 3
        i = 2
        num = ith_prime
    while i < n:
        num += 2
        if is_prime(num):
            ith_prime = num
            i += 1
    return ith_prime


def is_prime(x):
    """
    Программа проверяет, является ли число простым
    возвращает bool
    """
    if x == 2:
        return True
    elif x < 2:
        return False
    else:
        if x % 2 == 0:
            return False
        if x > 10:
            last_digit = x % 10
            if last_digit == 5 or last_digit == 0:
                return False  # если последняя цифра равна 5 или 0 - число составное
        for i in range(3, int(sqrt(x) + 1), 2):  # можно проверять только нечетные делители, меньшие корня числа
            if x % i == 0:
                return False
        return True


print(nth_prime(1_000))
print(run('nth_prime(1_000)'))
print(timeit('nth_prime(1_000)', number=10, globals=globals()))


"""
1_000:

    timeit: 0.05129538300388958

10_000:

    timeit: 1.1113693240040448

    cProfile:

         94258 function calls in 0.141 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.141    0.141 <string>:1(<module>)
    52363    0.122    0.000    0.127    0.000 task_02_no_sieve_no_list.py:27(is_prime)
        1    0.014    0.014    0.141    0.141 task_02_no_sieve_no_list.py:9(nth_prime)
        1    0.000    0.000    0.141    0.141 {built-in method builtins.exec}
    41891    0.005    0.000    0.005    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Для 1_000_000:

    timeit: 113.86798916300177

"""
