# ДОПОЛНИТЕЛЬНО, НО НЕОБЯЗАТЕЛЬНО:
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

n = int(input('Введите значение длинны списка '))
import random
ran = range(1, n + 1)
numbers = list(ran)
for i in range(len(numbers)):
    temp = random.randint(1000,10000)
    numbers[i] = temp
print(f'1 этап {numbers}')
delete = input('Введите цифру (0-9), которую хотите удалить ')
if int(delete) < 0 or int(delete) > 9:
    print('Введено некорректное значение')
for i in range(n):
    numbers[i] = int(str(numbers[i]).replace(delete, ''))
print(f'2 этап {numbers}')
for i in range(n):
    while(numbers[i] > 9 ):
        sum = 0
        count = str(numbers[i])
        for j in count:
            sum += int(j) 
        numbers[i] = sum 
    print(f'3 этап {numbers}')
numbers2 = []
for i in range(n):
    if numbers[i] not in numbers2:
        numbers2.append(numbers[i])
print(f'4 этап {numbers2}')
    





