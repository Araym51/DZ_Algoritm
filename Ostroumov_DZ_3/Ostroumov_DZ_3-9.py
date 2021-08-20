"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random


def m_string(a):
    """
    формирует массив на заданное количество элементов
    :param a: длинна требуемого массива
    :return: возращает массив
    """
    array = [0] * a
    for i in range(a):
        array[i] = int(random.randint(1, 100))
    return array


def counter(a):
    """
    считает сумму элементов массива и записывает результат в конец массива
    :param a: передается массив
    :return: возращается массив с посчитанной суммой элементов массива
    """
    summ = 0
    for item in a:
        summ += int(item)
    return a.append(summ)



m_string_1 = m_string(3)
m_string_2 = m_string(3)
m_string_3 = m_string(3)
m_string_4 = m_string(3)
m_string_5 = m_string(3)

counter(m_string_1)
counter(m_string_2)
counter(m_string_3)
counter(m_string_4)
counter(m_string_5)

matrix = [
    m_string_1,
    m_string_2,
    m_string_3,
    m_string_4,
    m_string_5
]

# до сюда слямзил с задания 8

min_value = 100
array_min = []
for row in matrix:  # определяем минимальные значения в матрице
    for x in row:
        if x < min_value:
            min_value = x
    array_min.append(min_value)
    min_value = 100

max_value = 0
for item in array_min: # ищем максимальное значение среди минимальных значений
    if item > max_value:
        max_value = item

print('В матрице:')
for row in matrix:
    print(row)

print(f'среди минимальных значений строк 1-5 {array_min} \n'
      f'максимальное: {max_value}')
