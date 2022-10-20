# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

def checindex_string(str_1, str_2):
    count = 0
    res = 0
    index = 0
    for i in range(len(str_1)):
        if str_1[i] == str_2[0]:
            index = i + 1
            for j in range(1, len(str_2)):
                if index != len(str_1) and str_1[index] == str_2[j]:
                    count += 1
                    index += 1
            if count == (len(str_2) - 1):
                res += 1
            count = 0
    return res

str_1 = input("Введите первую строку: ")
str_2 = input("Введите вторую строку: ")
print(f"Количество вхождений второй строки в первую = {checindex_string(str_1, str_2)}")
