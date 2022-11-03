# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import sample

# lst = sample(range(1, 21), 10)
# print(lst)

# def sum_odd(lst):
#     sum = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             sum += lst[i]
#     return sum

# print(f"Сумма элементов на нечётных позициях = {sum_odd(lst)}")

lst = sample(range(1, 21), 10)
print(list(enumerate(lst)))
lst = [lst[i] for i in range(len(lst)) if i % 2 != 0]
print(lst)
print(f"Сумма элементов на нечётных позициях = {sum(lst)}")