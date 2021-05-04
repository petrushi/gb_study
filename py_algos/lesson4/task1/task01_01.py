from timeit import timeit
from cProfile import run


def rec_even_odd(x, even=0, odd=0):
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
    if x < 10:
        return even, odd
    else:
        return rec_even_odd(x // 10, even, odd)


run('rec_even_odd(int("94" * 256))')
print(timeit('rec_even_odd(int("9"))', number=100, globals=globals()))  # 4.954800533596426e-05
print(timeit('rec_even_odd(int("57"))', number=100, globals=globals()))  # 5.513299402082339e-05
print(timeit('rec_even_odd(int("28" * 2))', number=100, globals=globals()))  # 9.449899516766891e-05
print(timeit('rec_even_odd(int("12" * 4))', number=100, globals=globals()))  # 0.0001923259987961501
print(timeit('rec_even_odd(int("34" * 8))', number=100, globals=globals()))  # 0.0004537190034170635
print(timeit('rec_even_odd(int("56" * 16))', number=100, globals=globals()))  # 0.0009614220034563914
print(timeit('rec_even_odd(int("78" * 32))', number=100, globals=globals()))  # 0.0021742509998148307
print(timeit('rec_even_odd(int("90" * 64))', number=100, globals=globals()))  # 0.005482879001647234
print(timeit('rec_even_odd(int("12" * 128))', number=100, globals=globals()))  # 0.014818408999417443
print(timeit('rec_even_odd(int("34" * 256))', number=100, globals=globals()))  # 0.04331965500023216
"""
cProfile:
512 символов:
         515 function calls (4 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
    512/1    0.001    0.000    0.001    0.001 task01_01.py:5(rec_even_odd)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


далее замеры с максимальной рекурсией в 10000:
print(timeit('rec_even_odd(int("56" * 512))', number=100, globals=globals()))  # 0.14796338000451215
print(timeit('rec_even_odd(int("78" * 1024))', number=100, globals=globals()))  # 0.5196730250027031
print(timeit('rec_even_odd(int("90" * 2048))', number=100, globals=globals()))  # 1.9352987469974323
print(timeit('rec_even_odd(int("12" * 4096))', number=100, globals=globals()))  # 7.183742383997014
"""
