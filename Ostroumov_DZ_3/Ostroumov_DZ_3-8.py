"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
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


# генерируем строки массива
m_string_1 = m_string(3)
m_string_2 = m_string(3)
m_string_3 = m_string(3)
m_string_4 = m_string(3)
m_string_5 = m_string(3)

# считаем строки
counter(m_string_1)
counter(m_string_2)
counter(m_string_3)
counter(m_string_4)
counter(m_string_5)

# объединяем всё в одну матрицу
result = [
    m_string_1,
    m_string_2,
    m_string_3,
    m_string_4,
    m_string_5
]

# печатаем результат
for row in result:
    print(row)
