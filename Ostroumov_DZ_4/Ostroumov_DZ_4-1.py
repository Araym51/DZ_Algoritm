"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

    3-7. В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random
import cProfile


def array_gen(a):
    """
    формирует массив на заданное количество элементов
    :param a: длинна требуемого массива
    :return: возращает массив
    """
    array = [0] * a
    for i in range(a):
        array[i] = int(random.randint(1, 100000))
    return array


a = array_gen(9999)


def array_1(arr):
    min_1 = 101
    min_2 = 101

    for item in arr:  # ищем первое минимальное значение
        if item <= min_1:
            min_1 = item

    arr.pop(arr.index(min_1))  # из массива удаляем первое найденное минимальное значение

    for item2 in arr:  # ищем второе минимальное значение
        if item2 <= min_2:
            min_2 = item2

    return print(f'минимальные значения в массиве: {min_1} и {min_2}')


"""
результат:
минимальные значения в массиве: 1 и 16
         7 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 Ostroumov_DZ_4-1.py:29(array_1)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
"""


b = array_gen(9999)


def array_2(arr):  # во втором алгоритме мы сначала сортируем массив, потом берем его первые минимальные значения
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return print(f'минимальные значения в массиве: {arr[0]} и {arr[1]}')


"""
результат:
минимальные значения в массиве: 10 и 16
         10005 function calls in 5.705 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    5.705    5.705 <string>:1(<module>)
        1    5.702    5.702    5.705    5.705 Ostroumov_DZ_4-1.py:49(array_2)
        1    0.000    0.000    5.705    5.705 {built-in method builtins.exec}
    10000    0.003    0.000    0.003    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

cProfile.run('array_1(a)')
cProfile.run('array_2(b)')
