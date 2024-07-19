
from aiogram import types, Dispatcher
from config import bot
import random




async def echo(message: types.Message):

    bot_win = {"bot win": 0}
    user_win = {"user win": 0}

    if message.text.strip().isdigit():
        replace_int = int(message.text)
        digits_pow = pow(replace_int, 2)
        await message.answer(
                              text="ваша число возведенное в квадрат \n"
                              f"{replace_int} ^ 2 = {digits_pow}"
                             )
        await message.delete()

    elif message.text.strip() == "/game":
         games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
         random_games = random.choice(games)
         user_dice = await bot.send_dice(chat_id=message.chat.id, emoji=random_games)
         user_value = user_dice.dice.value
         bot_dice = await bot.send_dice(chat_id=message.chat.id, emoji=random_games)
         bot_value = bot_dice.dice.value
         if bot_value > user_value:
             bot_win["bot win"] += 1
             await message.answer(text="бот выиграл")


         elif bot_value < user_value:
             user_win["user win"] += 1
             await message.answer(text="user выиграл")


         else:
             await message.answer(text="ничья")



    elif message.text == "/result_games":

        await message.answer(f"bot win : {bot_win}")
        await message.answer(f"user win: {user_win}")


    else:
         await message.answer(f"нет такой команды :'{message.text}' ")



def register_echo(Dp: Dispatcher):
    Dp.register_message_handler(echo)
