from task_02_02 import *  # импортирую файл с решением, чтобы все имена были в глобальных переменных
from memory_functions import *

globals_dict = globals().copy()  # копия, потому что во время вывода globals изменяется
only_my_vars_dict = {k: v for k, v in globals_dict.items() if to_keep(k)}  # словарь только с моими переменными
print(only_my_vars_dict)

show_memory(only_my_vars_dict)
"""
SIZE	:28
MIN_ITEM	:24
MAX_ITEM	:28
rnd_tuple	:200
35	:28
97	:28
87	:28
43	:28
87	:28
20	:28
49	:28
14	:28
30	:28
16	:28
100	:28
36	:28
24	:28
57	:28
34	:28
10	:28
33	:28
2	:28
18	:28
93	:28
max_	:28
min_	:28
i	:28
sum_between	:28
is_summing	:24
is_max_happened	:28
is_min_happened	:28
el	:28
общий расход памяти на переменные: 1060 байт

вывод: bool в python подкласс int, занимает также 24-28 байтов, засчет кортежа получилось сэкономить по памяти
"""
