def list_sum(num_list):
    total = 0
    for el in num_list:
        total += el
    return total



with open('subjects.txt', encoding='utf-8') as file:
    subject_dict = {}
    lines = file.readlines()
    for el in lines:
        subject_list = el.split(':')
        hours_string = subject_list[1]
        i = 0
        hours_list = []
        while i < len(hours_string):
            hours_int = ''
            el = hours_string[i]
            while '0' <= el <= '9':
                hours_int += el
                i+= 1
                if i < len(hours_string):
                    el = hours_string[i]
                else:
                    break
            i += 1
            if hours_int != '':
                hours_list.append(int(hours_int))
        
        subject_dict[subject_list[0]] = list_sum(hours_list)
    print(subject_dict)
