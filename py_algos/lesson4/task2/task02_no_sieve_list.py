from timeit import timeit
from cProfile import run
import math

"""
Решение через список подсчетом делителей. Все равно сильно медленнее решета.
"""


def prime_lst(x):
    """
    Программа находит n-ное простое число, формируя список и возвращает последний элемент
    """
    pr = [2, 3]
    n = 5
    length_ = len(pr)
    while length_ < x:
        divs = 1
        i = 1
        sqrt_ = math.sqrt(n)
        while pr[i] <= sqrt_:  # до корня из числа
            if n % pr[i] == 0:  # проверяю деление только на простые
                divs = divs + 1
            if divs == 2:
                break
            i += 1
        if divs == 1:
            pr.append(n)
            length_ += 1
        n += 2
    return pr[-1]


run('prime_lst(1_000)')
print(prime_lst(1_000))
print(timeit('prime_lst(1_000)', number=10, globals=globals()))

"""
Для 1_000:

    timeit: 0.05307934500160627
    
Для 10_000:

    timeit: 1.3071990509997704
    
    cProfile:
    
         62366 function calls in 0.146 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.146    0.146 <string>:1(<module>)
        1    0.140    0.140    0.146    0.146 task02_no_sieve_list.py:9(prime_lst)
        1    0.000    0.000    0.146    0.146 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    52363    0.005    0.000    0.005    0.000 {built-in method math.sqrt}
     9998    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Для 1_000_000:

    timeit == 89.0735487359998
"""
