


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, Dispatcher
from aiogram import types



async def quiz(message: types.Message):
    button0 = InlineKeyboardMarkup(row_width=2)
    button0.add(
                InlineKeyboardButton("Закрыт опрос", callback_data="close_quiz"),
                InlineKeyboardButton("Следующий опрос", callback_data="next_quiz1")
               )
    question = "Какая столица Франции?"
    answer = ["А) Рим", "Б) Мадрид", "В) Париж", "Г) Берлин"]

    await message.delete()
    await bot.send_poll(
                        chat_id=message.from_user.id,
                        question=question,
                        options=answer,
                        is_anonymous=True,
                        type="quiz",
                        correct_option_id=2,
                        explanation="правильно",
                        open_period=60,
                        reply_markup=button0
                        )

async def quiz1(call: types.CallbackQuery):

    button1 = InlineKeyboardMarkup(row_width=2)
    button1.add(
                InlineKeyboardButton("Закрыт опрос", callback_data="close_quiz"),
                InlineKeyboardButton("Следующий опрос", callback_data="next_quiz2")
                )

    question = "Кто написал пьесу «Ромео и Джульетта»?"
    answer = ["А) Уильям Шекспир", "Б) Чарльз Диккенс", "В) Джейн Остин", "Г) Марк Твен"]

    await bot.send_poll(
                          chat_id=call.from_user.id,
                          question=question,
                          options=answer,
                          is_anonymous=True,
                          type="quiz",
                          correct_option_id=0,
                          explanation="правильно",
                          open_period=60,
                          reply_markup=button1
                          )

async def quiz2(call: types.CallbackQuery):
    button2 = InlineKeyboardMarkup(row_width=1)
    button2.add(
        InlineKeyboardButton("Закрыт опрос", callback_data="close_quiz"),
    )

    question = "Какая планета в нашей С+олнечной системе самая большая?"
    answer = ["А) Земля", "Б) Юпитер", "В) Марс", "Г) Сатурн"]


    await bot.send_poll(
                        chat_id=call.from_user.id,  # - идентификатор чата
                        question=question,  # - вопрос
                        options=answer,  # -  параметры
                        is_anonymous=True,  # - анонимно
                        type="quiz",  # - тип
                        correct_option_id=1,  # - правильный идентификатор опции
                        explanation="правильно",  # - объяснение
                        open_period=60,  # - открытый период
                        reply_markup=button2  # - разметка ответа
                        )

async def close_quiz(call: types.CallbackQuery):
    await call.message.delete()

def register_quiz(Dp: Dispatcher):
    Dp.register_message_handler(quiz, commands=["quiz"])
    Dp.register_callback_query_handler(quiz1, text="next_quiz1")
    Dp.register_callback_query_handler(quiz2, text="next_quiz2")
    Dp.register_callback_query_handler(close_quiz, text="close_quiz")
