import findIP
import weather
from aiogram import types
from aiogram.utils import executor
from create_bot import dp
import markup


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer('Привет', reply_markup=markup.mainMenu)
    #weather.bot_message()


if __name__ == '__main__':
    executor.start_polling(dp)