# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# *Пример:*
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

try:
    number = int(input("Ввведите число: "))
    prod = []
    count = 1
    if number < 0:
        number *= (-1)
    else:
        for i in range(1, number + 1):
            count *= i
            prod.append(count)
        print(prod)

except ValueError:
    print("Нужно вводить число!!!")
