"""9. Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого)."""

a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
c = int(input('введите третье число: '))

if a < b < c:
    print('средним является число: ', b)
elif c < b < a:
    print('средним является число: ', b)
elif b < a < c:
    print('средним является число: ', a)
elif c < a < b:
    print('средним является число: ', a)
elif b < c < a:
    print('средним является число: ', c)
else:
    print('средним является число: ', c)
