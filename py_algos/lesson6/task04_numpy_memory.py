from task_04_numpy import *  # импортирую файл с решением, чтобы все имена были в глобальных переменных
from memory_functions import *

globals_dict = globals().copy()  # копия, потому что во время вывода globals изменяется
only_my_vars_dict = {k: v for k, v in globals_dict.items() if to_keep(k)}  # словарь только с моими переменными
print(only_my_vars_dict)

show_memory(only_my_vars_dict)
"""
bool_	:416
SIZE	:28
MIN_ITEM	:24
MAX_ITEM	:28
rnd_tuple	:200
2	:28
8	:28
6	:28
1	:28
6	:28
5	:28
0	:24
7	:28
8	:28
0	:24
3	:28
0	:24
0	:24
5	:28
5	:28
4	:28
7	:28
6	:28
2	:28
10	:28
max_	:28
min_	:24
i	:28
sum_between	:28
is_summing	:24
is_max_happened	:25
is_min_happened	:25
el	:28
общий расход памяти на переменные: 1450 байт

вывод: вес самого класса bool_ перевесил мои попытки оптимизации(сохранил ~10 байт на трех переменных xD), 
без класса вес 1034 байта

"""
