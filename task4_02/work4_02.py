# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
data = open('polinominal_1.txt','r')
polinom_1 = str(data.readline())
data.close()
data = open('polinominal_2.txt','r')
polinom_2 = str(data.readline())
data.close()
print(polinom_1)
print(polinom_2)
my_list_polinom_1 = polinom_1[0:(polinom_1.find('=') -1)].split(' + ')
my_list_polinom_2 = polinom_2[0:(polinom_2.find('=') -1)].split(' + ')
# print(my_list_polinom_1)
# print(my_list_polinom_2)
end_sum = int(my_list_polinom_1[-1]) + int(my_list_polinom_2[-1])
# print(end_sum)
def Dictionary(my_list):
    dictionary = {}
    for i in range(len(my_list) - 1):
        if i < len(my_list) - 2:
            dictionary[my_list[i][(my_list[i].rfind(' ')):]] = my_list[i][0:my_list[i].find(' ')]
        elif i == len(my_list) - 2:
            dictionary['1'] = my_list[i][0:my_list[i].find(' ')]
        else:
            dictionary['0'] = my_list[i]
    return dictionary
my_dict_polinom_1 = Dictionary(my_list_polinom_1)
my_dict_polinom_2 = Dictionary(my_list_polinom_2)
# print(my_dict_polinom_1)
# print(my_dict_polinom_2)
def Sum_polinom(my_dict1: dict, my_dict2: dict):
    sum = ''
    for i in my_dict1:
        if my_dict1.get(i) == None:
            my_dict1[i] = '0'
    for i in my_dict2:
        if my_dict2.get(i) == None:
            my_dict2[i] = '0'
    for i in my_dict1:
            if i != '1':
                sum += f'{str(int(my_dict1.get(i)) + int(my_dict2.get(i)))} * x ** {i} + '
            else:
                sum += f'{str(int(my_dict1.get(i)) + int(my_dict2.get(i)))} * x ' 
    return sum
sum_polinom = Sum_polinom(my_dict_polinom_1,my_dict_polinom_2)
sum_polinom += f'+ {end_sum} = 0' 
print(sum_polinom)
path = 'polinominal_3.txt'
data = open(path, 'w')
data.write(sum_polinom)
data.close()