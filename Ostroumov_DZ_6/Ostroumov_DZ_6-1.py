"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
/// версия Python 3.9
/// Windows 10 pro x64
/// 3-8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

import random
import sys

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
counter(m_string_1)
result = [m_string_1]
result_3 = sys.getsizeof(result) + sys.getsizeof(m_string_1)
print(f'{sys.getsizeof(result) = }, {sys.getsizeof(m_string_1) = },\n'
      f'общее количество затраченной памяти: {result_3}\n \n \n')

"""
sys.getsizeof(result) = 64, sys.getsizeof(m_string_1) = 120,
общее количество затраченной памяти: 184

/// 3 - 1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

nums = [n for n in range(2, 100)]
multiple_of = {"два": 0, "три": 0, "четыре": 0, "пять": 0, "шесть": 0, "семь": 0, "восемь": 0, "девять": 0}
# для анализа ввожу дополниетельные переменные:
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

for item in nums:
    if item % 2 == 0:
        multiple_of["два"] += 1
        two += 1
    if item % 3 == 0:
        multiple_of["три"] += 1
        three += 1
    if item % 4 == 0:
        multiple_of["четыре"] += 1
        four += 1
    if item % 5 == 0:
        multiple_of["пять"] += 1
        five += 1
    if item % 6 == 0:
        multiple_of["шесть"] += 1
        six += 1
    if item % 7 == 0:
        multiple_of["семь"] += 1
        seven += 1
    if item % 8 == 0:
        multiple_of["восемь"] += 1
        eight += 1
    if item % 9 == 0:
        multiple_of["девять"] += 1
        nine += 1

result_1 = sys.getsizeof(nums) + sys.getsizeof(multiple_of)
result_2 = two + three + four + five + six + seven + eight + nine + sys.getsizeof(nums)
print(f'{sys.getsizeof(nums) = }, {sys.getsizeof(multiple_of) = }, всего {result_1}')
print(f'каждая "индивдуальная" переменная будет занимать  {two} памяти')
print(f'без словаря, с индивидуальными переменными: {result_2}')

'''
sys.getsizeof(nums) = 920, sys.getsizeof(multiple_of) = 360, всего 1280
каждая "индивдуальная" переменная будет занимать  49 памяти
без словаря, с индивидуальными переменными: 1098
'''
