from timeit import timeit
from cProfile import run


def iteration_even_odd(x):
    even, odd = 0, 0
    while x > 0:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
        x //= 10
    return even, odd


run('iteration_even_odd(int("94" * 256))')
print(timeit('iteration_even_odd(int("9"))', number=100, globals=globals()))  # 5.80769992666319e-05
print(timeit('iteration_even_odd(int("57"))', number=100, globals=globals()))  # 5.477599916048348e-05
print(timeit('iteration_even_odd(int("94" * 2))', number=100, globals=globals()))  # 8.876400534063578e-05
print(timeit('iteration_even_odd(int("12" * 4))', number=100, globals=globals()))  # 0.00016441199841210619
print(timeit('iteration_even_odd(int("34" * 8))', number=100, globals=globals()))  # 0.00031527700048172846
print(timeit('iteration_even_odd(int("56" * 16))', number=100, globals=globals()))  # 0.0006685469998046756
print(timeit('iteration_even_odd(int("78" * 32))', number=100, globals=globals()))  # 0.0015147609956329688
print(timeit('iteration_even_odd(int("90" * 64))', number=100, globals=globals()))  # 0.0038602909990004264
print(timeit('iteration_even_odd(int("12" * 128))', number=100, globals=globals()))  # 0.011522827000590041
print(timeit('iteration_even_odd(int("34" * 256))', number=100, globals=globals()))  # 0.03595429800043348

"""
cProfile:
512 символов:
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task01_03.py:5(iteration_even_odd)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
8192:
         4 function calls in 0.077 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.077    0.077 <string>:1(<module>)
        1    0.077    0.077    0.077    0.077 task01_03.py:5(iteration_even_odd)
        1    0.000    0.000    0.077    0.077 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


print(timeit('iteration_even_odd(int("56" * 512))', number=100, globals=globals()))  # 0.12430953500006581
print(timeit('iteration_even_odd(int("78" * 1024))', number=100, globals=globals()))  # 0.4496790940029314
print(timeit('iteration_even_odd(int("90" * 2048))', number=100, globals=globals()))  # 1.7246242819965119
print(timeit('iteration_even_odd(int("12" * 4096))', number=100, globals=globals()))  # 6.68503041099757

print(timeit('iteration_even_odd(int("34" * 8192))', number=100, globals=globals()))  # 26.16368468199653
print(timeit('iteration_even_odd(int("56" * 16384))', number=100, globals=globals()))  # 103.9254790690029
"""
