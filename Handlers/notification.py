


from apscheduler.schedulers.asyncio import  AsyncIOScheduler
import datetime
from config import bot
from apscheduler.triggers.cron import CronTrigger
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

# cron

user = [6120256197, ]
notification = []

class Notification(StatesGroup):

      waiting_for_message = State()

async def send_notification():
    for i in user:
        if notification:
            message = notification.pop(0)

        else:
            message = "у вас нет запланированных задач"

        await bot.send_message(chat_id=i, text=f"напоминание\n"
                                           f"добрый день! не забудьте про - {message}")

async  def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(send_notification, CronTrigger(hour="19", minute="00", start_date=datetime.datetime.now()))
    scheduler.state()


async def handler_notification_command(message: types.Message):
    await message.reply(text="введите сообщение для уведомление:")
    await Notification.waiting_for_message.set()

async def handler_notification_text(message: types.Message, state: FSMContext):
    notification_message = message.text
    notification.append(notification_message)

    await message.reply(text=f"сообщение {notification_message} добавлено в список уводомленние")
    await state.finish()


def register_notification(Dp: Dispatcher):
    Dp.register_message_handler(handler_notification_command, commands=["notification"])
    Dp.register_message_handler(handler_notification_text, state=Notification.waiting_for_message)





