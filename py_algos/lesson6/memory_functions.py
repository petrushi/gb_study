import sys
"""
две функции для поиска глобальных переменных в файле и их фильтра от методов, самих функций и прочего
"""

def to_keep(string):  # функция, которая убирает ненужные мне переменные(не очень универсально)
    is_keeping = True
    if 'sys' in string or 'random' in string or '__' in string or 'show_memory' in string or 'to_keep' in string:
        is_keeping = False
    return is_keeping


def show_memory(dict_of_vars, total_memory_waste=0):
    for key, value in dict_of_vars.items():
        print(key, end='\t:')
        print(sys.getsizeof(value))
        total_memory_waste += sys.getsizeof(value)

        if hasattr(value, '__iter__'):
            if hasattr(value, 'items'):
                for _key, _value in value.items:
                    print(key, end='\t:')
                    print(sys.getsizeof(value))
                    total_memory_waste += sys.getsizeof(_value)
            else:
                for item in value:
                    print(item, end='\t:')
                    print(sys.getsizeof(item))
                    total_memory_waste += sys.getsizeof(item)

    print(f'общий расход памяти на переменные: {total_memory_waste} байт')
