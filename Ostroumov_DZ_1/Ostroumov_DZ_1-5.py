"""5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят и сколько между ними находится букв."""

a = ord(input('Введите первый латинский символ').lower())
b = ord(input('Введите второй латинский символ').lower())

position_a = a - 97 + 1
position_b = b - 97 + 1
letters_between = position_a - position_b
print('позиция символа ', chr(a), ':', position_a)
print('позиция символа ', chr(b), ':', position_b)
print('между ',chr(a),'и', chr(b), abs(letters_between), 'букв')
