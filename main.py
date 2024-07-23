

import logging
from config import Dp, admin, bot
from aiogram.utils import executor
from Handlers import commands, echo, guiz,  FSM_products_details, send_products, webapp, admin_group
from db import main_db
from Handlers import notification

async def on_startup(_):

    await main_db.sql_create()
    for i in admin:
        await bot.send_message(chat_id=i, text="on_startup")
        await bot.send_message(chat_id=i, text="база данных подключена")
    await Dp.bot.delete_webhook()

async def on_shutdown(_):

    for i in admin:
        await notification.send_notification()
        await bot.send_message(chat_id=i, text="on_shutdown")
        await bot.send_message(chat_id=i, text="база данных закрыта")

commands.register_commands(Dp)
guiz.register_quiz(Dp)
FSM_products_details.register_fsm_for_products_details(Dp)
notification.register_notification(Dp)
send_products.register_send_products(Dp)
webapp.register_online_websites(Dp)
admin_group.register_admin(Dp)
# echo.register_echo(Dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(Dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)