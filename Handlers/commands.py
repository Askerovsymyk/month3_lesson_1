
import random
import glob
import os
from aiogram import types, Dispatcher
from aiogram.types import InputFile
from config import bot


async def send_photo(message: types.Message):
    pixmap = r"Media/"
    files = glob.glob(os.path.join(pixmap, "*"))
    random_files = random.choice(files)
    await message.answer_photo(photo=InputFile(random_files))
    await message.delete()


async def send_file(message: types.Message):
    file_path = "echo.txt"
    if os.path.exists(file_path):
        await bot.send_document(chat_id=message.chat.id, document=open(file_path, 'rb'))
        await message.delete()
    else:
        await message.answer("Нет такого файла.")

async def help_command(message: types.Message):

         help_text = """
                      Если ввести число, оно будет возведено в квадрат.\n
                      Команда 'mem' выводит случайную картинку.\n
                      Команда 'sendfile' отправляет файл.\n
                      Если введена неправильная команда, будет эхо.\n
                      Команда /help выводит инструкцию для этого телеграм бота.\n
                      команда /game выводи игру с ботам\n
                      команда /registration выводит регистрацию покупку в магазина\n
                      команда /registration2 выводит регистрацию покупку в магазина\n
                      команда /notification выводит уведомление 
                              
                     """

         await message.answer(f"{help_text}")
         await message.delete()


def register_commands(Dp: Dispatcher):

    Dp.register_message_handler(send_photo, commands=["mem", "мем"])
    Dp.register_message_handler(send_file, commands=["sendfile"])
    Dp.register_message_handler(help_command, commands=["help"])