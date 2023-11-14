import os
import requests
from create_bot import dp, bot
import folium
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class MyStates_ip(StatesGroup):
    WAITING_FOR_DATA = State()

async def button_handler_ip(message: types.Message):
    await message.reply('-----Введите IP адрес-----')
    await MyStates_ip.WAITING_FOR_DATA.set()

async def data_handler_ip(message: types.Message, state: FSMContext):
    #data = message.text
    await state.finish()
    try:
        responce = requests.get(url=f'http://ip-api.com/json/{message.text}').json()

        if (responce.get('status') == 'success'):
            dataip = {
                '[IP]': responce.get('query'),
                '[Провайдер]': responce.get('isp'),
                '[Органицация]': responce.get('org'),
                '[Страна]': responce.get('country'),
                '[Регион]': responce.get('regionName'),
                '[Часовой пояс]': responce.get('timezone'),
                '[Город]': responce.get('city'),
                '[Широта]': responce.get('lat'),
                '[Долгота]': responce.get('lon'),
            }
            # preview_text = Figlet(font='slant')
            # await message.answer(preview_text.renderText('findIP'))
            # for k, v in dataip.items():
            #     await message.answer(f'{k} : {v}')

            formatted_dict = '\n'.join([f'{key}: {value}' for key, value in dataip.items()])
            await message.reply(text=formatted_dict)
            area = folium.Map(location=[responce.get('lat'), responce.get('lon')])
            area.save(f'{responce.get("query")}_{responce.get("city")}.html')
            with open(f'{responce.get("query")}_{responce.get("city")}.html', 'rb') as file:
                await bot.send_document(chat_id=message.chat.id, document=file, caption='Геопозиция')
            os.remove(f'{responce.get("query")}_{responce.get("city")}.html')
        else:
            await message.answer("Не корректный IP Адрес!")
    except:
        await message.reply("Нет соединения!")

dp.register_message_handler(button_handler_ip, lambda message: message.text == 'IP')
dp.register_message_handler(data_handler_ip, state=MyStates_ip.WAITING_FOR_DATA)