"""5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят и сколько между ними находится букв."""

a = ord(input('Введите первый латинский символ').lower())
b = ord(input('Введите второй латинский символ').lower())

if 97 <= a <= 122:
    if 97 <= b <= 122:
        position_a = a - 97 + 1
        position_b = b - 97 + 1
    else:
        print('вводите только латинские символы')
        exit(0)
else:
    print('вводите только латинские символы')
    exit(0)

print(a)
print(b)
letters_between = position_a - position_b
print('позиция символа ', chr(a), ':', position_a)
print('позиция символа ', chr(b), ':', position_b)
print('между ',chr(a),'и', chr(b), abs(letters_between), 'букв')
