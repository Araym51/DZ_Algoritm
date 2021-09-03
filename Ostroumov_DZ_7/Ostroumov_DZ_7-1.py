""""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными
числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
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
        array[i] = int(random.randint(-100, 100))
    return array


arr = array_gen(100)
print(f'исходный массив:\n {arr}')


def buble(array):
    length = len(array)
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


buble(arr)

print(f'отсортированный массив:\n {arr}')
