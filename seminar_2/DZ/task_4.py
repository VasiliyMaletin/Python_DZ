# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

try:
    n = int(input("Введите число N: "))
    interval = []
    for i in range((-n), n+1):
        interval.append(i)
    print(interval)

    path = 'file.txt'
    data = open(path, 'r')
    product = 1
    for line in data:
        product *= interval[int(line)]

    print(product)
    data.close()

except ValueError:
    print("Нужно вводить число!!!")
