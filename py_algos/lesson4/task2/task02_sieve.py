from timeit import timeit
from cProfile import run
from math import log, sqrt

"""
Поиск числа с помощью решета. Использую 2 списка, затратно по памяти, но выполняется довольно быстро.
"""


def prime_sieve(x):
    n = int((x * log(x)) + x * 2)  # моя формула примерного распределения простых чисел
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, int(sqrt(n))):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    b = []
    for j in sieve:
        if sieve[j] != 0:
            b.append(sieve[j])
    ans = b[x-1]
    return ans


print(prime_sieve(1_000))
print(run('prime_sieve(1_000)'))
print(timeit('prime_sieve(1_000)', number=10, globals=globals()))

"""
1_000 == 7919:
    timeit: 0.022364022996043786
    
10_000 = 104729:

    timeit: 0.32673908899596427
    
    cProfile:
             10634 function calls in 0.036 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.036    0.036 <string>:1(<module>)
        1    0.005    0.005    0.005    0.005 task02_sieve.py:11(<listcomp>)
        1    0.030    0.030    0.036    0.036 task02_sieve.py:9(prime_sieve)
        1    0.000    0.000    0.036    0.036 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
    10627    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

    
1_000_000 == 15485863:

    timeit: 6.402934536999965


"""
