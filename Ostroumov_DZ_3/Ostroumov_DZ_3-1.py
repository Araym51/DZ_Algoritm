"""
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

nums = [n for n in range(2, 100)]
multiple_of = {"два": 0, "три": 0, "четыре": 0, "пять": 0, "шесть": 0, "семь": 0, "восемь": 0, "девять": 0}

for item in nums:
    if item % 2 == 0:
        multiple_of["два"] += 1
    if item % 3 == 0:
        multiple_of["три"] += 1
    if item % 4 == 0:
        multiple_of["четыре"] += 1
    if item % 5 == 0:
        multiple_of["пять"] += 1
    if item % 6 == 0:
        multiple_of["шесть"] += 1
    if item % 7 == 0:
        multiple_of["семь"] += 1
    if item % 8 == 0:
        multiple_of["восемь"] += 1
    if item % 9 == 0:
        multiple_of["девять"] += 1

print(f'два кратно {multiple_of["два"]} числам\n'
      f'три кратно {multiple_of["три"]} числам\n'
      f'четыре кратно {multiple_of["четыре"]} числам\n'
      f'пять кратно {multiple_of["пять"]} числам\n'
      f'шесть кратно {multiple_of["шесть"]} числам\n'
      f'семь кратно {multiple_of["семь"]} числам\n'
      f'восемь кратно {multiple_of["восемь"]} числам\n'
      f'девять кратно {multiple_of["девять"]} числам\n')
