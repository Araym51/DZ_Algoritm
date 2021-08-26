"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

factories = {}
n = int(input('Количество предприятий: '))
profit = 0
profit_list = []
result = 0

if n <= 0:
    print('Считаем прибыль если предприятие хотя бы одно')
    exit(0)
else:
    for i in range(n):
        f_name = (str(i+1) + "-е предприятие:")
        print(f_name)
        profit = input('Введите прибыль предприятия по кварталам через пробел')
        profit_list = profit.split()
        if len(profit_list) != 4:
            print('вводить нужно 4 числа через пробел')
            exit(0)
        else:
            for j in profit_list:
                if j.isdigit():
                    result += int(j)
                else:
                    print('Вводить нужно числа')
                    exit(0)
        factories[f_name] = result / 4
        result = 0

for k, v in factories.items():
    result += int(v)

average = result / n
hi_average = {}
low_average = {}
print(f'средняя прибыль по предприятиям: {average}')

for k, v in factories.items():
    if v > average:
        hi_average[k] = v
    elif v < average:
        low_average[k] = v

print(f'предприятия с доходом выше среднего:\n{hi_average}')
print(f'предприятия с доходом ниже среднего:\n{low_average}')
