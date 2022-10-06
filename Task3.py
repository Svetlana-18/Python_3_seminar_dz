# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

from random import uniform


def list_rand_num(count: int):
    list_num = []
    if count <= 2:
        return "Ошибка"

    for i in range(count):
        list_num.append(round(uniform(1, count), 2))
    return list_num


def dif_max_min(list_num: list):
    num_max = num_min = list_num[0] % 1

    for k in range(1, len(list_num)):
        num = round(list_num[k] % 1, 2)
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num
    result = round(num_max - num_min, 2)
    print(f"Min: {num_min}, Max: {num_max}")
    return result


all_list = list_rand_num(int(input("Введите число: ")))
if all_list == 'Ошибка':
    print('Неверный ввод, введите целое положительное число больше единицы')
else:
    print(all_list)
    print(dif_max_min(all_list))
