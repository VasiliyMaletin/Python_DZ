# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# *Пример:* - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibanacchi(n):
    fib_pos = [0, 1]
    fib_neg = [0, 1]
    for i in range(2, n + 1):
        next = fib_pos[i - 1] + fib_pos[i - 2]
        if i % 2 == 0:
            fib_neg.append(-next)
        else:
            fib_neg.append(next)
        fib_pos.append(next)
    fib = fib_neg[1:][::-1] + fib_pos
    return fib

try:
    n = int(input('Введите число: '))
    print(fibanacchi(n))
except ValueError:
    print("Нужно вводить числа!!!")