# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

import random
n = int(input('Введите значение длинны списка чисел по порядку '))
ran = range(1, n + 1)
numbers = list(ran)
print(numbers)
# print(random.shuffle(numbers))
count = 0
for i in range(len(numbers)):
   temp = random.randint(0, n - 1 ) 
#    print(temp)
   count = numbers[i]
   numbers[i] = numbers[temp]
   numbers[temp] = count
print(numbers)

# 11 строка получаю случайное значение индекса ( n-1 индексы считаю с 0)
# 12 строка проверял работу цикла вручную
# 13 строка назначаю значение переменной текущего индекса 
# 14 строка значению текущего индекса присваиваю значение случайного
# 15 строка случайный индекс меняю на нулевой и т.д по циклу
