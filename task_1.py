# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

try:
    day = int(input("Введите день недели: "))
    if 8 > day > 5:
        print("Выходной")
    elif 0 < day < 6:
        print("Рабочий")
    else:
        print("В неделе 7 дней!!!")
except:
    print("Нужно вводить числа!!!")
