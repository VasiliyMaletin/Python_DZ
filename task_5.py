# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

try:
    from math import sqrt
    print("Введите координаты точки A:")
    point_a_x = float(input("x = "))
    point_a_y = float(input("y = "))
    print("Введите координаты точки B:")
    point_b_x = float(input("x = "))
    point_b_y = float(input("y = "))
    print("Расстояние между точкой A и B =",round(sqrt((point_a_x - point_b_x)**2 + (point_a_y - point_b_y)**2), 2)) 
except:
    print("Нужно вводить числа!!!")