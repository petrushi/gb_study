from collections import deque, Counter
CODE = deque('01')


def cipher(string: str, cd, prefix='', fin_dict=None) -> dict:
    """
    Функция производит что-то вроде шифрования Хаффмана без классов
    """
    def string_to_deq(str_):
        s = Counter()
        for k in str_:
            s[k] += 1
        while len(s) > 2:
            left, right = s.most_common()[:-3:-1]
            par = (left[0], right[0]), left[1] + right[1]  # создаю "родителя"
            del s[left[0]], s[right[0]]
            s[par[0]] = par[1]
        return deque(s)

    if fin_dict is None:
        fin_dict = {}
    for x in string_to_deq(string):
        if type(x) == str:
            fin_dict[x] = prefix+cd[0]
        else:
            n_prefix = prefix + cd[0]
            cipher(x, cd, n_prefix, fin_dict)
        cd.rotate()
    return fin_dict


for i in ('beep boop beer!', 'abcabcabc', 'now is better than never'):
    print(f'строка:\n{i}')
    print(f'алфавит для кодировки:\n{cipher(i, CODE)}')
    coded_string = ''
    for j in i:
        coded_string += cipher(i, CODE)[j] + ' '
    print(f'закодированная строка:\n{coded_string}\n')
