"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

symbol = input('Введите число: ')
search = int(input('Какое число ищем? '))
i = 0

for item in symbol:
    if int(item) == search:
        i += 1

if i == 0:
    print(f'цифра {search} не встречается в последовательности {symbol} ни разу')
    exit(0)
else:
    print(f'символ {search} встречается в последовательности {symbol} {i} раз')
    exit(0)
