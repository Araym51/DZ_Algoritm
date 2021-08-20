"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

array = [0] * 20
for i in range(20):
    array[i] = int(random.randint(1, 100))

max_value = 0
min_value = 101
max_index = []
min_index = []

for item in array:  # ищем минимальные и максимальные значения
    if max_value <= item:
        max_value = item
    if min_value >= item:
        min_value = item

i = -1
for item2 in array:  # записываем положение максимальных и минимальных  значений
    i += 1
    if max_value == item2:
        max_index.append(i)
    if min_value == item2:
        min_index.append(i)

print(f'изначальный список:\n{array}')

for min_position in min_index:  # меняем местами максимальное значение с минимальным
    array[min_position] = max_value

for max_position in max_index:  # меняем местами минимальное значение с максимальным
    array[max_position] = min_value

print(f'изменённый список:\n{array}')

print(f'числа {max_value} и {min_value} поменялись местами')
