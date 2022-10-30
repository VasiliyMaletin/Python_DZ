# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def write_file(name, string):
    with open(name, 'w') as f:
        f.write(string) 

def encoding(string):
    temp = ''
    encoding = '' 
    count = 1 
    if not string: 
        return '' 
    for i in string:   
        if i != temp:
            if temp: 
                encoding += str(count) + temp 
            count = 1 
            temp = i 
        else:
            count += 1 
    else: 
        encoding += str(count) + temp
    return encoding

def decoding(archive): 
    decode = '' 
    count = '' 
    for i in archive:
        if i.isdigit():
            count += i 
        else:
            decode += i * int(count)
            count = ''
    return decode 

source_string = input("Введите строку для сжатия: ")
print(f"Результат сжатия: {encoding(source_string)}")
write_file("archive.txt", encoding(source_string))
with open('archive.txt', 'r') as data:
    temp_string = data.readlines()
archive = str(temp_string).replace("['", "").replace("']", "")
print(f"Результат восстановления: {decoding(archive)}")
write_file("original.txt", decoding(archive))
