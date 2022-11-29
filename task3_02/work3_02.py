# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

n = int(input('Задайте длинну списка: '))
numbers = []
for i in range(n):
    numbers.append(int(input('Введите значение: ')))
print(numbers)
sum_of_pairs = []
index1 = 0
index2 = n - 1
sum = 0
while(index1 < index2):
    sum = numbers[index1] * numbers[index2]
    sum_of_pairs.append(sum)
    index1 += 1
    index2 -= 1
if n %2 > 0:
    middle = numbers[n // 2] ** 2
    sum_of_pairs.append(middle)
print('Произведение пар симметричных элементов списка равна ')
print(sum_of_pairs)