import requests
import datetime
from aiogram import types
from config import open_weather_token
from create_bot import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class MyStates_wet(StatesGroup):
    WAITING_FOR_DATA = State()

async def button_handler_wet(message: types.Message):
    await message.reply('-----Введите город!-----')
    await MyStates_wet.WAITING_FOR_DATA.set()

async def data_handler_wet(message: types.Message, state: FSMContext):

    await state.finish()
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F23B",
    }
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_deg = data["wind"]["deg"]
        wind_speed = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%d.%m.%Y %H:%M')
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%d.%m.%Y %H:%M')
        length_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Смайл отсутствует в словаре!"

        await message.answer(f"Погода на {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')} в городе: {city}\n{wd}\n"
                             f"Температура: {round(cur_weather)}С°\nВлажность: {humidity}%\nДавление: {pressure}\nВетер: {wind_deg}/{wind_speed}\n"
                             f"Восход: {sunrise}\nЗакат: {sunset}\nПродолжительльность дня: {length_day}"
                             )

    except:
        await message.reply("Проверить город!")

dp.register_message_handler(button_handler_wet, lambda message: message.text == 'погода')
dp.register_message_handler(data_handler_wet, state=MyStates_wet.WAITING_FOR_DATA)