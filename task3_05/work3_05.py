# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите длину спика чисел Фиббоначи: '))
firstNum = 0
secondNum = 1
numbers = [secondNum,firstNum,secondNum]
fibonacci = 0
negafibonacci = 0
for i in range(n - 1):
    fibonacci = firstNum + secondNum
    numbers.append(fibonacci)
    if i %2 == 0:
        negafibonacci = -fibonacci
        numbers.insert(0,negafibonacci)
    else:
        negafibonacci = fibonacci
        numbers.insert(0,negafibonacci)
    firstNum = secondNum
    secondNum = fibonacci
print(f'для n = {n} список будет выглядеть так:')
print(numbers)


    
