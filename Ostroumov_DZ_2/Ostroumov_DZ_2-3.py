"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843."""

a = input('введите число')


def reverse(a):
    if a.isdigit():
        text = a[::-1]
        return print(text)
    else:
        print('работаем только с числами')
        exit(0)


reverse(a)
