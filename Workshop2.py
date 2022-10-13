#-----------------------------------------Семинар 2 задание 1-----------------------------------------#
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
import random

float_value = input('Введите число с плавающей запятой: ')
sum_elements = 0
for i in float_value:
    try:
        sum_elements += int(i)
    except:
        continue
print(f'Сумма элементов введенного числа = {sum_elements}')

#-----------------------------------------Семинар 2 задание 2-----------------------------------------#
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите число: '))
# mul = 1
# factorial_list = []
# for i in range(1, number+1):
#     mul *= i
#     factorial_list.append(mul)
# print(factorial_list)

#-----------------------------------------Семинар 2 задание 3-----------------------------------------#
# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

# number = int(input('Введите число: '))
# result = 0
# sum_value = 0
# output_list = []
# for i in range(1, number+1):
#     result = (1 + (1 / i)) ** i
#     sum_value += result
#     output_list.append(f'{i}: {round(result,2)}')
# print(output_list, sep=',')
# print(f'Сумма последовательности чисел равна = {round(sum_value,2)}')

#-----------------------------------------Семинар 2 задание 4-----------------------------------------#
# Реализуйте алгоритм перемешивания списка.

# initial_list = [1,2,3,4,5,6,7,8,9]
# size = len(initial_list)
# print(initial_list)
#
# for i in range(size-1,0,-1):
#     j = random.randint(0,size-1)
#     initial_list[i], initial_list[j] = initial_list[j], initial_list[i]
# print(initial_list)

#-----------------------------------------Семинар 2 задание 5-----------------------------------------#
# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2] Надо вернуть их пересечение
# [1, 2, 2, 3] (порядок не важен)

# first_list = [1, 2, 3, 2, 0]
# size_first = len(first_list)
# second_list = [5, 1, 2, 7, 3, 2]
# size_second = len(second_list)
# output_list = []
#
# for i in range(0,size_first):
#     tmp = first_list[i]
#     for j in range(0,size_second):
#         if second_list[j] == tmp:
#             output_list.append(tmp)
#             break
#
# # Если алгоритмы не подразумевают метод .append() и его нельзя использовать то можно сделать так
# # counter = 0
# # for i in range(0,size_first):
# #     tmp = first_list[i]
# #     for j in range(0,size_second):
# #         if second_list[j] == tmp:
# #             counter += 1
# #             break
# #
# # output_list = [0] * counter
# # counter = 0
# #
# # for i in range(0,size_first):
# #     tmp = first_list[i]
# #     for j in range(0,size_second):
# #         if second_list[j] == tmp:
# #             output_list[counter] = tmp
# #             counter += 1
# #             break
#
# print(output_list)

#-----------------------------------------Семинар 2 задание 6-----------------------------------------#
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# number = int(input('Введите число: '))
#
# with open('text.txt','w') as file:
#     for _ in range(4):
#         file.writelines(f'{random.randint(0, number * 2)}\n')
# index_list = []
# with open('text.txt','r') as file:
#     for line in file:
#         index_list.append(line.strip())    # от каретки всегда нужно будет избавляться подобным способом?
#
# print(f'Индексы из text.txt - {index_list}')
# mul = 1
# number_list = list(range(-number, number+1))
# for item in index_list:
#     mul *= number_list[int(item)]
# print(f'Основной список - {number_list}')
# print(f'Сумма элементов = {mul}')


