from timeit import timeit
from cProfile import run


def iter_new_even_odd(x):
    even, odd = 0, 0
    while x > 0:
        num = x % 10
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        x //= 10
    return even, odd


run('iter_new_even_odd(int("94" * 256))')
print(timeit('iter_new_even_odd(int("9"))', number=100, globals=globals()))  # 6.518299994695553e-05
print(timeit('iter_new_even_odd(int("57"))', number=100, globals=globals()))  # 6.583600008980284e-05
print(timeit('iter_new_even_odd(int("94" * 2))', number=100, globals=globals()))  # 0.00010733400006301963
print(timeit('iter_new_even_odd(int("12" * 4))', number=100, globals=globals()))  # 0.00019473700001526595
print(timeit('iter_new_even_odd(int("34" * 8))', number=100, globals=globals()))  # 0.0003796380000267163
print(timeit('iter_new_even_odd(int("56" * 16))', number=100, globals=globals()))  # 0.0006952620000220122
print(timeit('iter_new_even_odd(int("78" * 32))', number=100, globals=globals()))  # 0.0014445799999975861
print(timeit('iter_new_even_odd(int("90" * 64))', number=100, globals=globals()))  # 0.003391100000044389
print(timeit('iter_new_even_odd(int("12" * 128))', number=100, globals=globals()))  # 0.008394303000045511
print(timeit('iter_new_even_odd(int("34" * 256))', number=100, globals=globals()))  # 0.02284372400004031
"""
cProfile:
512 символов:
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task01_04.py:5(iter_new_even_odd)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
8192:
         4 function calls in 0.033 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.033    0.033 <string>:1(<module>)
        1    0.033    0.033    0.033    0.033 task01_04.py:5(iter_new_even_odd)
        1    0.000    0.000    0.033    0.033 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



print(timeit('iter_new_even_odd(int("56" * 512))', number=100, globals=globals()))  # 0.07024101900003643
print(timeit('iter_new_even_odd(int("78" * 1024))', number=100, globals=globals()))  # 0.23114871999996467
print(timeit('iter_new_even_odd(int("90" * 2048))', number=100, globals=globals()))  # 0.8571792689999711
print(timeit('iter_new_even_odd(int("12" * 4096))', number=100, globals=globals()))  # 3.2042567759999656

print(timeit('iter_new_even_odd(int("34" * 8192))', number=100, globals=globals()))  # 12.11230721600009
print(timeit('iter_new_even_odd(int("56" * 16384))', number=100, globals=globals()))  # 47.441398574000004
"""
