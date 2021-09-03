"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def array_gen(n):
    """
    формирует массив на заданное количество элементов
    :param n: длинна требуемого массива
    :return: возращает массив
    """
    array = [0] * n
    for i in range(n):
        array[i] = int(random.randint(0, 50))
    return array


array = array_gen(20)


def merge(arr_1, arr_2):
    """
    функция сборки из двух массивов в один отсортированный массива
    :param arr_1: передается первый отсортированный массив
    :param arr_2: передается второй отсортированный массив
    :return: возвращает "склееный" массив
    """
    result_arr = []
    i = j = 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            result_arr.append(arr_1[i])
            i += 1
        else:
            result_arr.append(arr_2[j])
            j += 1
    while i < len(arr_1):
        result_arr.append(arr_1[i])
        i += 1
    while j < len(arr_2):
        result_arr.append(arr_2[j])
        j += 1
    return result_arr


def merge_sort(arr):
    """
    принимает список, разделяет его на индивидуальные элементы, сортирует,
    собирает в сортированный список
    :param arr: список
    :return: возвращает отсортированный список
    """
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


print(array)
print(merge_sort(array))
