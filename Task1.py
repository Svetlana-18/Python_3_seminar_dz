# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

number = int(input('Введите длину списка  '))


def creat__list(count):
    if count < 2:
        return 'Ошибка'
    new_list = sample(range(1, count * 2), count)
    return new_list


def multiplication_elem(worker_list):
    lengt = len(worker_list)
    result_list = []

    for i in range(lengt//2):
        result = worker_list[i]*worker_list[lengt - i - 1]
        result_list.append(result)
    if lengt % 2:
        result_list.append(worker_list[lengt//2])
    return result_list


res = creat__list(number)
if res == 'Ошибка':
    print('Неверный ввод, введите целое положительное число больше единицы')
else:
    print(res)
    print(multiplication_elem(res))
