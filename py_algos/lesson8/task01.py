def substrings(string: str) -> int:
    """
    Определение количества различных подстрок с использованием хеш-функции
    """
    sbs = set()
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            sbs.add(hash(string[i:j]))
    return len(sbs) - 1  # отнимаю саму строку


print(substrings('papa'))
print(substrings('sova'))
