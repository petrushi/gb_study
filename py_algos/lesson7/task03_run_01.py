"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.

Медиана подсчетом, без словаря и сортировки. Нормально, если медиана где-то в начале

"""
import random


def median(arr):
    floor = float('-inf')  # нижняя граница проверяемых чисел, обновляемые границы сильно ускорили программу
    ceil = float('inf')  # верхняя граница
    n = len(arr)
    if n % 2 == 0:
        print('в массиве четное количество элементов')
        return None
    for i in range(n):
        if floor < arr[i] < ceil:
            same = left = right = 0

            for j in range(n):
                if arr[i] < arr[j]:
                    right += 1
                elif arr[i] > arr[j]:
                    left += 1
                else:  # если элемент равен или тот же
                    same += 1
                if right > n // 2 or left > n // 2:  # если правых или левых больше половины длины
                    if right > left:  # если справа больше половины, выхожу из цикла и обновляю нижнюю границу
                        floor = arr[i]
                    else:
                        ceil = arr[i]  # или верхнюю
                    break
            if abs(right - left) < same:  # если разница больших и меньших < кол-ва эл-та в массиве
                return arr[i]


m = int(input('введите m: '))
rndm_arr = [round(random.uniform(-1090, 200), 1) for _ in range((2 * m) + 1)]
print(f'изначальный массив:\n{rndm_arr}')
print(f'медиана:{median(rndm_arr)}')
print(f'средний элемент отсортированного массива:{sorted(rndm_arr)[len(rndm_arr)//2]}')

