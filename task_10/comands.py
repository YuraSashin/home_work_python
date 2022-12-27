from bot_config import dp,bot
from aiogram import types
import random
field = [1,2,3,4,5,6,7,8,9]
count = 0

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

def moves(my_list_2: list):
    print(f'{my_list_2[0]} | {my_list_2[1]} | {my_list_2[2]}')
    print('----------')
    print(f'{my_list_2[3]} | {my_list_2[4]} | {my_list_2[5]}')
    print('----------')
    print(f'{my_list_2[6]} | {my_list_2[7]} | {my_list_2[8]}')
    print()

@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.first_name}!')
    await message.answer('Давайте поиграем в крестики-нолики, для этого введите "/Game"')
    print('работа')

@dp.message_handler(commands='Game')
async def game_start(message: types.Message):
    global field
    await message.answer(f'{field[0]} | {field[1]} | {field[2]}')
    await message.answer(f'{field[3]} | {field[4]} | {field[5]}')
    await message.answer(f'{field[6]} | {field[7]} | {field[8]}')
    await message.answer('Выберите координату чтобы поставить "X"')

@dp.message_handler()
async def game(message: types.Message):
    global field
    global count
    if count == 8:
        await message.answer('Ничья, если хотите поиграть еще раз, введите /Game')
        count = 0
    else:
        if message.text.isdigit():
            take = int(message.text) - 1
            if take < 0 or take > 9:
                await message.answer('Вы ввели некорректное число')
            if field[take] == 'X' or field[take] == 'O':
                await message.answer('Ячейка занята')
            else:
                field[take] = 'X'
                count += 1
                moves(field)
                if Game_over(field,'X'):
                    await message.answer(f'{field[0]} | {field[1]} | {field[2]}')
                    await message.answer(f'{field[3]} | {field[4]} | {field[5]}')
                    await message.answer(f'{field[6]} | {field[7]} | {field[8]}')
                    await message.answer('Вы победили, если хотите ещё поиграть,введите /Game')
                    field = [1,2,3,4,5,6,7,8,9]
                    count = 0
                else:
                    bot = random.randint(0,8)
                    while field[bot] == 'X' or field[bot] == 'O':
                        bot = random.randint(0,8)
                    field[bot] = 'O'
                    count += 1
                    moves(field)
                    await message.answer(f'Я выбрал ячейку {bot + 1}')
                    if Game_over(field,'O'):
                        await message.answer(f'{field[0]} | {field[1]} | {field[2]}')
                        await message.answer(f'{field[3]} | {field[4]} | {field[5]}')
                        await message.answer(f'{field[6]} | {field[7]} | {field[8]}')
                        await message.answer('Я победил,если хотите ещё поиграть, введите /Game')
                        field = [1,2,3,4,5,6,7,8,9]
                        count = 0
                    else:
                        await message.answer(f'{field[0]} | {field[1]} | {field[2]}')
                        await message.answer(f'{field[3]} | {field[4]} | {field[5]}')
                        await message.answer(f'{field[6]} | {field[7]} | {field[8]}')
                        await message.answer('Ваш ход')
        else:
            await message.answer('Введено некорректное значение')
