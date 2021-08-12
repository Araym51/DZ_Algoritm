"""2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат."""

a = str(101)
b = str(110)

a = int(a, 2)
b = int(b, 2)

bit_or = a | b
bit_and = a & b
bit_xor = a ^ b
bit_left_shift = a << 2
bit_right_shift = a >> 2
print(" OR: %s" % bin(bit_or))
print("AND: %s" % bin(bit_and))
print("XOR: %s" % bin(bit_xor))
print("побитовый сдвиг 5 влево на 2 знака: ", bin(bit_left_shift),
      '\nв десятичной системе: ', bit_left_shift)  # при сдвиге влево мы добавляем дополнительные нули к двоичному
# числу, тем самым увеличивая его

print("побитовый сдвиг 5 вправо на 2 знака: ",  bin(bit_right_shift),
      '\nв десятичной системе: ', bit_right_shift)  # при сдвиге вправо мы отсекаем заданное количество знаков, тем
# самым уменьшая его