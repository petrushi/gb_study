from task_03 import *  # импортирую файл с решением, чтобы все имена были в глобальных переменных
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
73	:28
20	:28
15	:28
71	:28
13	:28
6	:28
5	:28
72	:28
28	:28
33	:28
80	:28
94	:28
99	:28
83	:28
29	:28
5	:28
71	:28
44	:28
44	:28
29	:28
idx_min	:28
idx_max	:28
i	:28
summ	:28
общий расход памяти на переменные: 1008 байт

вывод: в своих решениях использовал больше переменных, чем требовалось, оттого занимал больше памяти, 
надо было работать только с индексами
"""
