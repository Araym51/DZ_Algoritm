"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random

array = [0] * 20
result = {}
max_value = None
max_cnt = 0

for i in range(20):
    array[i] = int(random.randint(1, 100))

array = array + array[10:] + array[5:] + array[0:]  # формируем массив, в котором точно будут повторяющиеся значения

for item in array:  # заполняем словарь
    result.setdefault(item, 0)
    result[item] += 1

for value, cnt in result.items():  # считаем сколько раз встречается значение
    if cnt > max_cnt:
        max_value = value
        max_cnt = cnt

print(f'число {max_value} встречается {max_cnt} раз')
