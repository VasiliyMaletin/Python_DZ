# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
 
def multiplier_list(n):
   
   lst = []
   for i in range(2, n + 1):
       while n % i == 0:
           lst.append(i)
           n = n // i
       i += 1
   if n > 1:
       lst.append(n)
   return lst
    
try:
    n = int(input("Введите число: "))
    print(f"Список множителей числа {n}: {multiplier_list(n)}")
except ValueError:
    print("Нужно вводить числа!!!")
    