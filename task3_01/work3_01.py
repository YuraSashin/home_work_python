# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

n = int(input('Задайте длинну списка: '))
numbers = []
for i in range(n):
    numbers.append(int(input('Введите значение: ')))
print(numbers)
sum = 0
for i in range(len(numbers)):
    if i %2 != 0:
        print(f'На нечётной позиции стоит элемент {numbers[i]} ')
        sum += numbers[i]
print(f'Сумма элементов, стоящих на нечётной позиции равна {sum}')