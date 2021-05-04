from function_for_test import reversed_bubble_sort, merge_sort, median, heap_sort
import random


def bubble_test(number=1000):
    for i in range(number):
        arr = [random.randint(-100, 100) for _ in range(23)]
        my_copy = arr[:]  # для теста копирую массив для стандартной сортировки и своей
        copy_standart = arr[:]
        reversed_bubble_sort(my_copy)
        copy_standart.sort(reverse=True)

        for j in range(len(arr)):
            if my_copy[j] != copy_standart[j]:
                print(f'ошибка в массиве: {arr}\n'
                      f'встроенная сортировка: {copy_standart}\n'
                      f'написанная сортировка: {my_copy}\n')
                return 1

    print('bubble sort: everything is alright')
    return 0


bubble_test()


def merge_test(number=1000):
    for i in range(number):
        arr = [random.uniform(0, 50) for _ in range(23)]
        copy_standart = arr[:]
        my_copy = merge_sort(arr)  # слияние возвращает другой массив
        copy_standart.sort()

        for j in range(len(arr)):
            if my_copy[j] != copy_standart[j]:
                print(f'ошибка в массиве: {arr}\n'
                      f'встроенная сортировка: {copy_standart}\n'
                      f'написанная сортировка: {my_copy}\n')
                return 1

    print('merge sort: everything is alright')
    return 0


merge_test()


def median_test(number=1000):
    for i in range(number):
        arr = [round(random.uniform(-100, 200), 1) for _ in range(23)]
        sorted_copy = sorted(arr)
        sorted_median = sorted_copy[len(arr)//2]
        my_median = median(arr)

        if my_median != sorted_median:
            print(f'медианы не совпали\nмассив:\n{arr}'
                  f'настоящая медиана:{sorted_median}, результат функции: {my_median}')
            return 1
    print(f'median is fine')
    return 0


median_test()


def heap_test(number=1000):
    for i in range(number):
        arr = [random.uniform(0, 50) for _ in range(23)]
        copy_standart = arr[:]
        heap_sort(arr)  # слияние возвращает другой массив
        copy_standart.sort()

        for j in range(len(arr)):
            if arr[j] != copy_standart[j]:
                print(f'ошибка в массиве: {arr}\n'
                      f'встроенная сортировка: {copy_standart}\n'
                      f'написанная сортировка: {arr}\n')
                return 1

    print('heap sort: everything is alright')
    return 0


heap_test()
