"""4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ."""

import random
from random import choice
from string import ascii_lowercase

a = random.randint(1, 1000)
b = float(random.randint(10000000, 999999999))
с = ''.join(choice(ascii_lowercase) for i in range(1))
i = 0

while b > 1:
    b = b / 10
    i += 1

print(a)
print('%.5f*10 в степени %.f' % (b, i))
print(с)
