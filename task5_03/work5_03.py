# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
my_str = 'aaaadddddeeeeeeeeerrrr'
path = 'my_str.txt'
data = open(path, 'w')
data.write(my_str)
data.close()
data = open('my_str.txt','r')
my_str_1 = str(data.readline())
data.close()
def Сompression(str_1: str):
    str_1 += 'y'
    count = 0
    my_str_new = ''
    temp = ''
    temp = my_str[0]
    for i in str_1:
        if i == temp:
            count +=1
        else:
            # print(count)
            my_str_new += str(count) + temp
            temp = i
            count = 1
    return my_str_new
def Crushing(str_2:str):
    len_str = 0
    for i in str_2:
        len_str += 1
    new_str_2 = ''
    counter = 0
    counter_2 = 1
    while(counter_2 < len_str):
        num = int(str_2[counter]) 
        while(num) > 0:
            new_str_2 += str_2[counter_2]
            num -= 1
        counter += 2
        counter_2 += 2
    return new_str_2
new_str = Сompression(my_str)
print(f'{my_str} = {new_str}')
my_new_str = Crushing(new_str)
print(f'{new_str} = {my_new_str}')
path = 'new_str.txt'
data = open(path, 'w')
data.write(new_str)
data.close()
path = 'my_new_str.txt'
data = open(path, 'w')
data.write(my_new_str)
data.close()



   







