"""6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""

lang = input('введите "rus" для кириллицы или "eng" латиницы ')


if lang == 'eng':
    a = (int(input('введите номер буквы от 1 до 26: ')))
    if a <= 26:
        letter = chr(a + 96)
    else:
        print('Вы ввели неправильное число')
        exit(0)
elif lang == 'rus':
    a = (int(input('введите номер буквы от 1 до 32: ')))
    if a <= 32:
        letter = chr(a + 1071)
    else:
        print('Вы ввели неправильное число')
        exit(0)
else:
    print('Вы не выбрали язык символов')
    exit(0)

print(letter)
