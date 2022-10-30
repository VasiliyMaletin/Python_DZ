# Напишите программу, удаляющую из текста все слова,
# содержащие "абв". Функции FIND и COUNT юзать нельзя.

text = input("Введите текст через пробел: ")
print(f"Исходный текст: {text}")
find_text = input("Введите искомое слово: ")
lst = [i for i in text.split() if find_text not in i]
print(f"Результат: {' '.join(lst)}")
