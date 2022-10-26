# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

def removing_duplicates(original_list):
    current_list = []
    for i in original_list:
         if i not in current_list:
            current_list.append(i) 
    return current_list

try:
    original_list = list(map(int, input("Введите числа через пробел: ").split()))
    print(f"Исходный список: {original_list}")
    print(f"Список без повторов: {removing_duplicates(original_list)}")
except ValueError:
    print("Нужно вводить числа через пробел!!!")
