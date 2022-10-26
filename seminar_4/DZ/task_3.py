# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def coefficient_list(lst):
    result = ''
    for i in range(len(lst)):
        if len(result) > 0 and lst[i] > 0:
            result += ' + '
        if lst[i] != 0:
            result += str(lst[i])
            if coefficient - i > 1:
                result +="X**" + str(coefficient - i)
            elif coefficient - i == 1:
                result +="X"
    result += ' = 0'
    return result

try:
    coefficient = int(input("Введите степень многочлена: "))
except ValueError:
    print("Нужно вводить числа!!!")

lst = []
for _ in range(coefficient + 1):
    numbers = randint(0, 101)
    lst.append(numbers)
print(lst)
print(coefficient_list(lst))

with open('file.txt', 'w') as f:
    f.write(coefficient_list(lst))