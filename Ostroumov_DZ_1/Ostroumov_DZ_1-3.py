"""3. По введенным пользователем координатам двух точек вывести
уравнение прямой вида y=kx+b, проходящей через эти точки."""

x1 = float(input('введите x1'))
y1 = float(input('введите y1'))
x2 = float(input('введите x2'))
y2 = float(input('введите y2'))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print('уравнение прямой проходящей через точки x1=%.f y1=%.f x2=%.f y2=%.f' % (x1, y1, x2, y2))
print('y=%.2f*x+%.2f' % (k, b))
