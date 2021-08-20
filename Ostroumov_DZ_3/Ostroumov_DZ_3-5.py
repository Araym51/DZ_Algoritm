"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

array = [0] * 20
value = -101
position = 0

for i in range(20):
    array[i] = int(random.randint(-100, 100))

for item in array:
    if value < item < 0:
        value = item
        position = array.index(item)

print(array)
print(f'максимальным отрицательным значением является: {value}, \n'
      f'позиция значения в массиве:{position}')
