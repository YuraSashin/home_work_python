# Создайте программу для игры с конфетами. Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Подумайте как наделить бота ""интеллектом""

import random
def Number(text: str, error: str):
    while(True):
        try:
            number = int(input(text))
            if number > 0:
                return number
            else:
                print(error)
        except:
            print(error)
def Game(move_int,candies_int):
    while candies_int > 0:
        if move_int == 0:
            player = Number('Сколько конфет вы хотите взять(не более 28):' , 'Введено некорректное значение')
            while player > 29 or player > candies_int:
                print('Введено некорректное значение')
                player = Number('Сколько конфет вы хотите взять(не более 28):' , 'Введено некорректное значение')
            print(f'Колличество конфет {candies_int}, Вы взяли {player}')
            candies_int -= player
            print(f'Осталось конфет {candies_int}')
            if candies_int == 0:
                print('Поздравляю, Вы победили!')
                break
            if candies_int < 58 and candies_int > 29:
                bot = candies_int - 29
            elif candies_int < 29:
                bot = candies_int
            else:
                bot = random.randint(1,29)
            print(f'Бот взял {bot} конфет')
            candies_int -= bot
            print(f'Осталось конфет {candies_int}')
            if candies_int == 0:
                print('Победил бот')
        else:
            if candies_int < 58 and candies_int > 29:
                bot = candies_int - 29
            elif candies_int < 29:
                bot = candies_int
            else:
                bot = random.randint(1,29)
            print(f'Колличество конфет {candies_int}, Бот взял {bot}')
            candies_int -= bot
            print(f'Осталось конфет {candies_int}')
            if candies_int == 0:
                print('Победил бот')
                break
            player = Number('Сколько конфет вы хотите взять(не более 28):' , 'Введено некорректное значение')
            while player > 28 or player > candies_int:
                print('Введено некорректное значение')
                player = Number('Сколько конфет вы хотите взять(не более 28):' , 'Введено некорректное значение')
            print(f'Вы взяли {player} конфет')
            candies_int -= player
            print(f'Осталось {candies_int}')
            if candies_int == 0:
                print('Поздравляю, Вы победили!')
candies = Number('Введите колличество конфет: ' , 'Введено некорректное значение')
move = random.randint(0,2)
if move == 0:
    print('Поздравляю, первым ходите Вы')
else:
    print('Первым ходит бот')
Game(move,candies)
