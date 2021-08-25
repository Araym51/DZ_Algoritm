"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию:
Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
"""

import cProfile


def eratosfen(n):
    arr = [x for x in range(0, n)]
    arr[1] = 0

    for item in arr:
        if arr[item] != 0:
            value = item * 2
            while value < n:
                arr[value] = 0
                value += item

    result = []
    for i in arr:
        if arr[i] != 0:
            result.append(arr[i])

    return print(result)


def prime_num(n):
    arr = []
    for item in range(2, n):
        value = 2
        while item % value != 0:
            value += 1
            if value == item:
                arr.append(item)
    return print(arr)


cProfile.run("eratosfen(99999)")
"""
         9598 function calls in 0.087 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.087    0.087 <string>:1(<module>)
        1    0.057    0.057    0.084    0.084 Ostroumov_DZ_4-2.py:12(eratosfen)
        1    0.007    0.007    0.007    0.007 Ostroumov_DZ_4-2.py:13(<listcomp>)
        1    0.000    0.000    0.087    0.087 {built-in method builtins.exec}
        1    0.019    0.019    0.019    0.019 {built-in method builtins.print}
     9592    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
cProfile.run("prime_num(99999)")
"""
         9596 function calls in 66.233 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   66.233   66.233 <string>:1(<module>)
        1   66.210   66.210   66.233   66.233 Ostroumov_DZ_4-2.py:31(prime_num)
        1    0.000    0.000   66.233   66.233 {built-in method builtins.exec}
        1    0.014    0.014    0.014    0.014 {built-in method builtins.print}
     9591    0.009    0.000    0.009    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""