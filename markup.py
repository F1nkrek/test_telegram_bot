from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnMain = KeyboardButton('back')

btnWeather = KeyboardButton('погода')
btnOther = KeyboardButton('IP')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnWeather, btnOther)

# button = types.InlineKeyboardButton(text='Нажми меня!', callback_data='button_clicked')

# app_start = InlineKeyboardMarkup(row_width=2)
# app_start.add(InlineKeyboardButton(text='Погода')
# btnInfo = KeyboardButton('info')
# btnMoney = KeyboardButton('money')
# otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)


