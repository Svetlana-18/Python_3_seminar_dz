# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

number = int(input("Введите число: "))


def fibonacci(num):
    if num in [1, 2]:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


list_new = [0]
for i in range(1, number + 1):
    list_new.append(fibonacci(i))
    list_new.insert(0, (fibonacci(i) * (-1) ** (i + 1)))
print(list_new)
