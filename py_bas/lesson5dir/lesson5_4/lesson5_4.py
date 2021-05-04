with open('english_numbers.txt') as file:
    lines = file.readlines()
    ru_lines = []
    with open('russian_numbers.txt', 'w') as ru_file:
        for el in lines:
            ru_lines.append(el.replace('One', 'Один')
            .replace('Two', 'Два')
            .replace('Three', 'Три')
            .replace('Four', 'Четыре')
            )
        ru_file.writelines(ru_lines)
