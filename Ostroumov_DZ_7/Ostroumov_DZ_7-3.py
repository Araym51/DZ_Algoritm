"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках
"""

import random


def array_gen(m):
    """
    формирует массив на заданное количество элементов
    :param m: длинна требуемого массива
    :return: возращает массив
    """
    m = 2 * m + 1
    array = [0] * m
    for i in range(m):
        array[i] = int(random.randint(0, 999))
    return array


arr = array_gen(10)


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


print(f'несортированный список:\n{arr}')
heap_sort(arr)
median_index = len(arr) // 2
print(f'медиана: {arr[median_index]}')
print(f'отсортированный список:\n{arr}')

# мой первоначальный вариант, как выяснилось неправильный:
# max_value = 0
# mid_value_1 = 0
# mid_value_2 = 0
#
# for item in arr:  # ищем максимальное значение
#     if item > max_value:
#         max_value = item
#
# half_max_value = max_value // 2  # половина от максимального значения будет точкой осчета для медианы
#
# for item in arr:  # ищем значение ближайшее к половине максимального, но меньше его
#     if half_max_value > item:
#         mid_value_1 = item
#         if mid_value_2 < mid_value_1:
#             mid_value_2 = mid_value_1
#
# les_then_max = mid_value_2
# mid_value_2 = max_value  # для корректного сравнения задаем промежуточной переменной максимальное значение массива
#
# for item in arr: # ищем значение ближайшее к половине максимального, но больше его
#     if max_value > item > half_max_value:
#         mid_value_1 = item
#         if mid_value_2 > mid_value_1:
#             mid_value_2 = mid_value_1
#
# more_then_max = mid_value_2
#
# result_more = more_then_max - half_max_value  # вычисляем, кто ближе к половине от максимума массива
# result_less = half_max_value - les_then_max
#
# if result_more > result_less:
#     print(f'медиана массива {les_then_max}')
# else:
#     print(f'медиана массива {more_then_max}')
#
#
# print(f'массив: \n{arr}')
# print(f'отсортированный массив: \n{sorted(arr)}')
