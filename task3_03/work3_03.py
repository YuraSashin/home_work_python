# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input('Задайте длинну списка: '))
numbers = []
for i in range(n):
    numbers.append(float(input('Введите вещественное значение: ')))
print(numbers)
numb = []
elem = 0
for i in range(len(numbers)):
    elem = numbers[i] - int(numbers[i])
    if elem != 0:
        numb.append(elem)
# print(numb)
max = 0
min = numb[0]
for i in range(len(numb)):
    if numb[i] > max:
        max = numb[i]
    if numb[i] < min:
        min = numb[i]
difference = 0
difference = round(max - min, 4)
print(f'Максимальная дробная часть равна {round(max,4)}, минимальная {round(min,4)}')
print(f'Разность между ними(max - min) равна {difference}')