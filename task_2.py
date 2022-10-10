# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

flag = True
for x in range(2):
    for y in range(2):
        for z in range(2):
            not (x or y or z) == (not x and not y and not z)
            print(x,y,z, not (x or y or z) == (not x and not y and not z))
            if not (x or y or z) != (not x and not y and not z):
                flag = False
if flag == True:
    print("Утверждение истинно")
else: print("Утверждение ложно")
                