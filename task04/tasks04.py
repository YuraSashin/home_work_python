# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите значение четверти(1-4): '))
if a < 1 or a > 4:
    print('Введено некорректное значение')
elif a == 1:
    print('x(min 0; max ∞) у(min 0; max ∞)')
elif a == 2:
    print('x(min -∞; max 0) y(min 0; max ∞)')
elif a == 3:
    print('x(min -∞; max 0) y(min -∞ max 0)')
else:
    print('x(min 0;(max ∞) y(min -∞, max 0)')