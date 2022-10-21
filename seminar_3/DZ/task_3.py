# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def input_lst():
    lst = [round(random.uniform(-10, 11), 2) for i in range(5)]
    return lst

def separation(lst):
    lst2 = []
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] *= -1
        lst_f = round(lst[i] % 1, 2)
        lst2.append(lst_f)
    return lst2

def max_element(lst2):
    max = lst2[0]
    for i in lst2:
        if max < i:
            max = i
    return max

def min_element(lst2):
    min = lst2[0]
    for i in lst2:
        if min > i:
            min = i
    return min

lst = input_lst()
lst2 = separation(lst)
print(lst)
print(lst2)
print(f"Разница между max и min дробной части элементов = {max_element(lst2) - min_element(lst2)}")
