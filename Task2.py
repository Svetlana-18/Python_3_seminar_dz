# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

num = int(input('Введите десятичное число  '))


def creat__list(number):
    result = []
    if number < 0:
        return 'Ошибка'
    elif number == 0:
        return '0'
    else:
        while number > 0:
            result.append(number % 2)
            number //= 2
        result.reverse()
        return result


res = creat__list(num)
if res == 'Ошибка':
    print('Неверный ввод, введите положительное целое число')
else:
    print(res)
