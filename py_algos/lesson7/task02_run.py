"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = merge_sort(left)  # рекурсивно вызываю функцию, пока длина правой и левой части не станет равна 1
    right = merge_sort(right)
    return merge(left, right)  # вызываю функцию слияния двух массивов


def merge(lft, rgt):
    result = []
    i = j = 0
    while i < len(lft) and j < len(rgt):
        if lft[i] <= rgt[j]:  # если левая часть больше или равна, добавляю к рез. массиву и беру след. из подмассива
            result.append(lft[i])
            i += 1
        else:
            result.append(rgt[j])
            j += 1
    result += lft[i:]  # когда один подмассив кончается, добавляю оставшееся
    result += rgt[j:]
    return result


rndm_arr = [round(random.uniform(0, 50), 3) for _ in range(10)]
print(f'изначальный массив:\n{rndm_arr}')
print(f'массив после сортировки:\n{merge_sort(rndm_arr)}')
