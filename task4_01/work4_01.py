# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def Number(text: str, error: str):
    while(True):
        try:
            number = int(input(text))
            return number
        except:
            print(error)
def Polinominal(coefficient, min, max):
    expression = ''
    for i in range(coefficient, -1, -1):
        coef = random.randint(min,max)
        if coef != 0:
            if i > 1:
                expression += f'{coef} * x ** {i} + '
            elif i == 1:
                expression += f'{coef} * x + '
            else:
                expression += f'{coef} '
    expression += '= 0'
    return expression
k = Number('Введите коэффициент К: ' , 'Введено некорректное значение')
int_min = Number('Введите минимальное значение для рандома: ' , 'Введено некорректное значение')
int_max = Number('Введите максимальное значение для рандома: ' , 'Введено некорректное значение')
polinominal_1 = Polinominal(k, int_min, int_max)
polinominal_2 = Polinominal(k, int_min, int_max)
path = 'polinominal_1.txt'
data = open(path, 'w')
data.write(polinominal_1)
data.close()
path2 = 'polinominal_2.txt'
data2 = open(path2, 'w')
data2.write(polinominal_2)
data2.close()
print(polinominal_1)
print(polinominal_2)