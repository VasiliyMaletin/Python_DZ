# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

try:
    number = float((input("Введите число: ")).replace('.', ''))
    sum_ = 0
    remainder = 0
    remainder = number % 10
    while number != 0:
        number //= 10
        sum_ += remainder
        remainder = number % 10
    print("Сумма чисел =", sum_)

except ValueError:
    print("Нужно вводить число!!!")
