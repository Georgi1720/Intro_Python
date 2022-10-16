# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции. Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

some_list = []
for _ in range(1,random.randint(2,10)):
    some_list.append(random.randint(1,100))

print(f'Исходный список - {some_list}')
sum = 0
for i in range(len(some_list)):
    if i % 2 != 0:
        sum += some_list[i]
print(f'Сумма нечетных позиций = {sum}')