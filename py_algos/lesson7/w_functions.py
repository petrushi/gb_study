"""
Функции без вызовов для тестов
"""


def reversed_bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        sorted_ = True

        for k in range(0, n - i):  # i элементов уже отсортированы, можно до них не идти
            if arr[k] < arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
                sorted_ = False
        if sorted_:  # если свопов не было, завершаю сортировку
            return arr
    return arr


def merge_sort(arr):
    def merge(lft, rgt):  # добавил одну функцию в другую, потому что тесты не делались нормально
        result = []
        i = j = 0
        while i < len(lft) and j < len(rgt):
            if lft[i] <= rgt[j]:
                result.append(lft[i])
                i += 1
            else:
                result.append(rgt[j])
                j += 1
        result += lft[i:]
        result += rgt[j:]
        return result

    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def median(arr):
    floor = float('-inf')  # нижняя граница проверяемых чисел
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


def heap_sort(arr):
    def child_heap(array, k, j):  # функция создает кучу из куска массива, который еще не отсортирован == heapify
        new_el = array[k]
        while 2 * k + 1 < j:
            child = 2 * k + 1
            if child + 1 < j and array[child] < array[child + 1]:
                child += 1
            if new_el >= array[child]:
                break
            array[k] = array[child]
            k = child
        array[k] = new_el

    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        child_heap(arr, i, n)  # в начале создаем максимальную кучу
    for ind in range(n - 1, 0, -1):
        arr[ind], arr[0] = arr[0], arr[ind]

        child_heap(arr, 0, ind)
