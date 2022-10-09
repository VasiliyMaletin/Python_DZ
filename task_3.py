# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

try:
    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            print("Координаты находятся в плоскости 1")
        elif x < 0 and y > 0:
            print("Координаты находятся в плоскости 2")
        elif x < 0 and y < 0:
            print("Координаты находятся в плоскости 3")
        else: print("Координаты находятся в плоскости 4")
    else: print("Координаты находятся на нулевой точке")
except:
    print("Нужно вводить числа!!!")