# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = str(input('Введите любое вещественное число: '))
# sum = 0
# number1 = number.replace('.','')
# for i in range(len(number1)):
#     sum += int(number1[i])
# print(f'Сумма цифр числа {number} равна {sum}')

# Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Введите целое число N: '))
# a = 1
# list = []
# for i in range(1, N + 1):
#     a *= i
#     list.append(a)
# print(list)

# Задайте список из n чисел последовательности (1 + 1/n) ** n
# и выведите на экран их сумму.

# Пример:
# -Для n = 4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

# n = int(input('Введите n: '))
# sum = 0
# p = 0
# print('{', end='')
# for i in range(1, n):
#     p = (1 + 1 / i) ** i
#     sum += p
#     print(f'{i}: {round(p, 2)}', end=', ')
# print(f'{i}: {round((1 + 1 / n) ** n, 2)}', end='')
# print('}')
# print(f'Сумма элементов списка равна {round(sum + (1 + 1 / n) ** n, 2)}')

# Реализуйте алгоритм перемешивания списка.
# Вариант 1 - с использованием shuffle
# import random
# list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list)
# random.shuffle(list)
# print(list)

# Вариант 2 - без использования shuffle
# import random
# list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list)
# temp = 0
# for i in range(len(list)):
#     a = random.randrange(i, len(list))
#     if a != i:
#         temp = list[i]
#         list[i] = list[a]
#         list[a] = temp
# print(list)