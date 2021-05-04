from timeit import timeit
from cProfile import run


def str_even_odd(x, even=0, odd=0):
    for i in str(x):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


run('str_even_odd(int("94" * 256))')
print(timeit('str_even_odd(int("9"))', number=100, globals=globals()))  # 8.122600411297753e-05
print(timeit('str_even_odd(int("57"))', number=100, globals=globals()))  # 0.00010453799768583849
print(timeit('str_even_odd(int("83" * 2))', number=100, globals=globals()))  # 0.00013919799675932154
print(timeit('str_even_odd(int("12" * 4))', number=100, globals=globals()))  # 0.00021964600455248728
print(timeit('str_even_odd(int("34" * 8))', number=100, globals=globals()))  # 0.00035835799644701183
print(timeit('str_even_odd(int("56" * 16))', number=100, globals=globals()))  # 0.0006663339954684488
print(timeit('str_even_odd(int("78" * 32))', number=100, globals=globals()))  # 0.0012893759994767606
print(timeit('str_even_odd(int("90" * 64))', number=100, globals=globals()))  # 0.002618532998894807
print(timeit('str_even_odd(int("12" * 128))', number=100, globals=globals()))  # 0.005317111994372681
print(timeit('str_even_odd(int("34" * 256))', number=100, globals=globals()))  # 0.010505015001399443
"""
cProfile:
512 символов:
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task01_02.py:5(str_even_odd)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
4096:
         4 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.003    0.003    0.003    0.003 task01_02.py:5(str_even_odd)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


print(timeit('str_even_odd(int("56" * 512))', number=100, globals=globals()))  # 0.022194236997165717
print(timeit('str_even_odd(int("78" * 1024))', number=100, globals=globals()))  # 0.04999087599571794
print(timeit('str_even_odd(int("90" * 2048))', number=100, globals=globals()))  # 0.12322501999733504
print(timeit('str_even_odd(int("12" * 4096))', number=100, globals=globals()))  # 0.3261064790058299

print(timeit('str_even_odd(int("34" * 8192))', number=100, globals=globals()))  # 0.9991469000015059
print(timeit('str_even_odd(int("56" * 16384))', number=100, globals=globals()))  # 3.3027206900005694
"""

