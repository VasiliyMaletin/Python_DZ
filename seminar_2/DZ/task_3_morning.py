# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

def create_string_list(number):
    list = []
    for i in range(number):
        list.append(input(f'Введите {i + 1}-й элемент строки: '))
    return list

def check_string(str_1, str_2):
    count = 0
    i = -1
    for i in str_1:
        if str_2 == i:
            count += 1
    return count

size = int(input('Введите количество элементов строки: '))
str_1 = create_string_list(size)
str_2 = input('Введите вторую строку: ')
if check_string(str_1, str_2) == (-1):
    print('Нет повторов')
else:
    print(f"Количество вхождений второй строки в первую = {check_string(str_1, str_2)}")
