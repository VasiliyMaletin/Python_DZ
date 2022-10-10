# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.
# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!
# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0
# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

try:
    first_number = float(input("Введите первое число: "))
    second_nember = float(input("Введите второе число: "))
    operation = input("Введите операцию: ")
    if second_nember == 0 and (operation == 'mod' or 'div' or '/'):
        print("Деление на 0!")
    elif operation == 'mod':
        print(first_number % second_nember)
    elif operation == 'div':
        print(first_number // second_nember)
    elif operation == '/':
        print(first_number / second_nember)
    elif operation == '+':
        print(first_number + second_nember)
    elif operation == '-':
        print(first_number - second_nember)
    elif operation == '*':
        print(first_number * second_nember)
    elif operation == 'pow':
        print(first_number ** second_nember)
    else: print("Вводите операции из списка: +, -, /, *, mod, pow, div")
except: print("Нужно вводить числа!!!")   