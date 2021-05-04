from task_01 import *  # импортирую файл с решением, чтобы все имена были в глобальных переменных
from memory_functions import *

globals_dict = globals().copy()  # копия, потому что во время вывода globals изменяется
only_my_vars_dict = {k: v for k, v in globals_dict.items() if to_keep(k)}  # словарь только с моими переменными
print(only_my_vars_dict)

show_memory(only_my_vars_dict)

"""
SIZE	:28
MIN_ITEM	:24
MAX_ITEM	:28
array	:256
57	:28
43	:28
17	:28
31	:28
18	:28
23	:28
80	:28
72	:28
28	:28
55	:28
51	:28
29	:28
55	:28
44	:28
96	:28
30	:28
56	:28
0	:24
9	:28
53	:28
max_pos	:28
max_el	:28
min_pos	:28
min_el	:24
i	:28
el	:28
sum_between	:28
k	:28
общий расход памяти на переменные: 1112 байт

или 1064, если нет элементов между

вывод: список занимает очень много памяти, надо заменить кортежем, тк менять его не понадобится
"""
