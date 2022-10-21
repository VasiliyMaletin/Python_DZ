# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное. Нельзя использовать готовые функции.

def bin_num(number):
    number_bin = ""
    while number > 0:
        reminder = number % 2
        number //= 2
        number_bin += str(reminder)
    number_bin = number_bin[::-1]
    return number_bin

try:
    number = int(input("Введите число: "))
    print(bin_num(number))
except ValueError:
    print("Нужно вводить числа!!!")