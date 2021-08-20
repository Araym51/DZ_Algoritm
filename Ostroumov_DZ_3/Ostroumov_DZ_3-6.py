"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

array = [0] * 20
for i in range(20):
    array[i] = int(random.randint(1, 100))

max_value = 0
min_value = 101
max_index = 0
min_index = 0

for item in array:
    if max_value <= item:
        max_value = item
        max_index = array.index(max_value)
    if min_value >= item:
        min_value = item
        min_index = array.index(min_value)  # до сюда код нагло тащим с 3го задания

if min_index < max_index:  # модифицируем индексы для правильного среза
    min_index += 1
else:
    max_index += 1

result = 0
for i in array[min_index:max_index]:
    result += i

print(f'сумма элементов между элементами {max_value} и {min_value} составляет: {result}\n'
      f'в одномерном массиве: \n{array}')
