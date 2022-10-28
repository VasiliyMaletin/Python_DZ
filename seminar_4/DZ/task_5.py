# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def write_file(name, polynomial):
    with open(name, 'w') as f:
        f.write(polynomial) 

def create_string(polynomial):
    lst = polynomial[::-1]
    string_polynomial = ''
    if len(lst) < 1:
        string_polynomial = 'X = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                string_polynomial += f'{lst[i]}X^{len(lst) - i - 1}'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    string_polynomial += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                string_polynomial += f'{lst[i]}X'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    string_polynomial += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                string_polynomial += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                string_polynomial += ' = 0'
    return string_polynomial

def sq_mn(coefficient):
    if 'X^' in coefficient:
        i = coefficient.find('^')
        num = int(coefficient[i + 1:])
    elif ('X' in coefficient) and ('^' not in coefficient):
        num = 1
    else:
        num = -1
    return num

def k_mn(coefficient):
    if 'X' in coefficient:
        i = coefficient.find('X')
        num = int(coefficient[:i])
    return num

def calc_mn(polynomial):
    polynomial = polynomial[0].replace(' ', '').split('=')
    polynomial = polynomial[0].split('+')
    lst = []
    length_polynomial = len(polynomial)
    coefficient = 0
    if sq_mn(polynomial[-1]) == -1:
        lst.append(int(polynomial[-1]))
        length_polynomial -= 1
        coefficient = 1
    degree = 1
    index = length_polynomial - 1
    while index >= 0:
        if sq_mn(polynomial[index]) != -1 and sq_mn(polynomial[index]) == degree:
            lst.append(k_mn(polynomial[index]))
            index -= 1
            degree += 1
        else:
            lst.append(0)
            degree += 1
    return lst 

with open('file.txt', 'r') as f:
    lst_f = f.readlines()
with open('file2.txt', 'r') as f2:
    lst_f2 = f2.readlines()
print(f"Первый многочлен: {lst_f}")
print(f"Второй многочлен: {lst_f2}")
polynomial_1 = calc_mn(lst_f)
polynomial_2 = calc_mn(lst_f2)
min_length = len(polynomial_1)
if len(polynomial_1) > len(polynomial_2):
    min_length = len(polynomial_2)
polynomial_3 = [polynomial_1[i] + polynomial_2[i] for i in range(min_length)]
if len(polynomial_1) > len(polynomial_2):
    max_length = len(polynomial_1)
    for i in range(min_length, max_length):
        polynomial_3.append(polynomial_1[i])
else:
    max_length = len(polynomial_2)
    for i in range(min_length, max_length):
        polynomial_3.append(polynomial_2[i])
        
write_file("file3.txt", create_string(polynomial_3))
with open('file3.txt', 'r') as f3:
    lst_f3 = f3.readlines()
print(f"Сумма многочленов: {lst_f3}")
