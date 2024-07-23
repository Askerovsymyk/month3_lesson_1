import logging
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import admin, bot

spam_words = ["спам", "подписывайтесь", "скидки", "дурак"]
user_warnings = {}

async def welcome_user(message: types.Message):
    for member in message.new_chat_members:
        await message.answer(f"Добро пожаловать в группу, {member.full_name}!")

async def warn_user(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Команда должна быть ответом на сообщение.")
        return

    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.full_name
    user_warnings[user_id] = user_warnings.get(user_id, 0) + 1

    if user_warnings[user_id] >= 3:
        await bot.kick_chat_member(message.chat.id, user_id)
        await message.answer(f"{user_name} был удален за превышение количества спам слов.")
        await bot.send_message(message.chat.id, f"{user_name} был удален за спам.")
    else:
        await message.answer(f"{user_name} получил предупреждение {user_warnings[user_id]}/3.")

async def complete_delete(call: types.CallbackQuery):
    user_id = int(call.data.replace("delete_user", ""))
    try:
        await bot.kick_chat_member(call.message.chat.id, user_id)
        await call.answer(text="Пользователь удален", show_alert=True)
        await bot.send_message(call.message.chat.id, f"Пользователь {user_id} был удален за спам.")
    except Exception as e:
        logging.error(f"Error in complete_delete: {e}")
        await call.answer(text="Ошибка при удалении пользователя.", show_alert=True)

async def filter_spam_words(message: types.Message):
    if any(word in message.text.lower() for word in spam_words):
        await message.delete()
        await warn_user(message)

async def pin_message(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Команда должна быть ответом на сообщение.")
        return

    await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    await message.answer("Сообщение закреплено.")

def register_admin(dp: Dispatcher):
    dp.register_message_handler(welcome_user, content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
    dp.register_message_handler(warn_user, commands=["warn"], commands_prefix=["!/"])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith("delete_user"))
    dp.register_message_handler(filter_spam_words)
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix=["!/"])

