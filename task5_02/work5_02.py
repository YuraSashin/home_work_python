# Создайте программу для игры в ""Крестики-нолики""
import random
def Number(text: str, error: str):
    while(True):
        try:
            number = int(input(text))
            if number > 0 and number < 10:
                return number
            else:
                print(error)
        except:
            print(error)
field = [1,2,3,4,5,6,7,8,9]
def Moves(my_list_2: list):
    print(f'{my_list_2[0]} | {my_list_2[1]} | {my_list_2[2]}')
    print('----------')
    print(f'{my_list_2[3]} | {my_list_2[4]} | {my_list_2[5]}')
    print('----------')
    print(f'{my_list_2[6]} | {my_list_2[7]} | {my_list_2[8]}')
    print()
Moves(field)
def Game(my_list: list):
    count = 1
    while count < 10:
        move = Number('Выберите координату(1-9) чтобы поставить " Х " ' , 'Введено некорректное значение') - 1
        while my_list[move] == 'X' or my_list[move] == 'O':
            print('Ячейка занята, выберите другую')
            move = Number('Выберите координату(1-9) чтобы поставить " Х " ' , 'Введено некорректное значение') - 1
        my_list[move] = 'X'
        print(f'Вы выбрали {move}')
        Moves(my_list)
        if Game_over(my_list,'X'):
            print('Вы победили')
            break
        if count == 9:
            print('Ничья')
            break
        bot = random.randint(0,8)
        while my_list[bot] == 'X' or my_list[bot] == 'O':
            bot = random.randint(0,8)
        print(f'Бот выбрал {bot + 1}')
        my_list[bot] = 'O'
        Moves(my_list)
        if Game_over(my_list,'O'):
            print('Победил бот')
            break
        count += 2
def Game_over(my_list_2: list , temp: str) -> bool:
    if my_list_2[0] == my_list_2[1] == my_list_2[2] == temp:
        return True
    elif my_list_2[3] == my_list_2[4] == my_list_2[5] == temp:
        return True
    elif my_list_2[6] == my_list_2[7] == my_list_2[8] == temp:
        return True
    elif my_list_2[0] == my_list_2[3] == my_list_2[6] == temp:
        return True
    elif my_list_2[1] == my_list_2[4] == my_list_2[7] == temp:
        return True
    elif my_list_2[2] == my_list_2[5] == my_list_2[8] == temp:
        return True
    elif my_list_2[0] == my_list_2[4] == my_list_2[8] == temp:
        return True
    elif my_list_2[2] == my_list_2[4] == my_list_2[6] == temp:
        return True
    else:
        return False 
print('Вы ходите первым')
Game(field)


