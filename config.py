

from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


admin = [6120256197, ]

TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
storage = MemoryStorage()
Dp = Dispatcher(bot=bot, storage=storage)

