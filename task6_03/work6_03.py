# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве 
# (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
# задача 5 семинар 1

# x1 = int(input('Введите значение х1: '))
# y1 = int(input('Введите значение y1: '))
# z1 = int(input('Введите значение z1(для 3D пространства)'))
# x2 = int(input('Введите значение х2: '))
# y2 = int(input('Введите значение y2: '))
# z2 = int(input('Введите значение z2(для 3D пространства)'))
# distance2D = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 4)
# print(f'Точка А({x1},{y1}), точка В({x2},{y2})')
# print(f'Расстояние между ними в 2D = {distance2D}')
# distance3D = round(((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5, 4)
# print(f'Точка А({x1},{y1},{z1}), точка В({x2},{y2},{z2})')
# print(f'Расстояние между ними в 3D = {distance3D}')
def Number(text: str, error: str):
    while(True):
        try:
            number = int(input(text))
            return number
        except:
            print(error)
x1 = Number('Введите значение Х1:' , 'Введено некорректное значение')
y1 = Number('Введите значение Y1:' , 'Введено некорректное значение')
z1 = Number('Введите значение Z1(для 3D пространства):' , 'Введено некорректное значение')
x2 = Number('Введите значение Х2:' , 'Введено некорректное значение')
y2 = Number('Введите значение Y2:' , 'Введено некорректное значение')
z2 = Number('Введите значение Z2(для 3D постранства):' , 'Введено некорректное значение')
res = lambda a,b: a - b
distance2D = round(((res(x2,x1)) ** 2 + (res(y2,y1)) ** 2) ** 0.5, 4)
print(f'Точка А({x1},{y1}), точка В({x2},{y2})')
print(f'Расстояние между ними в 2D = {distance2D}')
distance3D = round(((res(x2,x1)) ** 2 + (res(y2,y1)) ** 2 + (res(z2,z1)) ** 2) ** 0.5, 4)
print(f'Точка А({x1},{y1},{z1}), точка В({x2},{y2},{z2})')
print(f'Расстояние между ними в 3D = {distance3D}')
