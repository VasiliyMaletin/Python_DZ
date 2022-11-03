lst = '1 2 3 5 8 15 23 38'.split()
result = map(int, lst)
result = filter(lambda x: x % 2, result) # оставляет нечётные значения 
result = list(map(lambda x: (x, x ** 2), result))
print(result)