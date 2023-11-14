from config import bot_father_token
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(bot_father_token)
dp = Dispatcher(bot, storage=MemoryStorage())