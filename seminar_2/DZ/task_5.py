# Реализуйте алгоритм перемешивания списка.

import time

my_list = []
for i in range(1, 21):
    my_list.append(i)
print(my_list)


index = []
for i in my_list:
    index = int(time.time() % 10000) % i
    time.sleep(0.01)
    temp = my_list[i]
    my_list[i] = my_list[index]
    my_list[index] = temp
print(my_list)
    