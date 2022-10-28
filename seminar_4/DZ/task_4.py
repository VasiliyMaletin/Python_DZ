# Вычислить число Pi c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141

from decimal import Decimal

def num_pi(accuracy):
    numerator = 1
    count = 1
    while accuracy < 1:
        accuracy *= 10
        count += 1
    number_pi = 0
    for numerator in range(1, 10000001):
        number_pi += 4 * ((-1) ** (numerator + 1)) / (2 * numerator - 1)
    number_pi = round(number_pi, count)
    return number_pi

try:
    accuracy = Decimal(input("Введите точность числа π (например: 0.001): "))
    print(str(f'Число π с точностью {accuracy} = {num_pi(accuracy)}')[:-1])
except ValueError:
    print("Нужно вводить точность числами!!!")
