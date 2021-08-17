"""5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке."""

symbol = 32
result = ''
i = 0

while symbol <= 127:
    result = result + chr(symbol) + ' - ' + str(symbol) + ', '
    i += 1
    symbol += 1
    if i % 10 == 0:
        result = result + ' \n'

print(result)
