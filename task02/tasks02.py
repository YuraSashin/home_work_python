# Напишите программу для. проверки истинности утверждения 
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите значение X (0 или 1)'))
y = int(input('Введите значение Y (0 или 1)'))
z = int(input('Введите значение Z (0 или 1)'))
if x < 0 or x > 1 and y < 0 or y > 1 and z < 0 or z > 1:
    print('Введены некорректные числа')
elif x == 0 and y == 0 and z == 0:
    print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
    print('1 = 1 истина')
else:
    print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
    print('0 = 0 ложь')