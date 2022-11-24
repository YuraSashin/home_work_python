# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.

n = int(input('Введите чиcло '))
ran = range(1, n + 1)
numbers = list(ran)
sum = 0
for i in numbers:
    numbers[i - 1] = round((1 + 1 / i) ** i, 2)
    sum += numbers[i - 1]
print(numbers)
print(round(sum, 2))
