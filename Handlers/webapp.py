

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, ReplyKeyboardMarkup
from aiogram import Dispatcher, types


async def online_websites(message: types.Message):
    button_inline = InlineKeyboardMarkup(row_width=1)

    button_inline.add(
                        InlineKeyboardButton(text="Chat Gpt", web_app=WebAppInfo(url="https://chatgpt.com")),
                        InlineKeyboardButton(text="Geeks online", web_app=WebAppInfo(url="https://online.geeks")),
                        InlineKeyboardButton(text="News", web_app=WebAppInfo(url="https://www.youtube.com")),
                        InlineKeyboardButton(text="copilot", web_app=WebAppInfo(url="https://copilot.microsoft.com")),
                        InlineKeyboardButton(text="canva", web_app=WebAppInfo(url="https://www.canva.com"))
                     )
    await message.answer(text="нажмите на кнопку для перехода на сайт", reply_markup=button_inline)


def register_online_websites(Dp: Dispatcher):

    Dp.register_message_handler(online_websites, commands=["openwebsites"])

