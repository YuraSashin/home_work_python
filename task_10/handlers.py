from aiogram import types,Dispatcher

import comands

def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(comands.start_bot, commands= 'start')
    dp.register_message_handler(comands.game_start, commands= 'Game')
    dp.register_message_handler(comands.game)