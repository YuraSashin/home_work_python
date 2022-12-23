from bot_config import dp,bot
from aiogram import types
import random
total = random.randint(60,300)
move = random.randint(0,2)

@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.first_name}!')
    await message.answer('Давайте поиграем в конфеты, для этого введите "/Game", я объясню правила')
    print('работа')

@dp.message_handler(commands='Game')
async def game_start(message: types.Message):
    global move
    global total
    await message.answer('На столе лежит какое-то колличество конфет.\n Можно взять от 1 до 28 за ход, первый ход определится случайным образом.\nКто возьмёт последние конфеты, тот победил')
    if move == 0:
        await message.answer(' Первый ход достанется вам')
        await message.answer(f'На столе лежит {total} конфет')
    else:
         await message.answer('Я хожу первым')
         bot_one_move = random.randint(0,29)
         await message.answer(f'На столе лежит {total} конфет, я взял {bot_one_move}, осталось {total - bot_one_move} ')
         total -= bot_one_move
    await game()

@dp.message_handler()
async def game(message: types.Message):
    global total
    if message.text.isdigit():
        if total > 0:
            take = int(message.text)
            if take > 0 and take < 29:
                if take > total:
                    await message.answer('Вы не можете взять больше чем есть на столе')
                else:
                    total -= take
                    print(f'взяли {take} осталось {total}')
                    if total == 0:
                        await message.answer(f'{message.from_user.first_name} Поздравляю с победой!')
                        await message.answer('Если вы хотите поиграть еще раз, введите команду "/Game"')
                        total = random.randint(60,300)
                    else:
                        await message.answer(f'Вы взяли {take} конфет, осталось {total} ')
                        take_bot = 0
                        if total < 58 and total > 29:
                            take_bot = total - 29
                        elif total < 29:
                            take_bot = total
                        else:
                            take_bot = random.randint(1,29)
                        total -= take_bot
                        print(f'взяли {take_bot} осталось {total}')
                        if total == 0:
                            await message.answer(f'Я забираю оставшие конфеты ({take_bot}) и победа за мной!)')
                            await message.answer('Если хотите взять реванш, ВВедите команду "/Game"')
                            total = random.randint(60,300)
                        else:
                            await message.answer(f'Я взял {take_bot}, осталось{total} конфет, Ваш ход')
            else:
                await message.answer(f'{message.from_user.first_name}  Нужно ввести целое число от 1 до 28')
    else:
        await message.answer(f'{message.from_user.first_name}  Нужно ввести целое число от 1 до 28')       






    

