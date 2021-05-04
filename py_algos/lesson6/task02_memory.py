from task_02 import *  # импортирую файл с решением, чтобы все имена были в глобальных переменных
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
20	:28
16	:28
34	:28
81	:28
9	:28
5	:28
1	:28
11	:28
78	:28
31	:28
100	:28
53	:28
15	:28
7	:28
43	:28
64	:28
24	:28
25	:28
39	:28
100	:28
max_	:28
min_	:28
i	:28
sum_between	:28
is_summing	:50
n	:50
is_max_happened	:50
y	:50
is_min_happened	:50
y	:50
el	:28
общий расход памяти на переменные: 1280 байт


вывод: кортеж съел на 56 байт меньше, это успех, на односимвольных строках сэкономить не получилось, занимают в 2 раза
больше памяти чем int, тк они по сути все равно списки, char в python нет
"""
