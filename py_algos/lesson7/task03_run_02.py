"""
Сортировка пирамидой, альтернатива для 3 задания
"""
import random


def heap_sort(arr):
    def child_heap(array, k, j):  # функция создает кучу из куска массива, который еще не отсортирован == heapify
        new_el = array[k]
        
        while 2 * k + 1 < j:
            child = 2 * k + 1  # увеличиваю индекс дочернего прыжками

            if child + 1 < j and array[child] < array[child + 1]:  # если соседний больше
                child += 1  # меняю на соседний

            if new_el >= array[child]:
                break
            array[k] = array[child]  # переношу в родительский элемент, если он больше
            k = child
        array[k] = new_el
    n = len(arr)

    for i in range((n // 2) - 1, -1, -1):  # перебираю индексы от середины до 0
        child_heap(arr, i, n)  # в начале создаем максимальную кучу
    for ind in range(n - 1, 0, -1):
        arr[ind], arr[0] = arr[0], arr[ind]
        child_heap(arr, 0, ind)


m = int(input('введите m: '))
rndm_arr = [round(random.uniform(-34, 248), 1) for _ in range((2 * m) + 1)]
print(f'случайный массив:\n{rndm_arr}')
heap_sort(rndm_arr)
print(f'массив после сортировки:\n{rndm_arr}')
print(f'медиана:{rndm_arr[len(rndm_arr)//2]}')
