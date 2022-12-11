# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# n = int(input('Задайте длинну списка: '))
# numbers = []
# for i in range(n):
#     numbers.append(int(input('Введите значение: ')))
# print(numbers)
# sum = 0
# for i in range(len(numbers)):
#     if i %2 != 0:
#         print(f'На нечётной позиции стоит элемент {numbers[i]} ')
#         sum += numbers[i]
# print(f'Сумма элементов, стоящих на нечётной позиции равна {sum}')

def Number(text: str, error: str):
    while(True):
        try:
            number = int(input(text))
            return number
        except:
            print(error)
n = Number('Введите значение длинны списка: ', 'Введено некорректное значение')
numbers = []
for i in range(n):
    numbers.append(Number('Введите значение: ', 'Введено некорректное значение'))
print(numbers)
for i in range(len(numbers)):
    res = list(filter(lambda i: i %2 == 0, numbers))
# print(res)
sum = 0
for i in range(len(res)):
    print(f'На нечетной позиции стоит элемент {res[i]}')
    sum += res[i]
print(f'Сумма элементов стоящих на чечетной позиции равна {sum}')

