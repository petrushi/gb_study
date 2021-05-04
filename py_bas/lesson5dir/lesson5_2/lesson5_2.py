with open('text_file.txt') as file:
    lines = file.readlines()
    print(f'Количество строк в файле - {len(lines)}')
    i = 0
    while i < len(lines):
        symbols = len(lines[i])
        print(f'Количество символов в строке {i+1} - {symbols}')
        i += 1
