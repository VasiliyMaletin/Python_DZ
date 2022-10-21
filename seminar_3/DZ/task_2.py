# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def input_lst():
    lst = [int(i) for i in input("Введите список чисел через пробел: ").split()]
    return lst

def check_lst():
    lst2 = []
    i = 0
    while i < len(lst1) / 2:
        product = lst1[i] * lst1[len(lst1) - 1 - i]
        lst2.append(product)
        i += 1
    return lst2    

try:
    lst1 = input_lst()
    print(lst1)
    print(check_lst())
except ValueError:
    print("Нужно вводить числа!!!")

